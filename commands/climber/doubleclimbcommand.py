from wpilib.command.command import Command

import robot

class DoubleClimbCommand(Command):

    def __init__(self):
        super().__init__('Double Climb')

        self.requires(robot.climber)


    def initialize(self):
        self._finished = False
        robot.climber.resetEncoders()


    def execute(self):
        robot.climber.extendAllEnc()
        print('here')

    def isFinished(self):
        return robot.climber.getAvgPosition() >= 16500


    def end(self):
        print('Done')
        robot.climber.stopRacks()

