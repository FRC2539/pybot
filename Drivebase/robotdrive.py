import wpilib
import ports

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

class RobotDrive:
    def __init__(self):
        self.motors = [
                    WPI_TalonSRX(ports.DrivetrainPorts.FrontLeftMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.FrontRightMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.BackLeftMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.BackRightMotor)
                    ]
        
        for motor in self.motors:
            motor.set
            
            
    def stop(self):
        for motor in self.motors:
            motor.stopMotor()
            
    def move(self, x, y, rotate):
        # Given axises
        
        
