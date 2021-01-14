from ctre import WPI_TalonFX, CANCoder, NeutralMode, TalonFXControlMode, \
FeedbackDevice, AbsoluteSensorRange, RemoteSensorSource

import math

import constants

class SwerveModule:
    
    def __init__(self, driveMotorID, turnMotorID, canCoderID, speedLimit): # Get the ports of the devices for a module.
        
        '''
        The class constructor.
        
        TODO:
        - Organize method definitions into logical order.
        '''
        
        self.driveMotor = WPI_TalonFX(driveMotorID) # Declare and setup drive motor.
        
        self.driveMotor.setNeutralMode(NeutralMode.Brake)
        self.driveMotor.setSafetyEnabled(False)
        self.driveMotor.configSelectedFeedbackSensor(FeedbackDevice.IntegratedSensor, 0, 0)
    
        self.dPk = constants.drivetrain.dPk # P gain for the drive. 
        self.dIk = constants.drivetrain.dIk # I gain for the drive
        self.dDk = constants.drivetrain.dDk # D gain for the drive
        self.dFk = constants.drivetrain.dFFk # Feedforward gain for the drive
        self.dIZk = constants.drivetrain.dIZk # Integral Zone for the drive
        
        self.cancoder = CANCoder(canCoderID) # Declare and setup the remote encoder. 
        self.cancoder.configAbsoluteSensorRange(AbsoluteSensorRange.Signed_PlusMinus180, 0)
    
        self.turnMotor = WPI_TalonFX(turnMotorID) # Declare and setup turn motor.
        
        self.turnMotor.setNeutralMode(NeutralMode.Brake)
        self.turnMotor.setSafetyEnabled(False)
        self.turnMotor.configSelectedFeedbackSensor(FeedbackDevice.RemoteSensor0, 0, 0) # Set the feedback sensor as remote.
        self.turnMotor.configRemoteFeedbackFilter(canCoderID, RemoteSensorSource.CANCoder, 0, 0) # Configure and select CANCoder. 
        
        self.tPk = constants.drivetrain.tPk # P gain for the turn.
        self.tIk = constants.drivetrain.tIk # I gain for the turn.
        self.tDk = constants.drivetrain.tDk # D gain for the turn.
        self.tFk = constants.drivetrain.tFFk # Feedforward gain for the turn.
        self.tIZk = constants.drivetrain.tIZk # Integral Zone for the turn.
        
        self.wheelDiameter = constants.drivetrain.wheelDiameter # The diamter, in inches, of our driving wheels. 
        self.circ = self.wheelDiameter * math.pi # The circumference of our driving wheel.
        
        self.driveMotorGearRatio = constants.drivetrain.driveMotorGearRatio # 6.86 motor rotations per wheel rotation (on y-axis).
        self.turnMotorGearRatio = constants.drivetrain.turnMotorGearRatio # 12.8 motor rotations per wheel rotation (on x-axis).
        
        self.speedLimit = speedLimit # Pass the speed limit at instantiation so we can drive more easily. 
        
        self.setPID()
                
    def getWheelAngle(self):
        '''
        Get wheel angle relative to the robot.
        '''
        return self.turnMotor.getSelectedSensorPosition(0) # Returns absolute position of CANCoder. 
        
    def setWheelAngle(self, angle):
        '''
        This will set the angle of the wheel, relative to the robot. 
        0 degrees is facing forward. This will accept 0 - 360!
        '''
        self.turnMotor.set(TalonFXControlMode.Position, angle)
        
    def getWheelSpeed(self):
        '''
        Get the speed of this specific module.
        '''
        return self.driveMotor.getSelectedSensorVelocity() # Returns ticks per 0.1 seconds (100 mS). 
        
    def setWheelSpeed(self, speed):
        '''
        This will set the speed of the drive motor to a set velocity.
        '''
        self.driveMotor.set(TalonFXControlMode.Velocity, speed * self.speedLimit)
        
    def stopModule(self):
        '''
        Stop the motors within the module.
        '''
        self.turnMotor.stopMotor()
        self.driveMotor.stopMotor()
    
    def inchesToDriveTicks(self, inches):
        wheelRotations = inches / self.circ # Find the number of wheel rotations by dividing the distance into the circumference. 
        motorRotations = wheelRotations * self.driveMotorGearRatio # Find out how many motor rotations this number is.
        return motorRotations * 2048 # 2048 ticks in one Falcon rotation.
    
    def driveTicksToInches(self, ticks):
        motorRotations = ticks / 2048
        wheelRotations = motorRotations / self.driveMotorGearRatio
        return wheelRotations * self.circ # Basically just worked backwards from the sister method above.
    
    def setModuleProfile(self, profile):
        '''
        Which PID profile to use.
        '''
        self.turnMotor.selectProfileSlot(profile, 0)
        self.driveMotor.selectProfileSlot(profile, 0)
    
    def setPID(self):
        '''
        Set the PID constants for the module.
        '''
        for slot in range(2):
            self.driveMotor.config_kP(slot, self.dPk, 0)
            self.driveMotor.config_kI(slot, self.dIk, 0)
            self.driveMotor.config_kD(slot, self.dDk, 0)
            self.driveMotor.config_kF(slot, self.dFk, 0)
            self.driveMotor.config_IntegralZone(slot, self.dIZk, 0)

            self.turnMotor.config_kP(slot, self.tPk, 0)
            self.turnMotor.config_kI(slot, self.tIk, 0)
            self.turnMotor.config_kD(slot, self.tDk, 0)
            self.turnMotor.config_kF(slot, self.tFk, 0)
            self.turnMotor.config_IntegralZone(slot, self.tIZk, 0)