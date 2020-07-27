from wpilib.command import Command

import robot

class ExtendLauncherCommand(Command):

    def __init__(self):
        super().__init__('Extend Launcher')

    def initialize(self):
        robot.pneumatics.extendBallLauncherSolenoid()

    def end(self):
        robot.pneumatics.retractBallLauncherSolenoid()
