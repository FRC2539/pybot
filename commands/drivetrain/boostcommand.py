from wpilib.command.command import Command
from custom.config import Config

from networktables import NetworkTables as nt

import robot

class BoostCommand(Command):

    def __init__(self):
        super().__init__('Toggle Speed')

        self.requires(robot.drivetrain)
        self.nt = nt.getTable('DriveTrain')


    def initialize(self):
        robot.drivetrain.boost = True
        self.nt.putBoolean('boost', True)


    def end(self):
        robot.drivetrain.boost = False
        self.nt.putBoolean('boost', False)
