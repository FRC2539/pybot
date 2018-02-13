from wpilib.command import Command

import subsystems
from controller import logicalaxes
import math

logicalaxes.registerAxis('driveX')
logicalaxes.registerAxis('driveY')
logicalaxes.registerAxis('driveRotate')

class DriveCommand(Command):
    def __init__(self, speedLimit):
        super().__init__('DriveCommand %s' % speedLimit)

        self.requires(subsystems.drivetrain)
        self.speedLimit = speedLimit


    def initialize(self):
        subsystems.drivetrain.stop()
        subsystems.drivetrain.setProfile(0)
        #subsystems.drivetrain.setAcceleration(0.2)
        try:
            subsystems.drivetrain.setSpeedLimit(self.speedLimit)
        except (ZeroDivisionError, TypeError):
            print('Could not set speed to %f' % self.speedLimit)
            subsystems.drivetrain.setUseEncoders(False)


    def execute(self):
        tilt = subsystems.drivetrain.getTilt()
        correction = math.copysign(pow(tilt, 2), tilt) / 36
        if correction < 0.1:
            correction = 0

        subsystems.drivetrain.move(
            logicalaxes.driveX.get(),
            logicalaxes.driveY.get() - correction,
            logicalaxes.driveRotate.get()
        )

    def end(self):
        subsystems.drivetrain.setAcceleration(0)
