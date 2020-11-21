from wpilib.command import Command

import robot

class SetRPMCommand(Command):

    def __init__(self, rpm, end=False):
        super().__init__('Set RPM')

        self.requires(robot.shooter)
        
        self.rpm = rpm
        self.end_ = end

    def initialize(self):
        robot.shooter.setRPM(self.rpm)
        
    def end(self):
        if self.end_:
            robot.shooter.stopShooter()
