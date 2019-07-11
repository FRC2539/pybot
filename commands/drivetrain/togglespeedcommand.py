from wpilib.command.command import Command
from custom.config import Config

from networktables import NetworkTables as nt

import robot

class ToggleSpeedCommand(Command):

    def __init__(self):
        super().__init__('Toggle Speed')

        self.requires(robot.drivetrain)
        nt.initialize(server='10.25.39.2')

        self.DriveTrain = nt.getTable('DriveTrain')
        self.boost = False


    def initialize(self):
        if not self.boost:
            self.DriveTrain.putBoolean('boost', True)
            self.boost = True

        else:
            self.DriveTrain.putBoolean('boost', False)
            self.boost = False


    def execute(self):
        self._finished = True


    def isFinished(self):
        return self._finished


    def end(self):
        robot.drivetrain.stop()
