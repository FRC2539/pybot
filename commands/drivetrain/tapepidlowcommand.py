from wpilib.command.command import Command
from custom.config import Config
import math
import robot

from networktables import NetworkTables

class TapePIDLowCommand(Command):

    def __init__(self):
        super().__init__('Tape P I D Low')

        self.requires(robot.drivetrain)

        self.tape = Config('limelight/tv', 0)
        self.targetX = Config('limelight/tx', 0)
        self.targetY = Config('limelight/ty', 0)

        self.nt = NetworkTables.getTable('limelight')




    def initialize(self):
        self.nt.putNumber('pipeline', 1)
        self._finished = False


    def execute(self):
        if self.tape.getValue() == 1:
            oY = self.targetX.getValue()
            oX = self.targetY.getValue()
            h = 39.5 - 28.5

            theta = math.radians(73 + oY)

            oD = h * math.tan(theta) - 36

            return (oD, oX)

        else:
            print('no tape yet')


    def end(self):
        self.nt.putNumber('pipeline', 0)
        robot.lights.off()
