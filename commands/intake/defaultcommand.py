from wpilib.command.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for intake')

        self.requires(robot.intake)

        self.hadBall = None
        self.hasBall = None


    def initialize(self):
        self.hasBall = robot.intake.hasCargo

        if self.hasBall:
            robot.intake.hold()
        else:
            robot.intake.stop()
