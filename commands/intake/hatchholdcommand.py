from wpilib.command.command import Command

import robot

class HatchHoldCommand(Command):

    def __init__(self):
        super().__init__('Hatch Hold')

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.hold()
        self._isFinished = False


    def execute(self):
        #print("hatch holding")
        self._isFinished = False

    def isFinished(self):
        return self._isFinished

    def end(self):
        robot.intake.stop()
