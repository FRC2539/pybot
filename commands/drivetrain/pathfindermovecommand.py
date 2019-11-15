from wpilib.command.command import Command

import pathfinder as pf
from pathfinder.followers import EncoderFollower

import math
import robot

class PathfinderMoveCommand(Command):

    def __init__(self, points=[]):
        super().__init__('Pathfinder Move')

        self.requires(robot.drivetrain)
        self.points = points#[[-4, -1, 0], [-2, -2, 0], [0, 0, 0]]#points

    def initialize(self):
        robot.drivetrain.resetGyro()

        if not self.points:
            raise ValueError('No points given!')

        pfPoints = robot.drivetrain.pointsToPathfinder(self.points)
        print(str(pfPoints))

        pdfPoints = [pf.Waypoint(0, -3, 0), pf.Waypoint(1, 1, 0)]
        print(str(pdfPoints))

        info, trajectory = pf.generate(pdfPoints, pf.FIT_HERMITE_CUBIC, pf.SAMPLES_HIGH,
                                       dt=0.004,
                                       max_velocity=1,
                                       max_acceleration=2.0,
                                       max_jerk=120.0
                                       )

        print('info ' + str(info))
        print('trajectory ' + str(trajectory))

        modifier = pf.modifiers.TankModifier(trajectory).modify(0.5)

        self.left, self.right = robot.drivetrain.createEncoderFollowers(modifier)

        print('done with initialize')

    def execute(self):
        leftOut = self.left.calculate(int(robot.drivetrain.getFrontLeftPosition()))
        rightOut = self.right.calculate(int(robot.drivetrain.getFrontRightPosition()))

        print(str(leftOut) + ' ' + str(rightOut))

        gyroHeading = robot.drivetrain.getAngle()
        desiredHeading = pf.r2d(self.left.getHeading())
        print(str(desiredHeading) + ' desired heading')
        angleDifference = pf.boundHalfDegrees(desiredHeading - gyroHeading)

        turn = 0.8 * (1.0 / 80.0) * angleDifference

        print(str(leftOut + turn) + ' \n\n LOOK OVER HERE YOU MORON \n\n ' + str(rightOut - turn))

        robot.drivetrain.setSideSpeeds(leftOut + turn, rightOut - turn)

    def isFinished(self):
        return self.left.isFinished() or self.right.isFinished()

    def end(self):
        robot.drivetrain.stop()
