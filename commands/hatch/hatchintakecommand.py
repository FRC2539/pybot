from wpilib.command.command import Command

import robot

class HatchIntakeCommand(Command):

    def __init__(self):
        super().__init__('Hatch Intake')

        self.requires(robot.hatch)


    def initialize(self):
        print('grab')
        robot.hatch.grab()
        self._isFinished = False


    def execute(self):
        self._isFinished = robot.hatch.hasHatchPanel()


    def isFinished(self):
        return self._isFinished


    def end(self):
        robot.hatch.hasHatch = True
        robot.hatch.stop()
