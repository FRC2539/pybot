from wpilib.command.command import Command

import robot

class IntakeCommand(Command):

    def __init__(self):
        super().__init__('Intake')

        self.requires(robot.intake)
        self._finished = False
        self.cargoCount = 0

    def initialize(self):
        robot.intake.intake()


    def execute(self):
        if self.cargoCount >= 3 and self.hasCargo():
            self.cargoCount = 0
            self._finished = True
        elif self.hasCargo():
            self.cargoCount += 1


    def isFinished(self):
        return self._finished


    def end(self):
        robot.intake.stop()


    def hasCargo(self):
        '''Replace this with light sensor code.'''
        return False
