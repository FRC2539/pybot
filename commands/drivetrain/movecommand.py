from wpilib.command import Command
from custom import driverhud
from custom.config import MissingConfigError
import robot

class MoveCommand(Command):

    def __init__(self, distance, avoidCollisions=False, name=None):
        '''
        Takes a distance in inches and stores it for later. We allow overriding
        name so that other autonomous driving commands can extend this class.
        '''

        if name is None:
            name = 'Move Old %f inches' % distance

        super().__init__(name, 0.2)

        self.distance = distance
        
        self.stationary = False
        self.requires(robot.drivetrain)

    def _initialize(self):
        super()._initialize()
        self.precision = robot.drivetrain.inchesToUnits(1)

    def initialize(self):

        self.targetPositions = []
        self.offset = robot.drivetrain.inchesToUnits(self.distance)
                
        sign = 1
        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + (self.offset * sign))
            sign *= -1

        print('my target: ' + str(self.targetPositions))

        robot.drivetrain.setPositions(self.targetPositions)
        
    def execute(self):
        print('LEFT TARGET: ' + str(self.targetPositions[0]))
        print('LEFT POS: ' + str(robot.drivetrain.getPositions()[0]))
        
    def isFinished(self):
        return robot.drivetrain.doneMoving(self.targetPositions)
        
    def end(self):
        print('DONE')
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)
