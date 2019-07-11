from .basedrive import BaseDrive
from ctre._impl import ControlMode
from wpilib.drive.robotdrivebase import RobotDriveBase
import ports

class SkidDrive(BaseDrive):
    '''A drive base where all wheels on each side move together.'''


    def _configureMotors(self):

        '''Only the front motors are active in a skid system.'''
        self.activeMotors = self.motors[0:2]

        '''Make the back motors follow the front.'''


        if len(self.motors) == 4:
            try:
                self.motors[RobotDriveBase.MotorType.kRearLeft] \
                .follow(self.motors[RobotDriveBase.MotorType.kFrontLeft])
                self.motors[RobotDriveBase.MotorType.kRearRight] \
                .follow(self.motors[RobotDriveBase.MotorType.kFrontRight])

            except:
                pass


        '''Invert encoders'''

    def _calculateSpeeds(self, x, y, rotate):
        return [y + rotate, -y + rotate]
