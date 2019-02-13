from wpilib.command.command import Command

import robot

class AllExtendCommand(Command):

    def __init__(self):
        super().__init__('All Extend')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.extendAll()


    def execute(self):
        pass


    def end(self):
        robot.climber.stopRacks()
