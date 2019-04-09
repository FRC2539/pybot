from wpilib.command.command import Command

import robot

class HatchIntakeCommand(Command):

    def __init__(self):
        super().__init__('Hatch Intake')

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.intake()
        self._isFinished = False

    def execute(self):
        if robot.intake.hasHatchPanel():
            self._isFinished = True

    def isFinished(self):
        return self._isFinished

    def end(self):
        robot.intake.stop()
