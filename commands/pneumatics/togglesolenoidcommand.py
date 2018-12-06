from wpilib.command.instantcommand import InstantCommand
from wpilib.solenoid import Solenoid

import robot

class toggleSolenoidCommand(InstantCommand):

    def __init__(self):
        super().__init__('toggle Solenoid')

        self.requires(robot.pneumatics)


    def initialize(self):
        robot.pneumatics.toggle()
