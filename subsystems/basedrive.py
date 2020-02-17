from .debuggablesubsystem import DebuggableSubsystem

from wpilib import Timer

import math
import csv

from networktables import NetworkTables

from ctre import ControlMode, NeutralMode, WPI_TalonFX, TalonFXControlMode, TalonFXSensorCollection, TalonFXPIDSetConfiguration, TalonFXFeedbackDevice, Orchestra, FeedbackDevice
from rev import CANSparkMax, MotorType, ControlType

from navx import AHRS

from custom.config import Config
import ports


class BaseDrive(DebuggableSubsystem):
    '''
    A general case drive train system. It abstracts away shared functionality of
    the various drive types that we can employ. Anything that can be done
    without knowing what type of drive system we have should be implemented here.
    This code definitley doesn't play music.
    '''

    def setDriveTrain(self, compBot=True):
        if compBot:
            # WARNING: ALL PID's need to be finalized (even NEO's [taken from 9539 2019]).

            self.falconP = 0#Config('DriveTrain\FalconP', 0.03)
            self.falconI = 0#Config('DriveTrain\FalconI', 0.00001)
            self.falconD = 0#Config('DriveTrain\FalconD', 0)
            self.falconF = 100 #Config('DriveTrain\FalconF', 0.1)
            self.falconIZone = 0#Config('DriveTrain\FalconIZone', 0)

            #self.bensGloriousOrchestra = Orchestra()
            self.bensGloriousOrchestra = None

            try:
                self.motors = [
                    WPI_TalonFX(ports.drivetrain.frontLeftMotorID),
                    WPI_TalonFX(ports.drivetrain.frontRightMotorID),
                    WPI_TalonFX(ports.drivetrain.backLeftMotorID),
                    WPI_TalonFX(ports.drivetrain.backRightMotorID),
                ]

            except AttributeError:
                self.motors = [
                    WPI_TalonFX(ports.drivetrain.leftMotorID),
                    WPI_TalonFX(ports.drivetrain.rightMotorID),
                ]

            for motor in self.motors:
                motor.setNeutralMode(NeutralMode.Brake)
                motor.configSelectedFeedbackSensor(FeedbackDevice.IntegratedSensor, 0, 0)
                #self.bensGloriousOrchestra.addInstrument(motor)

            self.move = self.falconMove
            self.resetPID = self.falconResetPID
            self.setPositions = self.falconSetPositions
            self.setProfile = self.falconSetProfile
            self.stop = self.falconStop
            self.inchesToUnits = self.inchesToTicks
            self.getPositions = self.falconGetPositions
            self.averageError = self.falconAverageError
            self.neverPlayMusic = self.definitleyNotPlayMusic
            self.nopeNotPauseMusic = self.notPauseMusic
            self.noStopMusicHere = self.certainlyNotStopMusic
            self.resetEncoders = self.falconResetEncoders

        else:

            # For practice bot with NEO's

            print('in neos!!!\n\n\n')

            self.NEOencoders = []
            self.NEOcontrollers = []

            self.neoP = Config('DriveTrain\SparkP', 0.1)
            self.neoI = Config('DriveTrain\SparkI', 0)
            self.neoD = Config('DriveTrain\SparkD', 0.1)
            self.neoFF = Config('DriveTrain\SparkFF', 0)
            self.neoIZone = Config('DriveTrain\SparkIZone', 0)

            self.bensGloriousOrchestra = None # this makes me sad lol

            try:
                print('configured motors')
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
            self.resetPID = self.neoResetPID
            self.setPositions = self.neoSetPositions
            self.setProfile = self.neoSetProfile
            self.stop = self.neoStop
            self.inchesToUnits = self.inchesToRotations
            self.getPositions = self.neoGetPositions
            self.averageError = self.neoAverageError
            self.neverPlayMusic = self.null
            self.nopeNotPauseMusic = self.null
            self.noStopMusicHere = self.null
            self.resetEncoders = self.null

            print('set methods')

    def __init__(self, name):
        super().__init__(name)

        '''
        Create all motors, disable the watchdog, and turn off neutral braking
        since the PID loops will provide braking.
        '''

        '''
        Subclasses should configure motors correctly and populate activeMotors.

        '''

        self.compBot = True#Config('DriveTrain/Robot', True) # Commented to test for NEO temporarily.

        self.setDriveTrain(self.compBot)


        self.setupRecordData()

        self.activeMotors = []
        self._configureMotors(self.compBot)

        for motor in self.activeMotors:
            motor.configClosedloopRamp(0, 0)
            for profile in range(2):
                motor.config_kP(profile, self.falconP, 0)
                motor.config_kI(profile, self.falconI, 0)
                motor.config_kD(profile, self.falconD, 0)
                motor.config_kF(profile, self.falconF, 0)
                motor.config_IntegralZone(profile, self.falconIZone, 0)

        '''Initialize the navX MXP'''
        self.navX = AHRS.create_spi()
        self.resetGyro()
        self.flatAngle = 0

        '''A record of the last arguments to move()'''
        self.lastInputs = None
        #try:
            #self.folderSong = '/home/lvuser/py/subsystems'
            #print('loaded' + str(self.bensGloriousOrchestra.loadMusic(self.folderSong + '/' + 'song.chrp')))
        #except:
            #print('failed to load orchestra')


        self.setUseEncoders(True)
        self.maxSpeed = 2500#Config('DriveTrain/maxSpeed', 1)
        self.speedLimit = 2000#Config('DriveTrain/normalSpeed')
        self.deadband = Config('DriveTrain/deadband', 0.05)
        self.maxPercentVBus = 1 # used when encoders are not enabled in percent.

        '''Allow changing CAN Talon settings from dashboard'''
        self._publishPID('Speed', 0)
        self._publishPID('Position', 1)


        '''Add items that can be debugged in Test mode.'''
        self.debugSensor('navX', self.navX)

        self.debugMotor('Front Left Motor', self.motors[0])
        self.debugMotor('Front Right Motor', self.motors[1])

        self.resetPID()
        self.resetEncoders()

        self.setProfile(0)

        try:
            self.debugMotor('Back Left Motor', self.motors[2])
            self.debugMotor('Back Right Motor', self.motors[3])
        except IndexError:
            pass

    def setupRecordData(self):
        self.firstSave = True
        self.folder = '/home/lvuser/py/subsystems'

        self.timer = Timer()

        self.timer.start()

    def neoRecordDriveData(self):
        #for index, motor in enumerate(self.robotdrive_motors):
        #self.recordData[0].append(index)
        #self.recordData[1].append(motor.getEncoder().getVelocity())
        #self.recordData[2].append(motor.getOutputCurrent())
        #self.recordData[3].append(motor.getBusVoltage())
        #self.recordData[4].append(self.timer.get())
        #print(self.recordData)
        if self.firstSave:
            with open(self.folder +'/' + 'data.csv', 'w', newline='') as firstfile:
                print('first write')
                self.writer = csv.writer(firstfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_ALL, lineterminator='\n')
                for index, motor in enumerate(self.motors):
                    self.writer.writerow(['Motor: ' + str(index)] + ['RPM: ' + str((motor.getEncoder()).getVelocity())] + ['Amps: ' + str(motor.getOutputCurrent())] + ['Bus Volts: ' + str(motor.getBusVoltage())] + ['Time (s): ' + str(self.timer.get())])
                self.firstSave = False
        else:
            with open(self.folder +'/' + 'data.csv', 'a', newline='') as file:
                print('writing')
                self.writer = csv.writer(file, delimiter='\t', quotechar='|', quoting=csv.QUOTE_ALL, lineterminator='\n')

                for index, motor in enumerate(self.motors):
                    self.writer.writerow(['Motor: ' + str(index)] + ['RPM: ' + str((motor.getEncoder()).getVelocity())] + ['Amps: ' + str(motor.getOutputCurrent())] + ['Bus Volts: ' + str(motor.getBusVoltage())] + ['Time (s): ' + str(self.timer.get())])

            #for id_, vel, cur, volt, time in zip(self.recordData[0], self.recordData[1], self.recordData[2], self.recordData[3], self.recordData[4]):
            #self.writer.writerow(['Motor: ' + str(id_)] + ['RPM: ' + str(vel)] + ['Amps: ' + str(cur)] + ['Bus Volts: ' + str(volt)] + ['Time (s): ' + str(time)])



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
        if [x, y, rotate] == [0, 0, 0]:
            self.stop()
            return

        rotate *= 0.4
        y *= 0.5

        #print(str(x) + ' ' + str(y) + ' ' + str(rotate))

        self.lastInputs = [x, y, rotate]

        '''Prevent drift caused by small input values'''
        if self.useEncoders:
            x = math.copysign(max(abs(x) - self.deadband, 0), x)
            y = math.copysign(max(abs(y) - self.deadband, 0), y)
            rotate = math.copysign(max(abs(rotate) - self.deadband, 0), rotate)

        speeds = self._calculateSpeeds(x, y, rotate)

        #print('Speeds one: ' + str(speeds))
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
                    (motor.getPIDController()).setIAccum(0)

            #print("moving")
            #print(speeds)
            #print("boost: "+ str(self.boost))


            else:
                for motor, speed in zip(self.motors, speeds):
                    tmaxspeed = (self.maxSpeed / 100)
                    speed = (speed * 1)

                    if speed > 0.0 and speed > tmaxspeed:
                        speed = tmaxspeed

                    if speed < 0.0 and speed < (tmaxspeed * -1):
                       speed = (tmaxspeed * -1)


            for motor, speed in zip(self.activeMotors, speeds):
                motor.set(speed)
        else:
            for motor, speed in zip(self.activeMotors, speeds):
                motor.set(speed)

        if [x, y, rotate] == self.lastInputs:
            return
        if [x, y, rotate] == [0, 0, 0]:
            self.stop()
            return


        #self.neoRecordDriveData()


    def falconMove(self, x, y, rotate):
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

        print('two ' + str(speeds))

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
                print('vel ' + str((TalonFXSensorCollection(motor).getIntegratedSensorVelocity())))

                motor.set(TalonFXControlMode.PercentOutput, speed * self.maxPercentVBus) # make this velocity

        else:
            for motor, speed in zip(self.activeMotors, speeds):
                motor.set(ControlMode.PercentOutput, speed * self.maxPercentVBus)

        if [x, y, rotate] == self.lastInputs:
            return

        if [x, y, rotate] == [0, 0, 0]:
            self.stop()
            return


    def falconSetPositions(self, positions):
        '''
        Have the motors move to the given positions. There should be one
        position per active motor. Extra positions will be ignored.
        '''

        if not self.useEncoders:
            raise RuntimeError('Cannot set position. Encoders are disabled.')

        self.stop()
        for motor, position in zip(self.activeMotors, positions):
            #motor.selectProfileSlot(1, 0)
            #motor.configMotionCruiseVelocity(int(self.speedLimit), 0)
            #motor.configMotionAcceleration(int(self.speedLimit), 0)
            motor.set(ControlMode.Position, position)

    def neoSetPositions(self, positions):
        if not self.useEncoders:
            raise RuntimeError('Cannot set position. Encoders are disabled.')

        self.stop()
        for motor, position in zip(self.activeMotors, positions):
            #(motor.getPIDController()).setSmartMotionMaxVelocity(770.0, 0)
            #(motor.getPIDController()).setSmartMotionMaxAccel(80.0, 0)
            (motor.getPIDController()).setReference(position, ControlType.kPosition, 0, 0)


    def falconAverageError(self, positions=None):
        '''Find the average distance between setpoint and current position.'''
        error = 0
        for motor in self.activeMotors:
            error += abs(motor.getClosedLoopTarget(0) - motor.getSelectedSensorPosition(0))

        return error / len(self.activeMotors)

    def neoAverageError(self, positions):
        '''Find the average distance between setpoint and current position.'''
        error = 0
        for motor, pos in zip(self.activeMotors, positions):
            error += abs(pos - (motor.getEncoder()).getPosition())

        return error / len(self.activeMotors)

    def atPosition(self, positions, tolerance=10):
        '''
        Check setpoint error to see if it is below the given tolerance.
        '''
        return self.averageError(positions) <= tolerance

    def neoStop(self):
        '''Disable all motors until set() is called again.'''
        for motor in self.activeMotors:
            motor.stopMotor()

        self.lastInputs = None

    def falconStop(self):
        '''Disable all motors until set() is called again.'''
        for motor in self.activeMotors:
            motor.set(ControlMode.PercentOutput, 0.0)

        self.lastInputs = None

    def neoSetProfile(self, profile):
        pass # can't do this..


    def falconSetProfile(self, profile=0):
        '''Select which PID profile to use.'''
        for motor in self.activeMotors:
            motor.selectProfileSlot(profile, 0)

    def falconResetPID(self):
        '''Set all PID values to 0 for profiles 0 and 1.'''
        for motor in self.activeMotors:
            motor.configClosedloopRamp(0, 0)
            for profile in range(2):
                motor.config_kP(profile, self.falconP, 0)
                motor.config_kI(profile, self.falconI, 0)
                motor.config_kD(profile, self.falconD, 0)
                motor.config_kF(profile, self.falconF, 0)
                motor.config_IntegralZone(profile, self.falconIZone, 0)

            #motor.configMotionAcceleration(6000, 0)
            #motor.configMotionCruiseVelocity(15000, 0)
            #motor.configMotionSCurveStrength(5, 0)
            #motor.configPeakOutputForward(1, 0)
            #motor.configPeakOutputReverse(-1, 0)

            #motor.configNominalOutputForward(0, 0)
            #motor.configNominalOutputReverse(0, 0)

            #motor.configurePID(TalonFXPIDSetConfiguration(FeedbackDevice.IntegratedSensor), 0, 0)

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

    def inchesToRotations(self, distance):
        rotations = distance / (math.pi * 6)#Config('DriveTrain/wheelDiameter', 6))

        print('ROTATIONS : ' + str(rotations * 8.45))#Config('DriveTrain/ticksPerRotation', 8.45)))

        return float(rotations * 8.45)#Config('DriveTrain/GearRatio', 8.45))

    def inchesToTicks(self, distance):
        '''Converts a distance in inches into a number of encoder ticks.'''
        rotations = distance / (math.pi * 6)#Config('DriveTrain/wheelDiameter', 6))

        return int(rotations * 8.45) * 2048#Config('DriveTrain/ticksPerRotation', 4096))


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


    def falconGetPositions(self):
        '''Returns the position of each active motor.'''
        return [x.getSelectedSensorPosition(0) for x in self.activeMotors]

    def neoGetPositions(self):
        '''Returns the position of each active motor.'''
        return [(x.getEncoder()).getPosition() for x in self.activeMotors]


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

        table.addSubTableListener(updatePID, localNotify=True)

    def falconResetEncoders(self):
        for motor in self.activeMotors:
            motor.configSelectedFeedbackSensor(FeedbackDevice.IntegratedSensor, 0, 0)
            motor.setSelectedSensorPosition(0, 0, 0)

    def _configureMotors(self):
        '''
        Make any necessary changes to the motors and populate self.activeMotors.
        '''

        raise NotImplementedError()


    def _calculateSpeeds(self, x, y, rotate):
        '''Return a speed for each active motor.'''

        raise NotImplementedError()

    def definitleyNotPlayMusic(self):
        #self.bensGloriousOrchestra.play()
        print('PLAY MUSIC\n\n\n')

    def notPauseMusic(self):
        #self.bensGloriousOrchestra.pause()
        pass
    def certainlyNotStopMusic(self):
        #self.bensGloriousOrchestra.stop()
        pass
    def null(self):
        pass
