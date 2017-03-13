from wpilib.command.command import Command

import subsystems

class RunIntoWallCommand(Command):
    '''Drives the robot at a steady speed until it crashes into something.'''

    def __init__(self, speed):
        super().__init__('Run Into Wall')

        self.requires(subsystems.drivetrain)
        self.speed = speed


    def initialize(self):
        subsystems.drivetrain.move(0, self.speed, 0)


    def isFinished(self):
        return abs(subsystems.drivetrain.getAcceleration()) > 0.5


    def end(self):
        subsystems.drivetrain.stop()
