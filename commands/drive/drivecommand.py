from wpilib.command import Command

import subsystems
from controller import logicalaxes

logicalaxes.registerAxis('driveX')
logicalaxes.registerAxis('driveY')
logicalaxes.registerAxis('driveRotate')

class DriveCommand(Command):
    def __init__(self, speedLimit):
        super().__init__('DriveCommand %s' % speedLimit)

        self.requires(subsystems.drivetrain)
        self.speedLimit = speedLimit


    def initialize(self):
        subsystems.drivetrain.setSpeedLimit(self.speedLimit)
        subsystems.drivetrain.setUseEncoders(False)


    def execute(self):
        x = logicalaxes.driveX.get()
        y = logicalaxes.driveY.get()
        rotate = logicalaxes.driveRotate.get()
        if x > .05:
            x = .25 + .75 * x
        if y > .05:
            y = .25 + .75 * y
        if rotate > .05:
            rotate = .25 +.65 * rotate
        subsystems.drivetrain.move(
            x,
            y,
            rotate
        )


    def end(self):
        subsystems.drivetrain.setUseEncoders()
