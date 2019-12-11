import wpilib

from controller import logicalaxes
from controller.buildlayout import BuildLayout

from components.drivebase.drivevelocities import TankDrive

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

class RobotDrive:

    motors = list

    activeMotors = list

    velocityCalculator = TankDrive # Establishes drive

    def prepareToDrive(self):
        print(str(self.motors))
        for motor in self.motors:
            motor.setNeutralMode(2)
            motor.setSafetyEnabled(False)
            motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)

        self.activeMotors = self.motors[0:2]

        self.declareJoysticks()

    def calculateTankSpeed(self, y, rotate, x=0):
        return [y + rotate, -y + rotate]

    def declareJoysticks(self):
        self.build = BuildLayout(0)

        logicalaxes.registerAxis('driveX')
        logicalaxes.registerAxis('driveY')
        logicalaxes.registerAxis('driveRotate')

    def move(self):
        speeds = self.velocityCalculator.getSpeedT(
                                        y=logicalaxes.driveY.get(),
                                        rotate=logicalaxes.driveRotate.get()
                                        )
        for speed, motor in zip(speeds, self.activeMotors):
            motor.set(ControlMode.PercentOutput, speed)

    def execute(self):
        self.move()
