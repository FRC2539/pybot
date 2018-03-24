from wpilib.command import Command
from custom.config import Config
from custom import driverhud
import subsystems

class MoveWithGyroCommand(Command):

    def __init__(self, distance, avoidCollisions=True, name=None):
        '''
        Takes a distance in inches and stores it for later. We allow overriding
        name so that other autonomous driving commands can extend this class.
        '''

        if name is None:
            name = 'Move %f inches with gyro' % distance

        super().__init__(name, 0.2)

        self.distance = distance
        self.blocked = False
        self.avoidCollisions = avoidCollisions
        self.requires(subsystems.drivetrain)


    def initialize(self):
        self.obstacleCount = 0
        self.blocked = False
        self.onTarget = 0
        self.targetPositions = []
        offset = self.distance * Config('DriveTrain/ticksPerInch')
        sign = 1
        for position in subsystems.drivetrain.getPositions():
            self.targetPositions.append(position + offset * sign)
            sign *= -1

        subsystems.drivetrain.resetGyro()
        subsystems.drivetrain.setPositionsWithGyro(self.targetPositions)


    def execute(self):
        if self.avoidCollisions:
            if not self.blocked:
                if subsystems.drivetrain.getFrontClearance() < 10:
                    self.obstacleCount += 1
                else:
                    self.obstacleCount = 0

                if self.obstacleCount >= 10:
                    self.blocked = True
                    self.obstacleCount = 0
                    subsystems.drivetrain.stop()
                    subsystems.drivetrain.move(0, 0, 0)
                    driverhud.showAlert('Obstacle Detected')
            else:
                if subsystems.drivetrain.getFrontClearance() >= 20:
                    self.obstacleCount += 1
                else:
                    self.obstacleCount = 0

                if self.obstacleCount >= 10:
                    self.blocked = False
                    self.obstacleCount = 0
                    subsystems.drivetrain.setPositionsWithGyro(self.targetPositions)

        subsystems.drivetrain.setPositionsWithGyro(self.targetPositions)


    def isFinished(self):
        if self.blocked:
            return False

        if self.isTimedOut() and subsystems.drivetrain.atPosition(20):
            self.onTarget += 1
        else:
            self.onTarget = 0

        return self.onTarget > 5
