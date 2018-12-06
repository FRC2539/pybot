from wpilib.command.command import Command

import robot

class HoldSolenoidCommand(Command):

    def __init__(self):
        super().__init__('Hold Solenoid')

        self.requires(robot.pneumatics)

    def initialize(self):
        robot.pneumatics.hold()
