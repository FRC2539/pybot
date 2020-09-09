from wpilib.command import Command

import robot

class SetRPMCommand(Command):

    def __init__(self, rpm):
        super().__init__('Set RPM')

        self.requires(robot.shooter)
        self.rpm = rpm

    def initialize(self):
        robot.shooter.setPercent(0.8)
        
    def execute(self):
        print(robot.shooter.getRPM())

    def end(self):
        robot.shooter.stopShooter()
