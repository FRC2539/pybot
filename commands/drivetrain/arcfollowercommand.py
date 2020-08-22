from wpilib.command import Command

import robot


class ArcFollowerCommand(Command):

    def __init__(self, xTwo, yTwo, slopeOne, slopeTwo, xOne=0.0, yOne=0.0): # NOTE: Give slope as an integer or fraction, NO DECIMALS!
        super().__init__('Arc Follower')

        self.requires(robot.drivetrain)

        special = True

        if '/' in str(slopeOne):
            yPrimeOne = float(str(slopeOne).split('/')[0])
        else:
            yPrimeOne = float(slopeOne)

        if '/' in str(slopeTwo):
            yPrimeTwo = float(str(slopeTwo).split('/')[0])
        else:
            yPrimeTwo = float(slopeTwo)

        if xOne == 0.0:
            special = False

        a, b, c, d = robot.drivetrain.generatePolynomial(xOne, yOne, xTwo, yTwo, yPrimeOne, yPrimeTwo, special)

        eq = robot.drivetrain.getEquation(a, b, c, d)

        self.arcLength, self.derivative = robot.drivetrain.calcArcLength(xOne, xTwo, eq)

    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
