from wpilib.command.command import Command

import robot

class HatchIntakeCommand(Command):

    def __init__(self):
        super().__init__('Hatch Intake')

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.hatchGrab()
        self._isFinished = False


    def execute(self):
        self._isFinished = False #robot.intake.hasHatchPanel()


    def isFinished(self):
        return self._isFinished


    def end(self):
        robot.intake.hasCargo = True
        robot.intake.stop()
