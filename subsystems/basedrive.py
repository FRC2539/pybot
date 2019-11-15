from .debuggablesubsystem import DebuggableSubsystem

import math

import subsystems

from ctre import ControlMode, NeutralMode, FeedbackDevice
from rev import CANSparkMax, MotorType, ControlType, ConfigParameter, IdleMode

from networktables import NetworkTables
from networktables import NetworkTables as nt

from navx.ahrs import AHRS

import pathfinder as pf
from pathfinder.followers import EncoderFollower

from custom.config import Config
import ports
import robot


class BaseDrive(DebuggableSubsystem):
    '''
    A general case drive train system. It abstracts away shared functionality of
    the various drive types that we can employ. Anything that can be done
    without knowing what type of drive system we have should be implemented here.
    '''

    def __init__(self, name):
        super().__init__(name)

        '''
        Create all motors, disable the watchdog, and turn off neutral braking
        since the PID loops will provide braking.
        '''
        try:
            self.motors = [
                CANSparkMax(ports.drivetrain.frontLeftMotorID, MotorType.kBrushless),
                CANSparkMax(ports.drivetrain.frontRightMotorID, MotorType.kBrushless),
                CANSparkMax(ports.drivetrain.backLeftMotorID, MotorType.kBrushless),
                CANSparkMax(ports.drivetrain.backRightMotorID, MotorType.kBrushless),
            ]

        except AttributeError:
            print('error in init basedrive')
            self.motors = [
                CANSparkMax(ports.drivetrain.leftMotorID, MotorType.kBrushless),
                CANSparkMax(ports.drivetrain.rightMotorID, MotorType.kBrushless),
            ]

        self.activeMotors = self.motors[0:2]

        self.encoders = []
        self.PIDcontrollers = []

        for motor in self.motors:
            motor.setIdleMode(IdleMode.kBrake)
            self.encoders.append(motor.getEncoder())
            self.PIDcontrollers.append(motor.getPIDController())
            motor.setEncPosition(0.0)

        self.activeEncoders = []
        self.activePIDControllers = []

        for motor in self.motors[0:2]:
            self.activeEncoders.append(motor.getEncoder())
            self.activePIDControllers.append(motor.getPIDController())


        for encoder in self.encoders:
            encoder.setPositionConversionFactor(1)
            encoder.setVelocityConversionFactor(1)

        self.resetPID()

        self.resetEncoders()

        '''
        Subclasses should configure motors correctly and populate activeMotors.
        '''

        self.nt = nt.getTable('DriveTrain')

        self.driveMode = True

        self.activeMotors = []
        self._configureMotors()

        '''Initialize the navX MXP'''
        self.navX = AHRS.create_spi()
        self.resetGyro()
        self.flatAngle = 0

        '''A record of the last arguments to move()'''
        self.lastInputs = None

        self.driveSpeedMult = Config('DriveTrain/driveSpeedMult', 0.85)
        self.defenseSpeedMult = Config('DriveTrain/defenseSpeedMult', 1.2)

        self.chosenSpeed = 1

        self.setUseEncoders(True)
        self.maxSpeed = 1#Config('DriveTrain/maxSpeed', 2500)
        self.speedLimit = Config('DriveTrain/normalSpeed', 2000)
        self.deadband = Config('DriveTrain/deadband', 0.05)
        self.maxPercentVBus = 1
        self.boost = False

        self.rotationsPerInch = Config('DriveTrain/rotationsPerInch', 0.568)

        '''Allow changing CAN Talon settings from dashboard'''
        self._publishPID('Speed', 0)
        self._publishPID('Position', 1)


        '''Add items that can be debugged in Test mode.'''
        self.debugSensor('navX', self.navX)
        #self.debugMotor('Front Left Motor', self.motors[0])
        #self.debugMotor('Front Right Motor', self.motors[1])

        #try:
            #self.debugMotor('Back Left Motor', self.motors[2])
            #self.debugMotor('Back Right Motor', self.motors[3])
        #except IndexError:
            #pass

        #self.motors[3].setInverted()


    def initDefaultCommand(self):
        '''
        By default, unless another command is running that requires this
        subsystem, we will drive via joystick using the max speed stored in
        Config.
        '''
        from commands.drivetrain.drivecommand import DriveCommand

        self.setDefaultCommand(DriveCommand(self.speedLimit))


    def move(self, x, y, rotate):
        '''Turns coordinate arguments into motor outputs.'''

        '''
        Short-circuits the rather expensive movement calculations if the
        coordinates have not changed.
        '''
        if [x, y, rotate] == self.lastInputs:
            return
        if [x, y, rotate] == [0, 0, 0]:
            self.stop()
            return


        self.lastInputs = [x, y, rotate]

        '''Prevent drift caused by small input values'''
        if self.useEncoders:
            x = math.copysign(max(abs(x) - self.deadband, 0), x)
            y = math.copysign(max(abs(y) - self.deadband, 0), y)
            rotate = math.copysign(max(abs(rotate) - self.deadband, 0), rotate)

        speeds = self._calculateSpeeds(x, y, rotate)
        '''Prevent speeds > 1'''
        maxSpeed = 0
        for speed in speeds:
            maxSpeed = max(abs(speed), maxSpeed)

        if maxSpeed > 1:
            speeds = [x / maxSpeed for x in speeds]


        '''Use speeds to feed motor output.'''
        if self.useEncoders:
            if not any(speeds):
                '''
                When we are trying to stop, clearing the I accumulator can
                reduce overshooting, thereby shortening the time required to
                come to a stop.
                '''
                for motor in self.motors:
                    motor.setIAccum(0)

            #print("moving")
            #print(speeds)
            #print("boost: "+ str(self.boost))

            x = 0
            if self.boost:
                for motor, speed in zip(self.motors, speeds):
                    motor.set(speed * self.chosenSpeed)
                    x = x + 1

            else:
                for motor, speed in zip(self.motors, speeds):
                    tmaxspeed = (self.maxSpeed / 100)
                    speed = (speed * 1)

                    if speed > 0.0 and speed > tmaxspeed:
                        speed = tmaxspeed

                    if speed < 0.0 and speed < (tmaxspeed * -1):
                       speed = (tmaxspeed * -1)

                    motor.set(speed * self.chosenSpeed)
                    x = x + 1





            #for motor, speed in zip(self.activeMotors, speeds):
                #print(str('speed' + str(self.chosenSpeed)))
                #motor.set(speed * self.chosenSpeed)

        else:
            for motor, speed in zip(self.motors, speeds):
                motor.set(speed * self.chosenSpeed)

        if [x, y, rotate] == self.lastInputs:
            return
        if [x, y, rotate] == [0, 0, 0]:
            self.stop()
            return

    def toggleSpeed(self):
        if self.driveMode:
            self.chosenSpeed = abs(self.defenseSpeedMult.getValue())
            self.nt.putBoolean('DriveTrain/boost', True)
            self.driveMode = False

        else:
            self.chosenSpeed = abs(self.driveSpeedMult.getValue())
            self.nt.putBoolean('DriveTrain/boost', False)
            self.driveMode = True

        return self.driveMode

    def movePer(self, left, right):
        #speeds = self._calculateSpeeds(x, y, rotate / 2)
        #print("l: "+str(left)+" r:"+str(right))
        x = 0
        for motor in self.activeMotors:
            #print("x: "+str(x%2))
            motor.setIntegralAccumulator(0, 0, 0)
            if x % 2 == 0:
                motor.set(ControlMode.PercentOutput, left)
                #print("motor "+ str(x) + ": "+str(left))
            else:
                motor.set(ControlMode.PercentOutput, right * -1)
                #print("motor "+ str(x) + ": "+str(right * -1))
            x += 1

    def setPositions(self, positions):
        print('STARTED SETPOSITIONS\n\n')

        '''
        Have the motors move to the given positions. There should be one
        position per active motor. Extra positions will be ignored.
        #'''
        print('this is the positions var: '+ str(positions))

        #for controller, position in zip(self.PIDcontrollers, positions):
            #controller.setReference(position,ControlType.kPosition,0,0)
            #print('applied this position to the controller ' + str(position))
        print(str(self.PIDcontrollers))

        self.PIDcontrollers[0].setReference(float(positions[0]), ControlType.kPosition, 0, 0.0)
        self.PIDcontrollers[1].setReference(float(positions[1]), ControlType.kPosition, 0, 0.0)
        self.PIDcontrollers[2].setReference(float(positions[2]), ControlType.kPosition, 0, 0.0)
        self.PIDcontrollers[3].setReference(float(positions[3]), ControlType.kPosition, 0, 0.0)

        print(str(self.encoders[2].getPosition()))
        print(str(self.encoders[3].getPosition()))


        print('Current positions my dude ' + str(self.getPositions()))

        return self.getPositions()

            #while(max(self.getPositions())<positions+max(currentPos):
             #   print("still moving")
            #self.stop()
            #print("Done moving")
        '''elif (positions<0)
            self.move(0,-.2,0)
            while(max(self.getPositions())>positions+max(currentPos):
                print("still moving")
            self.stop()
            print("Done moving")
        '''


    '''
    def setPositions(self, positions):
        if not self.useEncoders:
            raise RuntimeError('Cannot set position. Encoders are disabled.')

        for motor, position, encoder in zip(self.activeMotors, positions, self.encoders):
            encoder.setPosition(position)
            motor.setSmartMotionMaxVelocity(4000)
    '''
    def averageError(self, targetPos):
        '''Find the average distance between setpoint and current position.'''
        error = 0
        for motor, encoder, target in zip(self.activeMotors, self.encoders, targetPos):
            error += abs(target - encoder.getPosition())
