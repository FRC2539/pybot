from wpilib.command.command import Command

from custom.config import Config

from networktables import NetworkTables

import robot

class GetLLDistanceCommand(Command):

    def __init__(self):
        super().__init__('Get L L Distance')

        self.requires(robot.drivetrain)

        self.tapeLow = Config('limelight-low/tv', 0)
        self.yDiff = Config('limelight-low/ty', 1.5)

        self.ntLow = NetworkTables.getTable('limelight-low')

        self.drivePipeID = 0 # Make this your basic drive pipeline.

    def initialize(self):
        self.ntLow.putNumber('pipeline', 1)

        #h; high goal height - limelight height (difference in heights used in the trig)
        #yAngle; Gets theta in degrees (34 was already set, calculated values based off of know heights and distances, and then repurposed those values.

    def execute(self):
        if self.tapeLow.getValue() == 1:
            yAngle = self.yDiff.getValue() + 34
            h = 83

            distanceFromTarget = h / (math.tan(yAngle))
            print(str(distanceFromTarget))

    def end(self):
        self.ntLow.putNumber('pipeline', 0)
