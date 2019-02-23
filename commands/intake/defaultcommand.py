from wpilib.command.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for intake')

        self.requires(robot.intake)

        self.hadBall = None
        self.hasBall = None


    def initialize(self):
        self.hadBall = robot.intake.hasCargo()


    def execute(self):
        if self.hadBall:
            self.hasBall = robot.intake.hasCargo()
            if not self.hasBall:
                robot.intake.intake()
            else:
                robot.intake.stop()

        else:
            robot.intake.stop()


    def end(self):
        pass
