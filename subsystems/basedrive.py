from wpilib.command import Subsystem

from wpilib.kinematics import DifferentialDriveOdometry, DifferentialDriveWheelSpeeds
from wpilib.geometry import Rotation2d

from .cougarsystem import *

import math
import numpy # The 'fake' math lib lol. And yes, I don't import as 'np'
#import sympy

from networktables import NetworkTables
from rev import CANSparkMax, ControlType, MotorType, IdleMode
from navx import AHRS

from custom.config import Config
import ports

from crapthatwillneverwork.simcansparkmax import SimCANSparkMax

class BaseDrive(CougarSystem):
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

        disablePrints()

        try:
            self.motors = [
                CANSparkMax(ports.drivetrain.frontLeftMotorID, MotorType.kBrushless),
                CANSparkMax(ports.drivetrain.frontRightMotorID, MotorType.kBrushless),
                CANSparkMax(ports.drivetrain.backLeftMotorID, MotorType.kBrushless),
                CANSparkMax(ports.drivetrain.backRightMotorID, MotorType.kBrushless)
            ]

        except AttributeError:
            self.motors = [
                CANSparkMax(ports.drivetrain.leftMotorID, MotorType.kBrushless),
                CANSparkMax(ports.drivetrain.rightMotorID, MotorType.kBrushless)
            ]

        for motor in self.motors:
            motor.setIdleMode(IdleMode.kBrake)

        '''
        Subclasses should configure motors correctly and populate activeMotors.
        '''
        self.activeMotors = []
        self._configureMotors()

        self.drivetrainWidth = 23.75
        self.trajectoryDerivative = None
        self.trajectoryLength = None
        self.finalX = None

        '''Initialize the navX MXP'''
        self.navX = AHRS.create_spi()
        self.resetGyro()
        self.zeroDisplacement()
        self.flatAngle = 0

        '''A record of the last arguments to move()'''
        self.lastInputs = None

        self.setUseEncoders(True)
        self.maxSpeed = 5500#Config('DriveTrain/maxSpeed') # 2500
        self.speedLimit = 5500#Config('DriveTrain/normalSpeed') # 4500
        self.deadband = 0.04 # Deadband of 2%
        self.maxPercentVBus = 1

        '''Allow changing CAN Talon settings from dashboard'''
        self._publishPID('Speed', 0)
        self._publishPID('Position', 1)

        self.resetEncoders()
        self.resetPID()

        self.odometry = DifferentialDriveOdometry(Rotation2d.fromDegrees(self.getHeadingWithLimit()))

    def initDefaultCommand(self):
        '''
        By default, unless another command is running that requires this
        subsystem, we will drive via joystick using the max speed stored in
        Config.
        '''
        from commands.drivetrain.drivecommand import DriveCommand

        self.setDefaultCommand(DriveCommand(self.speedLimit))

    def updateOdometry(self):
        distance = self.getDistance()
        self.odometry.update(Rotation2d.fromDegrees(self.getHeadingWithLimit()), distance[0], distance[1])

    def getDistance(self):
        return [(x / 10.71) * 0.47879 for x in self.getPositions()] # The weird float is the circumference of the wheel in meters.

    def getWheelSpeeds(self): # Returns meters per second
        mps = [((x / 60) / 10.71) * 0.47879 for x in self.getSpeeds()]
        return DifferentialDriveWheelSpeeds(mps[0], mps[1])

    def getPose(self):
        return self.odometry.getPoseMeters()

    def setVolts(self, leftPower, rightPower):
        self.activeMotors[0].setVoltage(leftPower)
        self.activeMotors[1].setVoltage(rightPower)


    def move(self, x, y, rotate):
        '''Turns coordinate arguments into motor outputs.'''

        '''
        Short-circuits the rather expensive movement calculations if the
        coordinates have not changed.
        '''

        if [x, y, rotate] == self.lastInputs or [x, y, rotate] == [0, 0, 0]:
            return

        self.lastInputs = [x, y, rotate]

        '''Prevent drift caused by small input values'''
        if self.useEncoders:
            x = math.copysign(max(abs(x) - self.deadband, 0), x)
            y = math.copysign(max(abs(y) - self.deadband, 0), y)
            rotate = math.copysign(max(abs(rotate) - self.deadband, 0), rotate)

        speeds = self._calculateSpeeds(x, y, rotate)

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


            for controller, speed in zip(self.activePIDControllers, speeds):
                print('running ')
                controller.setReference(speed * self.speedLimit, ControlType.kVelocity, 0, 0) # 'Speed' is a percent.
                #controller.set(speed)
        else:
            for motor, speed in zip(self.activeMotors, speeds):
                motor.set(speed * self.maxPercentVBus)


    def setPositions(self, positions):
        '''
        Have the motors move to the given positions. There should be one
        position per active motor. Extra positions will be ignored.
        '''

        if not self.useEncoders:
            raise RuntimeError('Cannot set position. Encoders are disabled.')

        self.stop()
        for motor, position in zip(self.activeMotors, positions):
            motor.getPIDController().setReference(position, ControlType.kPosition, 0, 0)


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

    def resetEncoders(self):
        for motor in self.motors:
            motor.getEncoder().setPosition(0.0)

    def stop(self):
        '''Disable all motors until set() is called again.'''
        for motor in self.activeMotors:
            motor.stopMotor()

        self.lastInputs = None


    def resetPID(self):
        '''Set all PID values to 0 for profiles 0 and 1.'''
        for motor in self.activeMotors:
            motor.setClosedLoopRampRate(0.25)
            controller = motor.getPIDController()
            for profile in range(2):
                controller.setP(0.0000007, profile) # 0.000007 TODO: Test this new value. We want 
                controller.setI(0, profile) # 0
                controller.setD(0.0001, profile) # 0.0001
                controller.setFF(0.0002, profile) # 0.0005
                controller.setIZone(0, profile) # 0


    def generatePolynomial(self, xOne, yOne, xTwo, yTwo, yPrimeOne, yPrimeTwo, special):
        '''
        Use matrices and points to solve for the constants of our custom cubic polynomial (ax^3 + bx^2 + cx + d).

        Screw me.

        [x1^3  x1^2 x1 1]
        [x2^3  x2^2 x2 1]
        [3x1^2 2x1  1  0]
        [3x2^2 2x2  1  0]

        '''

        if not special:

            matrixOne = numpy.array(
                [[           0,         0,    0, 1],
                [    xTwo ** 3, xTwo ** 2, xTwo, 1],
                [            0,         0,    1, 0],
                [3 * xTwo ** 2,  2 * xTwo,    1, 0]]
                )

        else:

            matrixOne = numpy.array(
                [[xOne ** 3, xOne ** 2, xOne, 1],
                [xTwo ** 3, xTwo ** 2, xTwo, 1],
                [3 * xOne ** 2, 2 * xOne, 1, 0],
                [3 * xTwo ** 2, 2 * xTwo, 1, 0]]
                )


        matrixTwo = numpy.array(
            [[yOne],
            [yTwo],
            [yPrimeOne],
            [yPrimeTwo]]
            )

        solutionMatrix = list(numpy.linalg.inv(matrixOne).dot(matrixTwo))

        return float(solutionMatrix[0]), float(solutionMatrix[1]), float(solutionMatrix[2]), float(solutionMatrix[3]) # a, b, c, d

    def getEquation(self, a, b, c, d):
        return str(a) + ' * x ** 3 + ' + str(b) + ' * x ** 2 + ' + str(c) + ' * x + ' + str(d)

    def calcArcLength(self, lowerLimit, upperLimit, equation):
        x = 2#sympy.Symbol('x')
        y = eval(equation)

        derivative = y.diff(x) # Gets the derivative. Tested, should work.

        return 0,0#sympy.integrate(sympy.sqrt((derivative ** 2) + 1), (x, lowerLimit, upperLimit)), derivative # Kwakulus made easy! (Not really.)

    def assignDerivative(self, der):
        self.trajectoryDerivative = str(der)

    def assignArcLength(self, length):
        self.trajectoryLength = length

    def assignFinalX(self, x):
        self.finalX = x

    def getHeadingDifference(self):
        X = (self.getFeetTravelled() / self.trajectoryLength) * self.finalX
        y = float(eval(self.trajectoryDerivative.replace('x', str(X)))) # Took the derivative, so this is the slope.

        desiredAngle = numpy.copysign(90 - numpy.degrees(numpy.arctan(abs(y))), y) # AS OF NOW IT ONLY

        return desiredAngle - self.getAngle()

    def calcSideDistances(self, radius, angle):
        radians = math.radians(angle)

        insideLength = radians * radius
        outsideLength = radians * (radius + self.drivetrainWidth)

        return insideLength, outsideLength

    def angleControlDrive(self, angleDiff):
        adjustment = angleDiff * 0.006

        if adjustment > 0:
            self.activeMotors[0].set(0.5 + adjustment)
            self.activeMotors[1].set(0.5)

        else:
            self.activeMotors[0].set(0.5)
            self.activeMotors[1].set(0.5 + adjustment)

    def getFeetTravelled(self):
        pos = self.getPositions()
        averagePos = (pos[0] + math.copysign(pos[1], pos[0])) / 2
        return self.rotationsToInches(averagePos) / 12

    def zeroDisplacement(self):
        self.navX.resetDisplacement()

    def getHeadingWithLimit(self):
        angle = self.getAngle()
        if angle > 180:
            angle = 180 - angle

        return angle

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
        '''Converts a distance in inches into a number of encoder ticks.'''
        rotations = distance / 18.25#(math.pi * Config('DriveTrain/wheelDiameter'))

        return float(rotations * 10.71)

    def rotationsToInches(self, rotations):
        return (rotations / 10.71) * 18.25

    def resetTilt(self):
        self.flatAngle = self.navX.getPitch()


    def getTilt(self):
        return self.navX.getPitch() - self.flatAngle


    def getAcceleration(self):
        '''Reads acceleration from NavX MXP.'''
        return self.navX.getWorldLinearAccelY()


    def getSpeeds(self):
        '''Returns the speed of each active motors.'''
        return [x.getVelocity() for x in self.activeEncoders]


    def getPositions(self):
        '''Returns the position of each active motor.'''
        return [x.getEncoder().getPosition() for x in self.activeMotors]


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


    def _configureMotors(self):
        '''
        Make any necessary changes to the motors and populate self.activeMotors.
        '''

        raise NotImplementedError()


    def _calculateSpeeds(self, x, y, rotate):
        '''Return a speed for each active motor.'''

        raise NotImplementedError()
