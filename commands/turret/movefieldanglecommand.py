from wpilib.command import Command

import robot

from controller import logicalaxes

logicalaxes.registerAxis('turretX')

class MoveFieldAngleCommand(Command):

    def __init__(self, val):
        super().__init__('Move Field Angle')


        self.rotate = val


    def initialize(self):
        pass


    def execute(self):
        robot.turret.moveFieldAngle(self.rotate)
        #robot.turret.moveFieldAngle(logicalaxes.turretX.get() * 20)


    def end(self):
        pass
