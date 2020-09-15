from wpilib.geometry import Pose2d, Rotation2d, Translation2d

class Constant:
    pass

DriveConstants = Constant()

DriveConstants.ksVolts = 0.169
DriveConstants.kvVoltsSecondPerMeter = 0.0766
DriveConstants.kaVoltSecondsSquaredPerMeter = 0.0096
DriveConstants.kPDriveVel = 0.214

DriveConstants.kTrackWidthMeters = 0.6096

# Auto Constants:

AutoConstants = Constant()

AutoConstants.kMaxSpeedMetersPerSecond = 3
AutoConstants.kMaxAccelerationMetersPerSecondSquared = 3

AutoConstants.kRamseteB = 2
AutoConstants.kRamseteZeta = 0.7

TrajectoryPoints = Constant()

TrajectoryPoints.points = { # Remember to format like one of the two below.
    0 : [Pose2d(0, 0, Rotation2d(0)), Translation2d(1, 1), Translation2d(2, -1), Pose2d(3, 0, Rotation2d(0))],
    }

def generateObjects(self, list_):
    newList = []
    newList.append(Pose2d(list_[0][0], list_[0][1], Rotation2d(list_[0][2]))) # Adds the first pose in.
    
    for X, Y, angle in list_[1:-1]: # Adds the middle translations in.
        newList.append(Translation2d(X, Y)) # Doesn't need the angle. 
        
    newList.append(Pose2d(list_[-1][0], list_[-1][1], Rotation2d(list_[-1][2]))) # Adds the last pose in.
    
    return newList
