from wpilib.command import InstantCommand

import robot


class ZeroCANCodersCommand(InstantCommand):
    def __init__(self):
        super().__init__("Zero CANCoders")

        """
        Used to zero the CANCoders. Ensure all wheels are straight, then 
        call this command. 
        """

        self.requires(robot.drivetrain)

    def initialize(self):
        offsets = [-angle for angle in robot.drivetrain.getModuleAngles()]

        robot.drivetrain.updateCANCoders(offsets)
