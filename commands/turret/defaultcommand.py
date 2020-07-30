from wpilib.command import Command
from controller import logicalaxes

import robot

logicalaxes.registerAxis('operatorX')

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Turret')

        self.requires(robot.turret)

    def execute(self):
        robot.turret.testMove(logicalaxes.operatorX.get())
        # WARNING: DO NOT USE THIS COMMAND USE TURRET MOVE
