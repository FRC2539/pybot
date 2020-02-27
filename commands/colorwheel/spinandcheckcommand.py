from wpilib.command import Command

from wpilib import DriverStation

import robot


class SpinAndCheckCommand(Command):

    def __init__(self):
        super().__init__('Spin And Check')

        self.requires(robot.colorwheel)
        self.driverStation = DriverStation.getInstance()
        self.needExecute = True

    def initialize(self):
        self.startColor = robot.colorwheel.getColor() # Make sure this provides the correct value, not an assumption
        self.desiredColor = (self.driverStation.getGameSpecificMessage).lower() # Make this come from FMS later. NOTE: If not a string, simply use a dictionary instead.

        if self.startColor != self.desiredColor.lower():
            robot.colorwheel.spinClockwise()
            self.spinUntilThis = robot.colorwheel.setSearch(self.desiredColor)
        else:
            robot.colorwheel.alignWithSensor()
            self.needExecute = False

    def execute(self):
        if self.needExecute and robot.colorwheel.getColor() == self.desiredColor: # usually the first part, not included if already there
            robot.colorwheel.stop()
            robot.colorwheel.alignWithSensor(self.spinUntilThis) # runs this once it sees the color
            self.needExecute = False

        elif not self.needExecute and robot.colorwheel.getColor() == self.spinUntilThis: # second part; should always run
            robot.colorwheel.stop()

    def end(self):
        robot.colorwheel.stop()
        self.needExecute = True
