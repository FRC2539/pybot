from wpilib.command.command import Command

import robot

class L2ExtendCommand(Command):

    def __init__(self):
        super().__init__('L2 Extend')

        self.requires(robot.climber)


    def initialize(self):
        self._finished = False
        robot.climber.resetEncoders()
        robot.climber.creepForward()


    def execute(self):
        robot.climber.extendAllEnc()


    def isFinished(self):
        return robot.climber.getAvgPosition() >= 15500


    def end(self):
        robot.climber.stopDrive()
        robot.climber.stopRacks()


    def interrupted(self):
        self.end()
