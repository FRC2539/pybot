from wpilib.command.command import Command

import robot

class AllExtendCommand(Command):

    def __init__(self):
        super().__init__('All Extend')

        self.requires(robot.climber)


    def initialize(self):
        self._finished = False
        robot.climber.resetEncoders()
        robot.climber.creepForward()

        robot.climber.startRaise()


    def execute(self):
        #encoder disable
        self._finished = robot.climber.extendAllEnc()
        #self._finished = robot.climber.extendAll()


    def isFinished(self):
        return self._finished


    def end(self):
        robot.climber.stopDrive()
        robot.climber.stopRacks()


    def interrupted(self):
        self.end()
