from wpilib.command import Command

import robot

import math

class CamTranHoodLimelight(Command):

    def __init__(self):
        super().__init__('Cam Tran Hood Limelight')

        self.requires(robot.hood)

        self.hoodEncZeroPos = 24 # The angle of the hood if the limelight's pitch read zero in degrees. This means the pitch we receive is the angle offset.
        self.hoodZeroPos = 220 # Angle of the hood equal to the angle of the limelight.

        # 27 degrees is the 236 degrees max.

    def initialize(self):
        robot.hood.stopHood()

    def execute(self):
        self.goal = robot.hood.benSetAngle(robot.limelight.getY())

    def isFinished(self):
        return ((not robot.hood.withinBounds()) or (abs(self.goal - robot.hood.getPosition()) <= 3))

    def end(self):
        robot.hood.stopHood()
