from .falconbasedrive import FalconBaseDrive
from .neobasedrive import NeoBaseDrive
from ctre import ControlMode
from rev import CANSparkMax, MotorType
from wpilib.drive import RobotDriveBase
import ports

testMax = CANSparkMax(0, MotorType.kBrushless)

class SkidDrive(FalconBaseDrive if 'v0.0' in testMax.getFirmwareString() else NeoBaseDrive):
    '''A drive base where all wheels on each side move together.'''
    
    def _deleteTestController(self):      
        try:
            del testMax
        except(UnboundLocalError):
            pass
    
    def _configureMotors(self):
        '''Only the front motors are active in a skid system.'''
        
        self.activeMotors = self.motors[0:2]

        '''Make the back motors follow the front.'''
        if len(self.motors) == 4:
            self.motors[2] \
                .follow(self.motors[0])
            self.motors[3] \
                .follow(self.motors[1])
            
        try:

            self.activePIDControllers = [y.getPIDController() for y in self.activeMotors]
            self.activeEncoders = [y.getEncoder() for y in self.activeMotors]

        except(AttributeError):
            
            self.activePIDControllers = []
            self.activeEncoders = []

            '''Invert encoders'''
            for motor in self.activeMotors:
                motor.setSensorPhase(True)


    def _calculateSpeeds(self, x, y, rotate):
        return [y + rotate, -y + rotate]
