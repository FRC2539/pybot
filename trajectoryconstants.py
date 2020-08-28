from wpilib.geometry import *

class Constant:
    pass

DriveConstants = Constant()

DriveConstants.ksVolts = 0
DriveConstants.kvVoltsSecondPerMeter = 0
DriveConstants.kaVoltSecondsSquaredPerMeter = 0
DriveConstants.kPDriveVel = 0

DriveConstants.kTrackWidthMeters = 0.6096

# Auto Constants:

AutoConstants = Constant()

AutoConstants.kMaxSpeedMetersPerSecond = 3
AutoConstants.kMaxAccelerationMetersPerSecondSquared = 3

AutoConstants.kRamseteB = 2
AutoConstants.kRamseteZeta = 0.7

TrajectoryPoints = Constant()

TrajectoryPoints.points = {
    0 : [Pose2d(0, 0, Rotation2d(0)), Translation2d(1, 1), Translation2d(2, -1), Pose2d(3, 0, Rotation2d(0))]
    }
