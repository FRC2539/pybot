from wpilib.command.command import Command
from custom.config import Config

from networktables import NetworkTables as nt
from controller.logicalaxes import registerAxis
from commands.drivetrain.drivecommand import DriveCommand

import robot

class BoostCommand(Command):

    def __init__(self):
        super().__init__('Toggle Speed')

        self.requires(robot.drivetrain)
        self.nt = nt.getTable('DriveTrain')


    #def initialize(self):
        #robot.drivetrain.toggleBoost()

    #def execute(self):
        #robot.drivetrain.toggleBoost()
        #self._finished = True

    #def end(self):
        #robot.drivetrain.toggleBoost()
        #DriveCommand(robot.drivetrain.speedLimit)
        #registerAxis('driveX')
        #registerAxis('driveY')
        #registerAxis('driveRotate')
