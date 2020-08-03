from wpilib.command import Command

import robot

class SetRPMCommand(Command):

    def __init__(self, rpm):
        super().__init__('Set RPM')

        self.requires(robot.shooter)
        self.rpm = rpm

    def initialize(self):
        print('begunb')
        robot.shooter.pseudoSet()

    def end(self):
        print('done')
        robot.shooter.pseudoStop()
