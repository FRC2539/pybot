from wpilib.command import Command

import robot


class ArcFollowerCommand(Command):

    def __init__(self, radius, angle, turnRight, averageSpeed=6):#xTwo, yTwo, slopeOne, slopeTwo, xOne=0.0, yOne=0.0): # NOTE: Give slope as an integer or fraction, NO DECIMALS!
        super().__init__('Arc Follower')

        self.requires(robot.drivetrain)

        self.radius = radius
        self.angle = angle
        self.turnRight = turnRight
        self.averageSpeed = averageSpeed

        if self.radius < (robot.drivetrain.drivetrainWidth / 12) * 2:
            raise Exception('You cannot have a radius that small for that drive train!')

        #special = True

        #if '/' in str(slopeOne):
            #yPrimeOne = float(str(slopeOne).split('/')[0])
        #else:
            #yPrimeOne = float(slopeOne)

        #if '/' in str(slopeTwo):
            #yPrimeTwo = float(str(slopeTwo).split('/')[0])
        #else:
            #yPrimeTwo = float(slopeTwo)

        #if xOne == 0.0:
            #special = False

        #a, b, c, d = robot.drivetrain.generatePolynomial(xOne, yOne, xTwo, yTwo, yPrimeOne, yPrimeTwo, special)

        #eq = robot.drivetrain.getEquation(a, b, c, d)

        #self.arcLength, self.derivative = robot.drivetrain.calcArcLength(xOne, xTwo, eq)

    def initialize(self):
        self.insideDistance, self.outerDistance = robot.drivetrain.calcSideDistances(self.radius, self.angle)

        self.baseTime = self.insideDistance / self.averageSpeed

        self.outerSpeed = self.outerDistance / self.baseTime
        self.innerSpeed = self.insideDistance / self.baseTime

        print('inside distance ' + str(self.insideDistance))
        print('outer distance ' +  str(self.outerDistance))

        print('inside speed ' + str(self.innerSpeed))
        print('outside speed ' + str(self.outerSpeed))

        if self.turnRight:
            self.leftSpeed = self.outerSpeed
            self.rightSpeed = self.innerSpeed

        else:
            self.leftSpeed = self.innerSpeed
            self.rightSpeed = self.outerSpeed

    def execute(self):
        pass


    def end(self):
        pass
