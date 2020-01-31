import wpilib
import math

import csv

from controller import logicalaxes

from components.drivebase.drivevelocities import TankDrive

from ctre import NeutralMode, FeedbackDevice, TalonFXControlMode
from rev import ControlType

class RobotDrive:

    robotdrive_motors: list

    velocityCalculator: object # Establishes drive

    build: object

    useActives: list

    rumble: bool

    def __init__(self):     # NOTE: Be careful with this new init, as I added it after running it on a robot. It passes tests though, so we should be "gucci". Also note that you cannot access VI stuff in __init__.
        self.assignFuncs(False)

        self.csvFile = 'data.csv'

    def assignFuncs(self, bot):

        # Assigns functions that are motor controller specific

        if bot:
            self.move = self.falconMove
            self.resetPID = self.falconResetPID
            self.getPositions = self.falconGetPosition
            self.setPositions = self.falconSetPositions

        else:
            self.move = self.neoMove
            self.resetPID = self.neoResetPID
            self.getPositions = self.neoGetPosition
            self.setPositions = self.neoSetPositions

    def prepareToDrive(self, bot):
        self.assignFuncs(bot)

        self.resetPID()

        self.lastInputs = None

        self.rumble = False

        self.build.setDualRumble() # TEMPORARY!!!

        self.useActives = self.velocityCalculator.configureFourTank(self.robotdrive_motors)

    def stop(self): # Compatible for both drivebases
        for motor in self.useActives:
            motor.stopMotor()

    def neoMove(self):
        with open(self.csvFile, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            y = self.build.getY() * -1 # invert the y-axis
            rotate = self.build.getRotate()


            if [y, rotate] == self.lastInputs: # I hope this doesn't stop the entire drive lol
                return

            speeds = self.velocityCalculator.getSpeedT(
                                            y=float(y),
                                            rotate=float(rotate)
                                                )

            for speed, motor in zip(speeds, self.useActives):
                motor.set(speed)
            for motor in self.robotdrive_motors:
                writer.writerow(['RPM: ' + str((motor.getEncoder()).getVelocity())] + ['Amps: ' + str(motor.getOutputCurrent())] + ['Volts?: ' + motor.getVoltageCompensationNominalVolatage()])

            self.lastInputs = [y, rotate]

    def falconMove(self):
        y = self.build.getY() * -1
        rotate = self.build.getRotate()

        if [y, rotate] == self.lastInputs: # I hope this doesn't stop the entire drive lol
            return

        speeds = self.velocityCalculator.getSpeedT(
                                        y=float(y),
                                        rotate=float(rotate)
                                            )

        for speed, motor in zip(speeds, self.useActives):
            motor.set(TalonFXControlMode.PercentOutput, speed)

        self.lastInputs = [y, rotate]

    def falconGetPosition(self):
        positions = []
        for motor in self.useActives:
            positions.append(motor.getSelectedSensorPosition())

        return positions

    def neoGetPosition(self):
        positions = []
        for motor in self.useActives:
            positions.append(motor.getEncoder().getPosition())

        return positions # Returns position in rotations TODO: Need to find unit that the talon and max share to ease calculations

    def falconSetPositions(self, positions):
        for motor, position in zip(self.useActives, positions):
            motor.set(TalonFXControlMode.MotionMagic, position) # motion magic works because of config above.

    def neoSetPositions(self, positions):
        for motor, position, in zip(self.useActives, positions):
            motor.getPIDController().setReference(position, ControlType.kPosition, 0, 0)

    def resetPosition(self):
        for motor in self.useActives:
            motor.setQuadraturePosition(0)

    def getAveragePosition(self, targets):
        error = 0
        for motor, target in zip(self.useActives, targets):
            error += abs(target - motor.getSelectedSensorPosition())

        return error

    def inchesToTicks(self, distance): #distance -> inches!
        # First does the wheel rotations necessary by dividing the distance by wheel the circumference. Takes this and multiplies by required ticks for one rotation (250)
        return (distance / (math.pi * 6)) * 250

    def falconResetPID(self): # Finalize both PID sets and set it up for nt values, separate for each bot
        for motor in self.useActives:
            motor.configClosedLoopRamp(0, 0)
            for profile in range(2):
                motor.config_kP(profile, 1, 0)
                motor.config_kI(profile, 0.001, 0)
                motor.config_kD(profile, 31, 0)
                motor.config_kF(profile, 0.7, 0)
                motor.config_IntegralZone(profile, 30, 0)

    def neoResetPID(self):
        for motor in self.useActives:
            motor.setClosedLoopRampRate(0.15)
            controller = motor.getPIDController()

            for profile in range(2):
                controller.setP(1, profile)
                controller.setI(0.001, profile)
                controller.setD(31, profile)
                controller.setFF(0.7, profile)
                controller.setIZone(30, profile)
                controller.setOutputRange(-1, 1, profile)

    def execute(self):
        # Functions as a default for a low level (kinda)
        self.move()

    def default(self):
        pass