#          error += abs(motor.getClosedLoopTarget(0) - encoder.getPosition())

        print('error ' + str(error))
        return error / len(self.activeMotors)


    def atPosition(self, target, tolerance=10):
        '''
        Check setpoint error to see if it is below the given tolerance.
        '''
        return self.averageError(target) <= tolerance


    def stop(self):
        '''Disable all motors until set() is called again.'''
        for motor in self.activeMotors:
            motor.stopMotor()

        self.lastInputs = None


    def resetPID(self):
        '''Set all PID values to 0 for profiles 0 and 1.'''
        for motor in self.activeMotors:
            controller = motor.getPIDController()
            motor.setClosedLoopRampRate(0.25)
            motor.setOpenLoopRampRate(0.25)

            for profile in range(2):
                controller.setP(0.05, profile)
                controller.setI(0, profile)
                controller.setD(0.1, profile)
                controller.setFF(0, profile)
                controller.setIZone(0, profile)
                controller.setOutputRange(-1, 1, profile)

    def resetGyro(self):
        '''Force the navX to consider the current angle to be zero degrees.'''

        self.setGyroAngle(0)

    def resetNavXDisplacement(self):
        '''Resets the accelerometer on the navX'''

        self.navX.resetDisplacement()


    def setGyroAngle(self, angle):
        '''Tweak the gyro reading.'''

        self.navX.reset()
        self.navX.setAngleAdjustment(angle)


    def getAngle(self):
        '''Current gyro reading'''

        return self.navX.getAngle() % 360


    def getAngleTo(self, targetAngle):
        '''
        Returns the anglular distance from the given target. Values will be
        between -180 and 180, inclusive.
        '''
        degrees = targetAngle - self.getAngle()
        while degrees > 180:
            degrees -= 360
        while degrees < -180:
            degrees += 360

        return degrees

    def setSideSpeeds(self, left, right):
        self.activeMotors[0].set(left)
        self.activeMotors[1].set(right)

    def getFrontLeftPosition(self):
        return self.encoders[0].getPosition()

    def getFrontRightPosition(self):
        return self.encoders[1].getPosition()

    def createEncoderFollowers(self, modifier):
        left = EncoderFollower(modifier.getLeftTrajectory())
        right = EncoderFollower(modifier.getRightTrajectory())

        left.configureEncoder(int(self.activeEncoders[0].getPosition()), 11,  0.5)
        right.configureEncoder(int(self.activeEncoders[1].getPosition()), 11,  0.5)
        # refer to documentation

        # 1.7 is the max velocity
        left.configurePIDVA(0.05, 0.0, 0.1, (1 / 1.7), 0)
        right.configurePIDVA(0.05, 0.0, 0.1, (1 / 1.7), 0)

        return left, right

    def pointsToPathfinder(self, points):
        finalList = []
        var = 0
        try:
            for coordinate in points:
                var = pf.Waypoint(int(coordinate[0]), int(coordinate[1]), math.radians(coordinate[2]))
                finalList.append(var)
        except ValueError:
            raise ValueError('Submitted a noninteger value to pathfinder')

        return finalList

    def getXDisplacement(self):
        '''Returns x-axis displacement of robot since the last reset, in INCHES'''
        return (self.navX.getDisplacementX() * 39.3701)


    def getYDisplacement(self):
        '''Returns y-axis displacement of robot since the last reset, in INCHES'''
        return (self.navX.getDisplacementY() * 39.3701)


    def inchesToRotations(self, distance):
        '''Converts a distance in inches into a number of encoder ticks.'''
        rotationsNeeded = (distance / (math.pi * 6)) * 10.7 #Config('DriveTrain/wheelDiameter', 6)) math * 6 is 18.85

        return float(rotationsNeeded) #* Config('DriveTrain/ticksPerRotation', 4096))


    def resetTilt(self):
        self.flatAngle = self.navX.getPitch()


    def getTilt(self):
        return self.navX.getPitch() - self.flatAngle


    def getAcceleration(self):
        '''Reads acceleration from NavX MXP.'''
        return self.navX.getWorldLinearAccelY()


    def getSpeeds(self):
        '''Returns the speed of each active motors.'''
        speeds = []
        for enc in self.activeEncoders:
            speeds.append(enc.getVelocity())

        return speeds

    def getPositions(self):
        '''Returns the position of each active motor.'''
        self.pos = []

        try:
            for x in self.encoders:
                self.pos.append(x.getPosition())

            return self.pos

        except(AssertionError):
            print('Assertion Error raised . . . ignoring!')
            return [0, 0, 0, 0]

    def getFrontClearance(self):
        '''Override this in drivetrain if a distance sensor is attached.'''
        raise NotImplementedError


    def getRearClearance(self):
        '''Override this in drivetrain if a rear distance sensor is attached.'''
        raise NotImplementedError


    def setUseEncoders(self, useEncoders=True):
        '''
        Turns on and off encoders. As a side effect, if encoders are enabled,
        the motors will be set to speed mode. Disabling encoders should not be
        done lightly, as many commands rely on encoder information.
        '''
        self.useEncoders = useEncoders


    def getEncoders(self):
        encoders = []
        for motor in self.motors:
            encoders.append(motor.getEncoder())
        return encoders

    def resetEncoders(self):
        for motor, encoder in zip(self.motors, self.encoders):
            motor.setEncPosition(0.0)
            encoder.setPosition(0.0)
            encoder.setPositionConversionFactor(1.0)

        print('reset ' + str(self.getPositions()))
        #print("reseted enc")


    def setSpeedLimit(self, speed):
        '''
        Updates the max speed of the drive and changes to the appropriate
        mode depending on if encoders are enabled.
        '''
        speed = int(speed)

        if speed <= 0:
            raise ValueError('DriveTrain speed must be greater than 0')

        self.speedLimit = speed
        if speed > self.maxSpeed:
            self.maxSpeed = speed

        '''If we can't use encoders, attempt to approximate that speed.'''
        self.maxPercentVBus = speed / self.maxSpeed
        #print("maxPercVBus: "+str(self.maxPercentVBus))


    def enableSimpleDriving(self):
        '''
        Allow the robot to drive without encoders or any input from Config.
        '''

        self.speedLimit = 1
        self.maxSpeed = 1
        self.setUseEncoders(False)


    def _publishPID(self, table, profile):
        '''
        Read the PID value from the first active CAN Talon and publish it to the
        passed NetworkTable.
        '''

        table = NetworkTables.getTable('DriveTrain/%s' % table)

        talon = self.activeMotors[0]

        # TODO: If CTRE ever gives us back the ability to query PID values, send
        # them to NetworkTables here. In the meantime, we just persist the last
        # values that were set via NetworkTables

        def updatePID(table, key, value, isNew):
            '''
            Loops over all active motors and updates the appropriate setting. To
            avoid using a very long if structure inside the loop, we use getattr
            to access the methods of the motor by name.
            '''

            table.setPersistent(key)

            if key == 'RampRate':
                for motor in self.activePIDControllers:
                    motor.setClosedLoopRampRate(value, 0)

                return

            if key == 'P':
                for motor in self.activePIDControllers:
                    motor.setP(value, 1)

                return

            funcs = {
                'I': 'setI',
                'D': 'setD',
                'F': 'setFF',
                'IZone': 'setIZone'
            }

            for motor in self.activePIDControllers:
                getattr(motor, funcs[key])(value, 0)
                getattr(motor, funcs[key])(value, 1)

        table.addTableListener(updatePID, localNotify=True)


    def _configureMotors(self):
        '''
        Make any necessary changes to the motors and populate self.activeMotors.
        '''

        raise NotImplementedError()


    def _calculateSpeeds(self, x, y, rotate):
        '''Return a speed for each active motor.'''

        raise NotImplementedError()
