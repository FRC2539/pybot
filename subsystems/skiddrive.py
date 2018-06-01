from .basedrive import BaseDrive
from ctre import WPI_TalonSRX, ControlMode
from wpilib.robotdrive import RobotDrive
import ports

class SkidDrive(BaseDrive):
    '''A drive base where all wheels on each side move together.'''


    def _configureMotors(self):

        '''Only the front motors are active in a skid system.'''
        self.activeMotors = self.motors[0:2]

        '''Make the back motors follow the front.'''
        self.motors[2].enableVoltageCompensation(True)
        self.motors[2].set(ControlMode.Follower, ports.drivetrain.frontLeftMotorID)
        self.motors[3].enableVoltageCompensation(True)
        self.motors[3].set(ControlMode.Follower, ports.drivetrain.frontRightMotorID)

        self.motors[2].setInverted(True)
        self.motors[3].setInverted(True)


    def _calculateSpeeds(self, x, y, rotate):
        return [y + rotate, -y + rotate]

