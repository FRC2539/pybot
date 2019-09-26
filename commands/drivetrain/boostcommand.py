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
        self.requires(robot.lights)

    def initialize(self):
        driveMode = robot.drivetrain.toggleSpeed()
        if not driveMode:
            robot.lights.chase()
        else:
            robot.lights.solidOrange()

    def end(self):
        pass
