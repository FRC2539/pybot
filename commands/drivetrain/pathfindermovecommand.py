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
        if self.points is []:
            raise ValueError('No points given!')

        pfPoints = robot.drivetrain.pointsToPathfinder(self.points)
        print(str(pfPoints))

        pdfPoints = [pf.Waypoint(-4, -1, math.radians(-45.0)), pf.Waypoint(-2, -2, 0), pf.Waypoint(0, 0, 0)]
        print(str(pdfPoints))

        info, trajectory = pf.generate(pfPoints, pf.FIT_HERMITE_CUBIC, pf.SAMPLES_HIGH,
                                       dt=0.05,
                                       max_velocity=1.7,
                                       max_acceleration=2.0,
                                       max_jerk=1.0
                                       )

        print('trajectory ' + str(trajectory))

        modifier = pf.modifiers.TankModifier(trajectory).modify(0.5)

        self.left, self.right = robot.drivetrain.createEncoderFollowers(modifier)

    def execute(self):
        leftOut = self.left.calculate(int(robot.drivetrain.getFrontLeftPosition()))
        rightOut = self.right.calculate(int(robot.drivetrain.getFrontRightPosition()))

        gyroHeading = robot.drivetrain.getAngle()
        desiredHeading = pf.r2d(self.left.getHeading())

        angleDifference = pf.boundHalfDegrees(desiredHeading - gyroHeading)

        turn = 0.8 * (-1.0 / 80.0) * angleDifference

        print(str(leftOut + turn) + ' ' + str(rightOut - turn))

        robot.drivetrain.setSideSpeeds(leftOut + turn, rightOut - turn)

    def end(self):
        robot.drivetrain.stop()
