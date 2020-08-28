from wpilib.command import Command

from wpilib.trajectory import TrajectoryConfig
from wpilib.trajectory import TrajectoryGenerator

from wpilib.trajectory.constraint import DifferentialDriveVoltageConstraint

from wpilib.controller import SimpleMotorFeedforward, RamseteController, PIDController

from wpilib.kinematics import DifferentialDriveKinematics

from trajectoryconstants import DriveConstants, AutoConstants, TrajectoryPoints

from crapthatwillneverwork.ramsetecommand import RamseteCommand

import robot

class TrajectoryCommand(Command):

    def __init__(self, trajectoryNumber):

        # This is terrifying lol.

        # These values below should and will come from the frc-characterization tool!

        self.kDriveKinematics = DifferentialDriveKinematics(DriveConstants.kTrackWidthMeters)

        self.autoVoltageConstraint = DifferentialDriveVoltageConstraint(
            SimpleMotorFeedforward(DriveConstants.ksVolts,
                                   DriveConstants.kvVoltsSecondPerMeter,
                                   DriveConstants.kaVoltSecondsSquaredPerMeter),
            self.kDriveKinematics,
            10 # Max voltage.
            )

        self.trajectoryConfig = TrajectoryConfig(AutoConstants.kMaxSpeedMetersPerSecond,
                                                 AutoConstants.kMaxAccelerationMetersPerSecondSquared,
                                                )

        self.trajectoryConfig.setKinematics(self.kDriveKinematics)
        self.trajectoryConfig.addConstraint(self.autoVoltageConstraint)

        path = TrajectoryPoints.points[trajectoryNumber]

        self.trajectory = TrajectoryGenerator.generateTrajectory(path[0],
                                                                 path[1:-1],
                                                                 path[-1],
                                                                 self.trajectoryConfig
                                                                 )

        ramseteCommand = RamseteCommand(self.trajectory,
                                        robot.drivetrain.getPose(),
                                        RamseteController(AutoConstants.kRamseteB, AutoConstants.kRamseteZeta),
                                        SimpleMotorFeedforward(DriveConstants.ksVolts,
                                                               DriveConstants.kvVoltsSecondPerMeter,
                                                               DriveConstants.kaVoltSecondsSquaredPerMeter),
                                        DriveConstants.kDriveKinematics,
                                        robot.drivetrain.getWheelSpeeds,
                                        PIDController(DriveConstants.kPDriveVel, 0, 0),
                                        PIDController(DriveConstants.kPDriveVel, 0, 0),
                                        robot.drivetrain.setVolts,
                                        robot.drivetrain
                                        )
