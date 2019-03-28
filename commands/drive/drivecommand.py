from wpilib.command import Command

import subsystems
import robot
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

    def execute(self):
        x = logicalaxes.driveX.get()
        if abs(x) < 0.02:
            x = 0
        y = logicalaxes.driveY.get()
        if abs(y) < 0.02:
            y = 0.0
        rotate = logicalaxes.driveRotate.get()

        subsystems.drivetrain.move(
            x,
            y,
            rotate
        )
