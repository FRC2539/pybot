import wpilib

from controller import logicalaxes

from components.drivebase.drivevelocities import TankDrive

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

class RobotDrive:

    robotdrive_motors = list

    activeMotors = list

    velocityCalculator = object # Establishes drive

    build = object # This is different from what is above. Fix if necessary.

    useActives = list

    def prepareToDrive(self):
        print(str(self.velocityCalculator))
        for motor in self.robotdrive_motors:
            motor.setNeutralMode(2)
            motor.setSafetyEnabled(False)
            motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)

        self.activeMotors = self.robotdrive_motors[0:2]

        self.useActives = self.velocityCalculator.configureFourTank(self.robotdrive_motors)

    def getSpeeds(self):
        # Temporary...probably
        return [self.robotdrive_motors[0].get(),
                self.robotdrive_motors[1].get(),
                self.robotdrive_motors[2].get(),
                self.robotdrive_motors[3].get()
                ]

    def calculateTankSpeed(self, y, rotate, x=0):
        return [y + rotate, -y + rotate]

    def move(self):
        y = self.build.getY() * -1
        if abs(y) < 0.01:
            y = 0.0 # added for stupid sensitivity issue.
        speeds = self.velocityCalculator.getSpeedT(
                                        y=float(y),
                                        rotate=float(self.build.getRotate())
                                            )

        speeds.append(speeds[0])
        speeds.append(speeds[1]) # Temporary until I configure them correctly.

        for speed, motor in zip(speeds, self.robotdrive_motors):
            motor.set(ControlMode.PercentOutput, speed)

    def execute(self):
        # Functions as a default for a low level (kinda)
        self.move()
