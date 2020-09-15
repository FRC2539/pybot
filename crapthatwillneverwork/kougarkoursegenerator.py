from wpilib.trajectory import TrajectoryConfig
from wpilib.trajectory import TrajectoryGenerator

from wpilib.geometry import Pose2d

from wpilib.trajectory.constraint import DifferentialDriveVoltageConstraint

from wpilib.controller import SimpleMotorFeedforwardMeters, RamseteController, PIDController

from wpilib.kinematics import DifferentialDriveKinematics

from trajectoryconstants import DriveConstants, AutoConstants, TrajectoryPoints, generateObjects

import robot

class KougarKourseGenerator:

    def __init__(self, desiredPointsOrID):
                        
        if type(desiredPointsOrID) == int or type(desiredPointsOrID) == float:
            if isinstance(TrajectoryPoints.points[desiredPointsOrID][0], Pose2d):
                path = TrajectoryPoints.points[desiredPointsOrID] # We have a preset. 
            else:
                raise TypeError("Please don't add points in that format here. Instead, replace the ID with the list.")
        else:
            # NOTE: If you choose to use custom points, remember to provide an X, Y, and rotation in degrees.
            
            path = generateObjects(desiredPointsOrID)

        # This is terrifying lol.

        # These values below should and will come from the frc-characterization tool!

        self.kDriveKinematics = DifferentialDriveKinematics(DriveConstants.kTrackWidthMeters)

        self.autoVoltageConstraint = DifferentialDriveVoltageConstraint(
            SimpleMotorFeedforwardMeters(DriveConstants.ksVolts,
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

        self.trajectory = TrajectoryGenerator.generateTrajectory(path[0],
                                                                 path[1:-1],
                                                                 path[-1],
                                                                 self.trajectoryConfig
                                                                 )
