from wpilib.command.command import Command

import pathfinder as pf
from pathfinder.followers import EncoderFollower

import math
import robot

class PathfinderMoveCommand(Command):

    def __init__(self, points=[]):
        super().__init__('Pathfinder Move')

        self.requires(robot.drivetrain)

        self.points = [0,0]

        robot.drivetrain.resetGyro()

    def initialize(self):
        robot.drivetrain.resetGyro()
        robot.drivetrain.manipulateStupidGyro(0.05)

        if not self.points:
            raise ValueError('No points given!')

        #pfPoints = robot.drivetrain.pointsToPathfinder(self.points)
        #print(str(pfPoints))

        #pdfPoints = [pf.Waypoint(0, 0, 0), pf.Waypoint(0, 5, 0)]
        #print(str(pdfPoints))

        #info, trajectory = pf.generate(pdfPoints, pf.FIT_HERMITE_CUBIC, pf.SAMPLES_HIGH,
                                       #dt=0.020,
                                       #max_velocity=5.0,
                                       #max_acceleration=2.0,
                                       #max_jerk=120.0
                                       #)

        #print('info ' + str(info))
        #print('trajectory ' + str(trajectory))

        trajectory = robot.drivetrain.getTrajectory()
        modifier = pf.modifiers.TankModifier(trajectory).modify(1.6823) # Wheelbase (Front to rear)

        robot.drivetrain.enableConversionFactor()

        self.left, self.right = robot.drivetrain.createEncoderFollowers(modifier)

        robot.drivetrain.resetEncoders()

    def execute(self):
        leftOut = self.left.calculate(int(robot.drivetrain.getFrontLeftPosition()))
        rightOut = self.right.calculate(int(robot.drivetrain.getFrontRightPosition()))

        print('heading ' + str(robot.drivetrain.getAngle()))

        gyroHeading = robot.drivetrain.getAngle()
        desiredHeading = pf.r2d(self.left.getHeading())

        angleDifference = pf.boundHalfDegrees(desiredHeading - gyroHeading)

        turn = 5 * (-1.0 / 80.0) * angleDifference

        robot.drivetrain.setSideSpeeds(leftOut + turn, rightOut - turn)

        print(str(self.left.isFinished()) + ' statuses of side trajectories ' + str(self.right.isFinished()))

    def isFinished(self):
        return self.left.isFinished() or self.right.isFinished()

    def end(self):
        robot.drivetrain.disableConversionFactor()
        robot.drivetrain.stop()
