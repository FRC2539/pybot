from wpilib.command.command import Command

import robot

class HatchIntakeCommand(Command):

    def __init__(self, override=False):
        super().__init__('Hatch Intake')

        self.requires(robot.hatch)

        self.override = override


    def initialize(self):
        print('grab')
        robot.hatch.grab()
        self._isFinished = False


    def execute(self):
        if not self.override:
            self._isFinished = robot.hatch.hasHatchPanel()


    def isFinished(self):
        return self._isFinished


    def end(self):
        robot.hatch.hasHatch = robot.hatch.hasHatchPanel()
        if robot.hatch.hasHatch:
            robot.hatch.hold()
        else:
            robot.hatch.stop()
