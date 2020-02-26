from wpilib.command import Command

import robot


class SpinAndCheckCommand(Command):

    def __init__(self):
        super().__init__('Spin And Check')

        self.requires(robot.colorwheel)
        self.driverStation = DriverStation.getInstance()


    def initialize(self):
        self.myColor = robot.colorwheel.getColor() # Make sure this provides the correct value, not an assumption
        self.desiredColor = (self.driverStation.getGameSpecificMessage).lower() # Make this come from FMS later. NOTE: If not a string, simply use a dictionary instead.
        print('needed ' + str(self.desiredColor))
        if robot.colorwheel.getColor() != self.desiredColor.lower():
            robot.colorwheel.spinClockwise()
        else:
            robot.colorwheel.spinToSensor()

    def execute(self):
        pass


    def end(self):
        pass
