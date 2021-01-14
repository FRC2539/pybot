from ctre import WPI_TalonFX, CANCoder, NeutralMode, TalonFXControlMode, \
FeedbackDevice, AbsoluteSensorRange, RemoteSensorSource

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
    
        self.dPk = 0.001 # P gain for the drive. 
        self.dIk = 0 # I gain for the drive
        self.dDk = 0 # D gain for the drive
        self.dFk = 0 # Feedforward gain for the drive
        self.dIZk = 0 # Integral Zone for the drive
        
        self.cancoder = CANCoder(canCoderID) # Declare and setup the remote encoder. 
        self.cancoder.configAbsoluteSensorRange(AbsoluteSensorRange.Signed_PlusMinus180, 0)
    
        self.turnMotor = WPI_TalonFX(turnMotorID) # Declare and setup turn motor.
        
        self.turnMotor.setNeutralMode(NeutralMode.Brake)
        self.turnMotor.setSafetyEnabled(False)
        self.turnMotor.configSelectedFeedbackSensor(FeedbackDevice.RemoteSensor0, 0, 0) # Set the feedback sensor as remote.
        self.turnMotor.configRemoteFeedbackFilter(canCoderID, RemoteSensorSource.CANCoder, 0, 0) # Configure and select CANCoder. 
        
        self.tPk = 0.001 # P gain for the turn.
        self.tIk = 0 # I gain for the turn.
        self.tDk = 0 # D gain for the turn.
        self.tFk = 0 # Feedforward gain for the turn.
        self.tIZk = 0 # Integral Zone for the turn.
        
        self.driveMotorGearRatio = 6.86 # 6.86 motor rotations per wheel rotation.
        
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
        pass
    
    def driveTicksToInches(self, ticks):
        pass
    
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