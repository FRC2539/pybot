from wpilib.command.command import Command

import robot

class GetOnPlatformCommand(Command):

    def __init__(self):
        super().__init__('Get On Platform')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.driveForward()


    def execute(self):
        robot.climber.extendAll()


    def end(self):
        robot.climber.stopRacks()
        robot.climber.stopDrive()
