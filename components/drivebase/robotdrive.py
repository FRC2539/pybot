import wpilib
import ports

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

from drivevelocities import TankDrive, MecanumDrive

class RobotDrive:
    def __init__(self, _type='tank'):
        self.motors = [
                    WPI_TalonSRX(ports.DrivetrainPorts.FrontLeftMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.FrontRightMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.BackLeftMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.BackRightMotor)
                    ]
        
        for motor in self.motors:
            pass
        # Add in motor specifications here               

        if str(_type).lower() == 'tank':
            self.drivetrain = TankDrive(rotateModifier=0.8) # Add desired modifiers here!
            self.activeMotors = self.drivetrain.configureFourTank(self.motors)
        else:
            self.drivetrain = MecanumDrive(rotateModifier=0.8) # Add desired modifiers here!
            self.activeMotors = self.drivetrain.configureMecanum(self.motors)
            
        self.drivetrain.checkParameters()

    def stop(self):
        for motor in self.motors:
            motor.stopMotor()
            
    def driveRobot(self):
        
            
    def move(self, x, y, rotate):
        # Given axises
        speeds = self.tankDrive.getTankSpeed(x, y, rotate)
        
        for motor, velocity in zip(self.activeMotors, speeds):
            motor.set(ControlMode.PercentOutput, velocity)
        
