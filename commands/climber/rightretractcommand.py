from wpilib.command.command import Command

import robot

class RightRetractCommand(Command):

    def __init__(self):
        super().__init__('Right Retract')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.retractRight()


    def execute(self):
        pass


    def end(self):
        robot.climber.stopRacks()
