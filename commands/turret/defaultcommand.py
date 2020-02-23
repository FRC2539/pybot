from wpilib.command import Command
from controller import logicalaxes

import robot

logicalaxes.registerAxis('operatorX')

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Turret')

        self.requires(robot.turret)

    def execute(self):
        robot.turret.move(logicalaxes.operatorX.get() * 0.8)
