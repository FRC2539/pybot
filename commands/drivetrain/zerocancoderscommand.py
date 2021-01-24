from wpilib.command import InstantCommand

import robot


class ZeroCANCodersCommand(InstantCommand):
    def __init__(self, CANCoderVals: list = [0.0, 0.0, 0.0, 0.0]):
        super().__init__("Zero CANCoders")

        self.positions = CANCoderVals

    def initialize(self):
        robot.drivetrain.updateCANCoders(self.positions)
        print("Zeroed CANCoders!")
