from wpilib.command import Command

import robot

class SetHoodCommand(Command):

    def __init__(self, angle):
        super().__init__('Set Hood')

        self.requires(robot.hood)

        realAngle = robot.hood.angleMin + (2 * angle)

        self.angle = realAngle
        self.oldAngle = realAngle

        self.dir = 'u'

    def initialize(self):
        self.angle = self.oldAngle
        if robot.hood.getPosition() >= self.angle:
            self.speed = -0.3
            self.dir = 'd'
            self.angle += 5 # compensating for gear lash
        else:
            self.speed = 0.3
            self.dir = 'u'
            self.angle -= 5

        #print(self.dir)
        if abs(robot.hood.getPosition() - self.angle) < 1:
            robot.hood.stopHood()

        else:
            robot.hood.setPercent((self.speed))


    def execute(self):
        #print(robot.hood.getPosition())
        if (robot.hood.getPosition() <= self.angle and self.dir == 'd') or (robot.hood.getPosition() >= self.angle and self.dir == 'u'):
            robot.hood.stopHood()
        else:
            robot.hood.setPercent((self.speed))

    def isFinished(self):
        if abs(robot.hood.getPosition() - self.angle) <= 1:
            return True

        return False

    def end(self):
        robot.hood.stopHood()
        robot.hood.updateNetworkTables()
