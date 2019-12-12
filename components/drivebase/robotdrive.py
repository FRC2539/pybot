import wpilib

from controller import logicalaxes

from components.drivebase.drivevelocities import TankDrive

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

class RobotDrive:

    motors = list

    activeMotors = list

    velocityCalculator = TankDrive # Establishes drive

    build = object # This is different from what is above. Fix if necessary.

    def prepareToDrive(self):
        print(str(self.motors))
        for motor in self.motors:
            motor.setNeutralMode(2)
            motor.setSafetyEnabled(False)
            motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)

        self.activeMotors = self.motors[0:2]

    def getSpeeds(self):
        # Temporary...probably
        return [self.motors[0].get(), self.motors[1].get(), self.motors[2].get(), self.motors[3].get()]

    def calculateTankSpeed(self, y, rotate, x=0):
        return [y + rotate, -y + rotate]

    def move(self):
        speeds = self.velocityCalculator.getSpeedT(
                                        y=self.build.getY(),
                                        rotate=self.build.getRotate()
                                        )
        for speed, motor in zip(speeds, self.activeMotors):
            motor.set(ControlMode.PercentOutput, speed)

    def execute(self):
        self.move()
