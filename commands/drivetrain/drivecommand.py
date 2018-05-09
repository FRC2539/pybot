from wpilib.command import Command

import subsystems
from controller import logicalaxes
from custom.config import Config
import math

logicalaxes.registerAxis('driveX')
logicalaxes.registerAxis('driveY')
logicalaxes.registerAxis('driveRotate')

class DriveCommand(Command):
    def __init__(self, speedLimit):
        super().__init__('DriveCommand %s' % speedLimit)

        self.requires(subsystems.drivetrain)
        self.speedLimit = speedLimit

        self.preciseSpeed = Config('DriveTrain/preciseSpeed')
        if self.speedLimit < self.preciseSpeed:
            self.preciseSpeed = self.speedLimit



    def initialize(self):
        subsystems.drivetrain.stop()
        subsystems.drivetrain.setProfile(0)
        try:
            subsystems.drivetrain.setSpeedLimit(self.speedLimit)
        except (ZeroDivisionError, TypeError):
            print('Could not set speed to %f' % self.speedLimit)
            subsystems.drivetrain.setUseEncoders(False)

        self.lastY = None
        self.slowed = False


    def execute(self):
        # Avoid quick changes in direction
        y = logicalaxes.driveY.get()
        if self.lastY is None:
            self.lastY = y
        else:
            cooldown = 0.05
            self.lastY -= math.copysign(cooldown, self.lastY)

            # If the sign has changed, don't move
            if self.lastY * y < 0:
                y = 0

            if abs(y) > abs(self.lastY):
                self.lastY = y

        tilt = subsystems.drivetrain.getTilt()
        correction = tilt / 20
        if abs(correction) < 0.2:
            correction = 0

        subsystems.drivetrain.move(
            logicalaxes.driveX.get(),
            y - correction,
            logicalaxes.driveRotate.get()
        )
