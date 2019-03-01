from wpilib.command.command import Command

import robot

class LeftRetractCommand(Command):

    def __init__(self):
        super().__init__('Left Retract')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.retractLeft()


    def execute(self):
        pass


    def end(self):
        robot.climber.stopRacks()
