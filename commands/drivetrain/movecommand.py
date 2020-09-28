from wpilib.command import Command
from custom import driverhud
from custom.config import MissingConfigError
import robot

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
        self.precision = robot.drivetrain.inchesToTicks(1)

    def initialize(self):
        self.obstacleCount = 0
        self.blocked = False
        self.onTarget = 0
        self.targetPositions = [] # [Left, right]
        robot.drivetrain.setProfile(1)
        self.offset = robot.drivetrain.inchesToTicks(self.distance)
        sign = 1
        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + (self.offset * sign))
            sign *= -1

        robot.drivetrain.setPositions(self.targetPositions)

    def isFinished(self):
        if self.offset < 0:
            return self.targetPositions[0] >= min([abs(robot.drivetrain.getPositions()[0]), abs(robot.drivetrain.getPositions()[1])])
        else:
            return self.targetPositions[0] <= min([abs(robot.drivetrain.getPositions()[0]), abs(robot.drivetrain.getPositions()[1])])

    def end(self):
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)
