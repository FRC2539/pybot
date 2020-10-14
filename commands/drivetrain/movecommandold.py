from wpilib.command import Command
from custom import driverhud
from custom.config import MissingConfigError
import robot

class MoveCommandOld(Command):

    def __init__(self, distance, avoidCollisions=False, name=None):
        '''
        Takes a distance in inches and stores it for later. We allow overriding
        name so that other autonomous driving commands can extend this class.
        '''

        if name is None:
            name = 'Move %f inches' % distance

        super().__init__(name, 0.2)

        self.distance = distance
        self.stationary = False
        self.requires(robot.drivetrain)
        self.requires(robot.ledsystem)

    def _initialize(self):
        super()._initialize()
        self.precision = robot.drivetrain.inchesToUnits(1)

    def initialize(self):
        if abs(robot.drivetrain.getSpeeds()[0]) < 5.0:
            self.stationary = True

            self.targetPositions = []
            robot.drivetrain.setProfile(1)
            self.offset = robot.drivetrain.inchesToUnits(self.distance)
            print('offset ' +str(self.offset))
            sign = 1
            for position in robot.drivetrain.getPositions():
                self.targetPositions.append(position + (self.offset * sign))
                sign *= -1

            print('my target: ' + str(self.targetPositions))

            robot.drivetrain.setPositions(self.targetPositions)

    def execute(self):
        if not self.stationary:
            self.stationary = True

            self.targetPositions = []
            robot.drivetrain.setProfile(1)
            self.offset = robot.drivetrain.inchesToUnits(self.distance)
            print('offset ' +str(self.offset))
            sign = 1
            for position in robot.drivetrain.getPositions():
                self.targetPositions.append(position + (self.offset * sign))
                sign *= -1

            print('my target: ' + str(self.targetPositions))

            robot.drivetrain.setPositions(self.targetPositions)

        print("current position " + str(robot.drivetrain.getPositions()))

    def isFinished(self):
        print(min([abs(robot.drivetrain.getPositions()[0]), abs(robot.drivetrain.getPositions()[1])]))
        if self.offset < 0:
            print('here')
            print(self.targetPositions[0] >= min([abs(robot.drivetrain.getPositions()[0]), abs(robot.drivetrain.getPositions()[1])]))
            return self.targetPositions[0] >= min([abs(robot.drivetrain.getPositions()[0]), abs(robot.drivetrain.getPositions()[1])])
        else:
            return self.targetPositions[0] <= min([abs(robot.drivetrain.getPositions()[0]), abs(robot.drivetrain.getPositions()[1])])

    def end(self):
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)
