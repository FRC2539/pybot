from wpilib.command.command import Command
import subsystems

class GoToWallCommand(Command):
    '''Drives the robot straight forward until it reaches a wall.'''

    def __init__(self):
        super().__init__('Drive To Wall')

        self.requires(subsystems.drivetrain)


    def initialize(self):
        subsystems.drivetrain.move(0, 1, 0)
        self._finished = False


    def execute(self):
        slow = (subsystems.drivetrain.getUltrasonic())

        if slow < 4.98:
            subsystems.drivetrain.move(0, max(slow / 4, 0), 0)

        self._finished = (slow < 3)


    def isFinished(self):
        # Stop if collision detected
        if subsystems.drivetrain.getUltrasonic() > 3:
            return True

        return self._finished


    def end(self):
        subsystems.basedrive.stop()
