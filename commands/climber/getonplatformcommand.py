from wpilib.command.command import Command

import robot

class GetOnPlatformCommand(Command):

    def __init__(self, l2=False):
        super().__init__('Get On Platform')

        self.requires(robot.climber)
        self.l2 = l2


    def initialize(self):
        robot.climber.driveForward()


    def execute(self):
        if(not self.l2):
            robot.climber.extendAll()


    def end(self):
        robot.climber.stopRacks()
        robot.climber.stopDrive()
