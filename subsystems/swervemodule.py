from ctre import WPI_TalonFX, CANCoder, NeutralMode, TalonFXControlMode, TalonFXFeedbackDevice, AbsoluteSensorRange

class SwerveModule:
    
    def __init__(self, driveMotorID, turnMotorID, canCoderID): # Get the ports of the devices for a module.
        
        self.driveMotor = WPI_TalonFX(driveMotorID) # Declare and setup drive motor.
        
        self.driveMotor.setNeutralMode(NeutralMode.Brake)
        self.driveMotor.setSafetyEnabled(False)
        self.driveMotor.configSelectedFeedbackSensor(TalonFXFeedbackDevice.IntegratedSensor)
    
        self.dPk = 0.001
        self.dIk = 0
        self.dDk = 0
        self.dFk = 0
        self.dIZk = 0
    
        self.turnMotor = WPI_TalonFX(turnMotorID) # Declare and setup turn motor.
        
        self.turnMotor.setNeutralMode(NeutralMode.Brake)
        self.turnMotor.setSafetyEnabled(False)
        self.turnMotor.configSelectedFeedbackSensor(TalonFXFeedbackDevice.IntegratedSensor)
        
        self.tPk = 0.001
        self.tIk = 0
        self.tDk = 0
        self.tFk = 0
        self.tIZk = 0
        
        self.cancoder = CANCoder(canCoderID)
        self.cancoder.configAbsoluteSensorRange(AbsoluteSensorRange.Unsigned_0_to_360, 0)
        
    def getWheelAngle(self):
        '''
        Get wheel angle relative to the robot.
        '''
        return self.cancoder.getAbsolutePosition()
        
    def setWheelAngle(self, angle):
        '''
        This will set the angle of the wheel, relative to the robot. 
        0 degrees is facing forward. This will accept 0 - 360!
        '''
        self.turnMotor.set(ControlMode.Position, turn)
        
    def angleToTurnTicks(self, angle):
        pass
    
    def turnTicksToAngle(self, ticks):
        pass
    
    def inchesToDriveTicks(self, inches):
        pass
    
    def driveTicksToInches(self, ticks):
        pass
    
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
            
            
            
