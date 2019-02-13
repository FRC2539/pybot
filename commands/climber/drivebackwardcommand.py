from wpilib.command.command import Command

import robot

class DriveBackwardCommand(Command):

    def __init__(self):
        super().__init__('Drive Backward')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.driveBackward()


    def execute(self):
        pass


    def end(self):
        robot.climber.stopDrive()
