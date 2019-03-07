from wpilib.command.instantcommand import InstantCommand
from networktables import NetworkTables as Ben

import robot

class ToggleFieldOrientationCommand(InstantCommand):

    def __init__(self):
        super().__init__('Toggle Field Orientation')

        self.requires(robot.drivetrain)

        Ben.initialize(server="10.25.39.2")
        self.DriveTrain = Ben.getTable("DriveTrain")

        self.DriveTrain.putString('orientation', 'Field')

    def initialize(self):
        val = robot.drivetrain.toggleFieldOrientation()
        if not val:
            self.DriveTrain.putString('orientation', 'Robot')
        else:
            self.DriveTrain.putString('orientation', 'Field')
