from wpilib.command.command import Command
from controller import logicalaxes
from commands.climber.climbcommandgroup import ClimbCommandGroup

import math
import robot

logicalaxes.registerAxis('climb')


class BensClimbCommand(Command):

    def __init__(self):
        super().__init__('Bens Climb')

        self.requires(robot.climber)


    def initialize(self):
        self.lastPos = None
        self.slowSpeed = None
        self._isFinished

    def execute(self):
        pos = logicalaxes.climb.get()
        #if self.lastPos == None:
            #self.lastPos = pos
        #else:
            #cooldown = 0.05
            #self.lastPos -= math.copysign(cooldown, self.lastPos)
        print('pos' + str(pos))
        if logicalaxes.climb.get() >= 0.99:
            self._isFinished = True


    def isFinished(self):
        return self._isFinished

    def end(self):
        self.ClimbCommandGroup()
