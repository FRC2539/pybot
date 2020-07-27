from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for pneumatics')

        self.requires(robot.ledsystem)
        self.requires(robot.pneumatics)

    def execute(self):
        print('running')
        if robot.pneumatics.isPressureLow():
            robot.ledsystem.setRed()

        else:
            robot.ledsystem.rainbowLava() # All set!
