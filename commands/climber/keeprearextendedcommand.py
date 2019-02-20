from wpilib.command.command import Command

import robot

class KeepRearExtendedCommand(Command):

    def __init__(self):
        super().__init__('Keep Rear Extended')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.retractFront()


    def execute(self):
        robot.climber.extendRear()


    def end(self):
        robot.climber.stopRacks()
