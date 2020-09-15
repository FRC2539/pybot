from wpilib.trajectory import TrajectoryConfig
from wpilib.trajectory import TrajectoryGenerator

from wpilib.trajectory.constraint import DifferentialDriveVoltageConstraint

from wpilib.controller import SimpleMotorFeedforwardMeters, RamseteController, PIDController

from wpilib.kinematics import DifferentialDriveKinematics

from trajectoryconstants import DriveConstants, AutoConstants, TrajectoryPoints, generateObjects

from crapthatwillneverwork.ramsetecommand import RamseteCommand

import robot

class TrajectoryCommand:

    def __init__(self, desiredPointsOrID):
                        
        if type(desiredPointsOrID) == int or type(desiredPointsOrID) == float:
            path = TrajectoryPoints.points[desiredPointsOrID] # We have a preset. 
            
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
        
        #self.ramseteCommand = RamseteCommand(
    def getCommand(self):
        return [self.trajectory,
        robot.drivetrain.getPoseMeters,
        RamseteController(AutoConstants.kRamseteB, AutoConstants.kRamseteZeta),
        SimpleMotorFeedforwardMeters(DriveConstants.ksVolts,
                                DriveConstants.kvVoltsSecondPerMeter,
                                DriveConstants.kaVoltSecondsSquaredPerMeter),
        self.kDriveKinematics,
        robot.drivetrain.getWheelSpeeds,
        PIDController(DriveConstants.kPDriveVel, 0, 0),
        PIDController(DriveConstants.kPDriveVel, 0, 0),
        robot.drivetrain.setVolts,
        robot.drivetrain]
                                        #)