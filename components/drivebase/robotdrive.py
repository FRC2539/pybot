import wpilib

from controller import logicalaxes
from controller.buildlayout import BuildLayout

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

class RobotDrive:

    motors = list

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
        speeds = self.calculateTankSpeed(
                                        y=logicalaxes.driveY.get(),
                                        rotate=logicalaxes.driveRotate.get()
                                        )

        print(str(speeds))
        for speed, motor in zip(speeds, self.motors):
            motor.set(0, float(0.5))

    def execute(self):
        self.move()
