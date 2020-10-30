from wpilib.command import Subsystem

from rev import CANSparkMax, MotorType, IdleMode

from .cougarsystem import  *

import ports

class Climber(Subsystem):
    '''Makes the climber move.'''

    def __init__(self):
        
        super().__init__('Climber')
        
        disablePrints()

        self.climberMotor = CANSparkMax(ports.climber.motorID, MotorType.kBrushless)
            
        self.climberMotor.setIdleMode(IdleMode.kBrake)
        self.climberMotor.setInverted(False)
    
    def raiseClimber(self):
       self.climberMotor.set(0.5)
    
    def lowerClimber(self):
       self.climberMotor.set(-0.5)
     
    def stopClimber(self):
       self.climberMotor.stopMotor()
    
