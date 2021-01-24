from wpilib.command import InstantCommand

import robot


class ZeroCANCodersCommand(InstantCommand):
    def __init__(self, CANCoderVals: list = [-71.0, 0.0, 0.0, 0.0]):
        super().__init__("Zero CANCoders")

        # Doesn't work. Maybe it can't use it while its being used?

        self.positions = CANCoderVals

    def initialize(self):
        robot.drivetrain.updateCANCoders(self.positions)
        robot.drivetrain.updateModuleAngles()
        print("Zeroed CANCoders!")
