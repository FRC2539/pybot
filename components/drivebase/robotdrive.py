import wpilib

from controller import logicalaxes
from controller.buildlayout import BuildLayout

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

class RobotDrive:

    motors = [
              WPI_TalonSRX,
              WPI_TalonSRX,
              WPI_TalonSRX,
              WPI_TalonSRX
              ]

    activeMotors = motors[0:2]

    def __init__(self):
        self.enabled = True

    def prepareToDrive(self):
        for motor in self.motors:
            motor.setNeutralMode(NeutralMode.Brake)
            motor.setSafetyEnabled(False)
            motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)

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
        print(str(self.activeMotors))
        for speed, motor in zip(speeds, self.activeMotors):
            motor.set(2, 0.5)

    def execute(self):
        self.move()
