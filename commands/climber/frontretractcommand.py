from wpilib.command.command import Command

import robot

class FrontRetractCommand(Command):

    def __init__(self):
        super().__init__('Front Retract')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.retractFront()


    def execute(self):
        pass


    def end(self):
        robot.climber.stopRacks()
