from wpilib.command import Command
from custom import driverhud
from custom.config import MissingConfigError
import robot
import math

class MoveCommand(Command):

    def __init__(self, distance, avoidCollisions=True, name=None):
        '''
        Takes a distance in inches and stores it for later. We allow overriding
        name so that other autonomous driving commands can extend this class.
        '''

        if name is None:
            name = 'Move %f inches' % distance

        super().__init__(name, 0.2)

        self.distance = distance
        self.blocked = False
        self.avoidCollisions = avoidCollisions
        self.requires(robot.drivetrain)

    def _initialize(self):
        super()._initialize()
        self.precision = robot.drivetrain.inchesToUnits(1)
        
    def initialize(self):
        
        for x in range(1000):
            pass
        
        robot.drivetrain.resetEncoders()
        robot.drivetrain.stop()
        self.obstacleCount = 0
        self.blocked = False
        self.onTarget = 0
        self.targetPositions = [0, 0] # [Left, right]
        robot.drivetrain.setProfile(1)
        self.offset = abs(robot.drivetrain.inchesToUnits(self.distance))
        
        sign = 1
        
        #for position in robot.drivetrain.getPositions():
            #self.targetPositions.append(position + (self.offset * sign))
            #sign *= -1

        self.startPos = abs(robot.drivetrain.getPositions()[0])
        
        self.goal = self.offset + self.startPos

    def execute(self):
        self.currentPos = abs(robot.drivetrain.getPositions()[0])
        remaining = self.goal - self.currentPos
        print('remaining ' + str(remaining))

        speed = math.copysign(max(min(abs(((remaining * 1.5) / self.goal)), 0.8), 0.2), self.distance)

        print('speed ' + str(speed))

        robot.drivetrain.move(0, speed, 0)

    def isFinished(self):    
        print('goal ' + str(self.goal))
        return self.goal <= self.currentPos
        #if self.offset < 0:
            #return self.targetPositions[0] >= min([abs(robot.drivetrain.getPositions()[0]), abs(robot.drivetrain.getPositions()[1])])
        #else:
            #return self.targetPositions[0] <= min([abs(robot.drivetrain.getPositions()[0]), abs(robot.drivetrain.getPositions()[1])])

    def end(self):
        
        for x in range(1000):
            print('goal' + str(self.goal))
            print('pos ' + str(self.currentPos))
        
        robot.drivetrain.stop()
