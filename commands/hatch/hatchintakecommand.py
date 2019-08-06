from wpilib.command.command import Command

import robot

class HatchIntakeCommand(Command):

    def __init__(self, override=False):
        super().__init__('Hatch Intake')

        self.requires(robot.hatch)

        self.override = True


    def initialize(self):
        robot.hatch.grab()
        robot.lights.solidGreen()
        self._isFinished = False


    def execute(self):
        if not self.override:
            self._isFinished = robot.hatch.hasHatchPanel()

        print(str(robot.hatch.hasHatchPanel()))


    def isFinished(self):
        return self._isFinished


    def end(self):
        robot.lights.off()
        robot.hatch.hasHatch = robot.hatch.hasHatchPanel()
        if robot.hatch.hasHatch:
            robot.hatch.hold()
        else:
            robot.hatch.stop()
