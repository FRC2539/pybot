import wpilib
import math

from controller import logicalaxes

from components.drivebase.drivevelocities import TankDrive

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

class RobotDrive:

    robotdrive_motors: list

    activeMotors: list

    velocityCalculator: object # Establishes drive

    build: object # This is different from what is above. Fix if necessary.

    useActives: list

    def __init__(self):     # NOTE: Be careful with this new init, as I added it after running it on a robot. It passes tests though, so we should be "gucci"
        self.rumble = False

    def prepareToDrive(self):
        print(str(self.velocityCalculator))
        for motor in self.robotdrive_motors:
            motor.setNeutralMode(2)
            motor.setSafetyEnabled(False)
            motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)

            # Configures mm stuff.
            motor.configMotionAcceleration(300) # Dummy value
            motor.configMotionCruiseVelocity(500) # Dummy value

        self.resetPID()

        self.rumble = False

        self.useActives = self.velocityCalculator.configureFourTank(self.robotdrive_motors)

    def getSpeeds(self):
        # Temporary...probably
        return [self.useActives[0].get(),
                self.useActives[1].get(),
                self.useActives[2].get(),
                self.useActives[3].get()
                ]

    def calculateTankSpeed(self, y, rotate, x=0):
        return [y + rotate, -y + rotate]

    def stop(self):
        for motor in self.useActives:
            motor.stopMotor()

    def move(self):
        y = self.build.getY() * -1
        if abs(y) < 0.01:
            y = 0.0 # added for stupid sensitivity issue.
        speeds = self.velocityCalculator.getSpeedT(
                                        y=float(y),
                                        rotate=float(self.build.getRotate())
                                            )
        if abs(speeds[0]) == 1.0 and abs(speeds[1]) == 1.0: # Probably only temporary, as this will slow the process down.
            self.build.setDualRumble()
            self.rumble = True
        elif (abs(speeds[0]) < 0.95 or abs(speeds[1]) < 0.95) and self.rumble: # Runs if they're less than almost full and if rumble is engaged.
            self.build.disableRumble()
            self.rumble = False

        for speed, motor in zip(speeds, self.useActives):
            motor.set(ControlMode.PercentOutput, speed)
    def getPosition(self):
        positions = []
        for motor in self.useActives:
            positions.append(motor.getSelectedSensorPosition())

        return positions

    def setPositions(self, positions):
        for motor, position in zip(self.useActives, positions):
            motor.set(ControlMode.MotionMagic, position) # motion magic works because of config above.

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

    def resetPID(self):
        for motor in self.useActives:
            motor.configClosedLoopRamp(0, 0)
            for profile in range(2):
                motor.config_kP(profile, 1, 0)
                motor.config_kI(profile, 0.001, 0)
                motor.config_kD(profile, 31, 0)
                motor.config_kF(profile, 0.7, 0)
                motor.config_IntegralZone(profile, 30, 0)

    def execute(self):
        # Functions as a default for a low level (kinda)
        self.move()
