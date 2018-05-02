from wpilib.command.command import Command
import robot

class GoToWallCommand(Command):
    '''Drives the robot straight forward until it reaches a wall.'''

    def __init__(self):
        super().__init__('Drive To Wall')

        self.requires(robot.drivetrain)


    def initialize(self):
        robot.drivetrain.setProfile(0)
        robot.drivetrain.move(0, 1, 0)
        self._finished = False


    def execute(self):
        slow = (robot.drivetrain.getFrontClearance() - 4) / 16.0

        if slow < 1:
            robot.drivetrain.move(0, max(slow, 0), 0)

        self._finished = (slow <= 0)


    def isFinished(self):
        # Stop if collision detected
        if abs(robot.drivetrain.getAcceleration()) > 1:
            return True

        return self._finished


    def end(self):
        robot.drivetrain.stop()
