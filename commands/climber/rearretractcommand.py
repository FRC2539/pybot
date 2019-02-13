from wpilib.command.command import Command

import robot

class RearRetractCommand(Command):

    def __init__(self):
        super().__init__('Rear Retract')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.retractRear()


    def execute(self):
        pass


    def end(self):
        robot.climber.stopRacks()
