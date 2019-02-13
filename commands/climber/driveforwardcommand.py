from wpilib.command.command import Command

import robot

class DriveForwardCommand(Command):

    def __init__(self):
        super().__init__('Drive Forward')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.driveForward()


    def execute(self):
        pass


    def end(self):
        robot.climber.stopDrive()
