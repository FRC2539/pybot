from .debuggablesubsystem import DebuggableSubsystem

import math

from networktables import NetworkTables

from ctre import ControlMode, NeutralMode, TalonFX, FeedbackDevice
from rev import CANSparkMax, MotorType, ControlType

from navx import AHRS

from custom.config import Config
import ports


class BaseDrive(DebuggableSubsystem):
    '''
    A general case drive train system. It abstracts away shared functionality of
    the various drive types that we can employ. Anything that can be done
    without knowing what type of drive system we have should be implemented here.
    '''

    def setDriveTrain(self, compBot):
        if compBot:
            # WARNING: ALL PID's need to be finalized (even NEO's [taken from 9539 2019]).

            self.falconP = Config('DriveTrain\FalconP', 0)
            self.falconI = Config('DriveTrain\FalconI', 0)
            self.falconD = Config('DriveTrain\FalconD', 0)
            self.falconF = Config('DriveTrain\FalconF', 0)
            self.falconIZone = Config('DriveTrain\FalconIZone', 0)

            try:
                self.motors = [
                    TalonFX(ports.drivetrain.frontLeftMotorID),
                    TalonFX(ports.drivetrain.frontRightMotorID),
                    TalonFX(ports.drivetrain.backLeftMotorID),
                    TalonFX(ports.drivetrain.backRightMotorID),
                ]

            except AttributeError:
                self.motors = [
                    TalonFX(ports.drivetrain.leftMotorID),
                    TalonFX(ports.drivetrain.rightMotorID),
                ]

            for motor in self.motors:
                motor.setNeutralMode(NeutralMode.Brake)
                motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)

            self.move = self.falconMove

        else:

            # For practice bot with NEO's

            self.NEOencoders = []
            self.NEOcontrollers = []

            self.neoP = Config('DriveTrain\SparkP', 0.05)
            self.neoI = Config('DriveTrain\SparkI', 0)
            self.neoD = Config('DriveTrain\SparkD', 0.1)
            self.neoFF = Config('DriveTrain\SparkFF', 0)
            self.neoIZone = Config('DriveTrain\SparkIZone', 0)

            try:
                self.motors = [
                    CANSparkMax(ports.drivetrain.frontLeftMotorID, MotorType.kBrushless),
                    CANSparkMax(ports.drivetrain.frontRightMotorID, MotorType.kBrushless),
                    CANSparkMax(ports.drivetrain.backLeftMotorID, MotorType.kBrushless),
                    CANSparkMax(ports.drivetrain.backRightMotorID, MotorType.kBrushless),
                ]

            except AttributeError:
                self.motors = [
                    CANSparkMax(ports.drivetrain.leftMotorID, MotorType.kBrushless),
                    CANSparkMax(ports.drivetrain.rightMotorID, MotorType.kBrushless),
                ]

            for motor in self.motors:
                self.NEOcontrollers.append(motor.getPIDController())
                self.NEOencoders.append(motor.getEncoder())

                motor._setEncPosition(0.0)
                motor.setIdleMode(CANSparkMax.IdleMode.kBrake)


            # Make general method names based off of methods that require controller-specific methods.

            self.move = self.neoMove


    def __init__(self, name):
        super().__init__(name)

        '''
        Create all motors, disable the watchdog, and turn off neutral braking
        since the PID loops will provide braking.
        '''

        '''
        Subclasses should configure motors correctly and populate activeMotors.

        '''

        self.compBot = False#Config('DriveTrain/Robot', True) # Commented to test for NEO temporarily.

        self.setDriveTrain(self.compBot)

        self.activeMotors = []
        self._configureMotors(self.compBot)

        '''Initialize the navX MXP'''
        self.navX = AHRS.create_spi()
        self.resetGyro()
        self.flatAngle = 0

        '''A record of the last arguments to move()'''
        self.lastInputs = None

        self.setUseEncoders()
        self.maxSpeed = Config('DriveTrain/maxSpeed')
        self.speedLimit = Config('DriveTrain/normalSpeed')
        self.deadband = Config('DriveTrain/deadband', 0.05)
        self.maxPercentVBus = 1

        '''Allow changing CAN Talon settings from dashboard'''
        self._publishPID('Speed', 0)
        self._publishPID('Position', 1)


        '''Add items that can be debugged in Test mode.'''
        self.debugSensor('navX', self.navX)

        self.debugMotor('Front Left Motor', self.motors[0])
        self.debugMotor('Front Right Motor', self.motors[1])

        try:
            self.debugMotor('Back Left Motor', self.motors[2])
            self.debugMotor('Back Right Motor', self.motors[3])
        except IndexError:
            pass


    def initDefaultCommand(self):
        '''
        By default, unless another command is running that requires this
        subsystem, we will drive via joystick using the max speed stored in
        Config.
        '''
        from commands.drivetrain.drivecommand import DriveCommand

        self.setDefaultCommand(DriveCommand(self.speedLimit))


    def neoMove(self, x, y, rotate):

        if [x, y, rotate] == self.lastInputs:
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
                for motor in self.activeMotors:
                    motor.setIAccum(0)

            for motor, speed in zip(self.activeMotors, speeds):
                motor.set(speed)

        else:
            for motor, speed in zip(self.activeMotors, speeds):
                motor.set(speed)


    def falconMove(self, x, y, rotate):
        '''Turns coordinate arguments into motor outputs.'''

        '''
        Short-circuits the rather expensive movement calculations if the
        coordinates have not changed.
        '''
        if [x, y, rotate] == self.lastInputs:
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
                for motor in self.activeMotors:
                    motor.setIntegralAccumulator(0, 0, 0)

            for motor, speed in zip(self.activeMotors, speeds):
                motor.set(ControlMode.Velocity, speed * self.speedLimit)

        else:
            for motor, speed in zip(self.activeMotors, speeds):
                motor.set(ControlMode.PercentOutput, speed * self.maxPercentVBus)


    def setPositions(self, positions):
        '''
        Have the motors move to the given positions. There should be one
        position per active motor. Extra positions will be ignored.
        '''

        if not self.useEncoders:
            raise RuntimeError('Cannot set position. Encoders are disabled.')

        self.stop()
        for motor, position in zip(self.activeMotors, positions):
            motor.selectProfileSlot(1, 0)
            motor.configMotionCruiseVelocity(int(self.speedLimit), 0)
            motor.configMotionAcceleration(int(self.speedLimit), 0)
            motor.set(ControlMode.MotionMagic, position)


    def averageError(self):
        '''Find the average distance between setpoint and current position.'''
        error = 0
        for motor in self.activeMotors:
            error += abs(motor.getClosedLoopTarget(0) - motor.getSelectedSensorPosition(0))

        return error / len(self.activeMotors)


    def atPosition(self, tolerance=10):
        '''
        Check setpoint error to see if it is below the given tolerance.
        '''
        return self.averageError() <= tolerance


    def stop(self):
        '''Disable all motors until set() is called again.'''
        for motor in self.activeMotors:
            motor.stopMotor()

        self.lastInputs = None


    def setProfile(self, profile):
        '''Select which PID profile to use.'''
        for motor in self.activeMotors:
            motor.selectProfileSlot(profile, 0)


    def falconResetPID(self):
        '''Set all PID values to 0 for profiles 0 and 1.'''
        for motor in self.activeMotors:
            motor.configClosedLoopRamp(0, 0)
            for profile in range(2):
                motor.config_kP(profile, 0, 0)
                motor.config_kI(profile, 0, 0)
                motor.config_kD(profile, 0, 0)
                motor.config_kF(profile, 0, 0)
                motor.config_IntegralZone(profile, 0, 0)

    def neoResetPID(self):
        '''Set all PID values to 0 for profiles 0 and 1.'''
        for motor in self.activeMotors:
            motor.setClosedLoopRampRate(0.15) # Adjust as needed
            controller = motor.getPIDController()

            for profile in range(2):
                controller.setP(self.neoP, profile)
                controller.setI(self.neoI, profile)
                controller.setD(self.neoD, profile)
                controller.setFF(self.neoFF, profile)
                controller.setIZone(self.neoIZone, profile)
                controller.setOutputRange(-1, 1, profile)

    def resetGyro(self):
        '''Force the navX to consider the current angle to be zero degrees.'''

        self.setGyroAngle(0)


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


    def inchesToTicks(self, distance):
        '''Converts a distance in inches into a number of encoder ticks.'''
        rotations = distance / (math.pi * Config('DriveTrain/wheelDiameter'))

        return int(rotations * Config('DriveTrain/ticksPerRotation', 4096))


    def resetTilt(self):
        self.flatAngle = self.navX.getPitch()


    def getTilt(self):
        return self.navX.getPitch() - self.flatAngle


    def getAcceleration(self):
        '''Reads acceleration from NavX MXP.'''
        return self.navX.getWorldLinearAccelY()


    def getSpeeds(self):
        '''Returns the speed of each active motors.'''
        return [x.getSelectedSensorVelocity(0) for x in self.activeMotors]


    def getPositions(self):
        '''Returns the position of each active motor.'''
        return [x.getSelectedSensorPosition(0) for x in self.activeMotors]


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


    def setSpeedLimit(self, speed):
        '''
        Updates the max speed of the drive and changes to the appropriate
        mode depending on if encoders are enabled.
        '''

        if speed <= 0:
            raise ValueError('DriveTrain speed must be greater than 0')

        self.speedLimit = speed
        if speed > self.maxSpeed:
            self.maxSpeed = speed

        '''If we can't use encoders, attempt to approximate that speed.'''
        self.maxPercentVBus = speed / self.maxSpeed


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
                for motor in self.activeMotors:
                    motor.configClosedLoopRamp(value, 0)

                return

            if key == 'P':
                for motor in self.activeMotors:
                    motor.config_kP(1, value, 0)

                return

            funcs = {
                'I': 'config_kI',
                'D': 'config_kD',
                'F': 'config_kF',
                'IZone': 'config_IntegralZone'
            }

            for motor in self.activeMotors:
                getattr(motor, funcs[key])(0, value, 0)
                getattr(motor, funcs[key])(1, value, 0)

        table.addTableListener(updatePID, localNotify=True)


    def _configureMotors(self):
        '''
        Make any necessary changes to the motors and populate self.activeMotors.
        '''

        raise NotImplementedError()


    def _calculateSpeeds(self, x, y, rotate):
        '''Return a speed for each active motor.'''

        raise NotImplementedError()
