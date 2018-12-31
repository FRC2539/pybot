from wpilib.command.command import Command
import pathfinder as pf

from subsystems.basedrive import BaseDrive
from pathfinder.followers import EncoderFollower

import math
import robot

class FollowTrajectoryCommand(Command):

    def __init__(self, points, fit_type, vel, accel, jerk):
        pass
"""
        super().__init__('Follow Trajectory')
        self.requires(robot.drivetrain)
        self.waypoints = []
        for i in points:
            self.waypoints.append(pf.Waypoint(i[0], i[1], math.radians(i[2])))

        info, trajectory = pf.generate(self.waypoints, pf.FIT_HERMITE_CUBIC, pf.SAMPLES_HIGH,
                                    0.05, # 50ms
                                    vel,
                                    accel,
                                    jerk)

        modifier = pf.modifiers.TankModifier(trajectory).modify(0.7318375)

        self.leftFollower = EncoderFollower(modifier.getLeftTrajectory())
        self.leftFollower.configurePIDVA(1.0, 0.0, 0.0, 1 / 1.7, 0)

        self.rightFollower = EncoderFollower(modifier.getRightTrajectory())
        self.rightFollower.configurePIDVA(1.0, 0.0, 0.0, 1 / 1.7, 0)



    def initialize(self):
        robot.drivetrain.resetGyro()
        robot.drivetrain.resetEncoders()
        self.leftFollower.configureEncoder(0, 4373, 6) # getQuadraturePosition replaces 0
        self.rightFollower.configureEncoder(0, 4373, 6)



#        self.leftOutput = self.leftFollower.calculate(getSensorCollection)
#        self.rightOutput = self.rightFollower.calculate(getSensorCollection)

    def execute(self):
        leftOutput = self.leftFollower.calculate(robot.drivetrain.getPositions()[0])
        rightOutput = self.rightFollower.calculate(robot.drivetrain.getPositions()[1])
        gyro_heading = robot.drivetrain.getAngle()
        desired_heading = pf.r2d(self.leftFollower.getHeading())
        turn = 0.8 * (-1.0/80.0) * pf.boundHalfDegrees(desired_heading - gyro_heading)
        robot.drivetrain.tankDrive(leftOutput + turn, rightOutput - turn)


    def end(self):
        pass
"""
