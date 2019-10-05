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
            name = 'Move %f inches' % distance

        super().__init__(name, 0.2)

        self.distance = distance
        self.blocked = False
        self.avoidCollisions = avoidCollisions
        self.requires(robot.drivetrain)


    def _initialize(self):
        super()._initialize()
        print('BEGAN INITIALIZE\n\n')

        self.precision = robot.drivetrain.inchesToRotations(1)


    def initialize(self):
        print('BEGAN INITIALIZE\n\n')
        self.obstacleCount = 0
        self.blocked = False
        self.onTarget = 0
        self.targetPositions = []
        self.offset = robot.drivetrain.inchesToRotations(self.distance)
        print('offset ' + str(self.offset))
        sign = 1
        print('OLD POSITIONS ' + str(robot.drivetrain.getPositions()))
        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + self.offset * sign)
            sign *= -1

        #print('Targets: ' + str(self.targetPositions))
        #print('Starting: ' + str(robot.drivetrain.getPositions()))

        pos = robot.drivetrain.setPositions(self.targetPositions)
        print('target positions ' + str(self.targetPositions))

        #robot.drivetrain.setPositions(self.targetPositions)
        #print('\nSET POSITIONS')

        #if val:
            #print('\nTRUE\n')
        #else:
            #print('\nFALSE\n')

    def execute(self):
        print('Current: ' + str(robot.drivetrain.getPositions()))

        # Checks for a passing value

        if self.avoidCollisions:
            try:
                if self.distance < 0:
                    clearance = robot.drivetrain.getRearClearance()
                else:
                    clearance = robot.drivetrain.getFrontClearance()

                if not self.blocked:
                    if clearance < 10:
                        if self.obstacleCount >= 10:
                            self.blocked = True
                            self.obstacleCount = 0
                            robot.drivetrain.stop()
                            robot.drivetrain.move(0, 0, 0)
                            driverhud.showAlert('Obstacle Detected')
                        else:
                            self.obstacleCount += 1
                    else:
                        self.obstacleCount = 0

                else:
                    if clearance >= 20:
                        if self.obstacleCount >= 10:
                            self.blocked = False
                            self.obstacleCount = 0
                            robot.drivetrain.setPositions(self.targetPositions)
                        else:
                            self.obstacleCount += 1
                    else:
                        self.obstacleCount = 0

            except NotImplementedError:
                pass

    def isFinished(self):
        '''
        for target, position in zip(self.targetPositions, robot.drivetrain.getPositions()):
            if abs(target) <= abs(position) + abs(self.offset):
                print('target ' + str(target) + ' position + offset ' + str(position + self.offset))
                return True
        if self.blocked:
            return False

        if self.isTimedOut() and robot.drivetrain.atPosition(self.precision):
            self.onTarget += 1
        else:
            self.onTarget = 0

        return self.onTarget > 5
        '''
        return False

    def end(self):
        robot.drivetrain.stop()
