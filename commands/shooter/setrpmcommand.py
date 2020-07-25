from wpilib.command import Command

import robot

class SetRPMCommand(Command):

    def __init__(self, rpm):
        super().__init__('Set RPM')

        self.requires(robot.shooter)
        self.rpm = rpm

    def initialize(self):
        robot.shooter.setRPM(self.rpm)

    def end(self):
        robot.shooter.stopShooter()
