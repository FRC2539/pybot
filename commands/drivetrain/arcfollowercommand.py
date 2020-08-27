from wpilib.command import Command

import robot


class ArcFollowerCommand(Command):

    def __init__(self, xTwo, yTwo, slopeStart, slopeEnd, xOne=0.0, yOne=0.0): # NOTE: Give slope as an integer or fraction, NO DECIMALS!
        super().__init__('Arc Follower')

        '''

        Experimental command for a standard tank system with a NavX.

        xTwo: The end point's x-coordinate
        yTwo: The end point's y-coordinate
        slopeStart: The starting 'angle' of the robot. Think of this as rise over run! 75 (the default) is about a straight, vertical line.
        slopeEnd: The ending 'angle' of the robot. See slopeStart.
        xOne: The start point's x-coordinate, typically 0.0.
        yOne: The start point's y-coordinate, typically 0.0.

        '''

        self.requires(robot.drivetrain)

        if xOne == xTwo:
            raise Exception('Use the drive command for a vertical line! . . . I really hope it\'s a vertical line . . . ')

        special = True

        if '/' in str(slopeStart):
            yPrimeOne = float(str(slopeStart).split('/')[0])
        else:
            yPrimeOne = float(slopeStart)

        if '/' in str(slopeEnd):
            yPrimeTwo = float(str(slopeEnd).split('/')[0])
        else:
            yPrimeTwo = float(slopeEnd)

        if xOne == 0.0:
            special = False

        a, b, c, d = robot.drivetrain.generatePolynomial(xOne, yOne, xTwo, yTwo, yPrimeOne, yPrimeTwo, special)

        eq = robot.drivetrain.getEquation(a, b, c, d)

        self.arcLength, self.derivative = robot.drivetrain.calcArcLength(xOne, xTwo, eq)

        self.finalX = xTwo

    def initialize(self):
        robot.drivetrain.resetEncoders()
        robot.drivetrain.resetGyro()
        robot.drivetrain.zeroDisplacement()

        robot.drivetrain.assignDerivative(self.derivative)
        robot.drivetrain.assignArcLength(self.arcLength)
        robot.drivetrain.assignFinalX(self.finalX)

    def execute(self):
        robot.drivetrain.angleControlDrive(robot.drivetrain.getHeadingDifference())

    def isFinished(self):
        return ((robot.drivetrain.rotationsToInches(robot.drivetrain.getPositions()[0]) / 12) >= self.arcLength)

    def end(self):
        robot.drivetrain.stop()
