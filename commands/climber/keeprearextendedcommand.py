from wpilib.command.command import Command

import robot

class KeepRearExtendedCommand(Command):

    def __init__(self, l2=False):
        super().__init__('Keep Rear Extended')

        self.requires(robot.climber)

        self.l2 = l2


    def initialize(self):
        robot.climber.retractFront()


    def execute(self):
        if(not self.l2):
            robot.climber.extendRear()


    def end(self):
        robot.climber.stopRacks()
