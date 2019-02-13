from wpilib.command.command import Command

import robot

class AllRetractCommand(Command):

    def __init__(self):
        super().__init__('All Retract')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.retractAll()


    def execute(self):
        pass


    def end(self):
        robot.climber.stopRacks()
