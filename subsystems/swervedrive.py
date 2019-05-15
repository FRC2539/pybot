from .debuggablesubsystem import DebuggableSubsystem
from .basedrive import BaseDrive
from wpilib.drive.robotdrivebase import RobotDriveBase
from ctre._impl import ControlMode

import ports

class SwerveDrive(BaseDrive):
    '''A drivebase where all four wheels are controlled independently, and is pretty sick.'''
    def _calculateSpeeds(self):
        pass

    def _configureMotors(self):
        pass
