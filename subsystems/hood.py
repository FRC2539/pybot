from .debuggablesubsystem import DebuggableSubsystem

from rev import CANSparkMax, MotorType, ControlType

import ports


class Hood(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Hood')

        self.hoodMotor = CANSparkMax(ports.hood.hoodMotorID, MotorType.kBrushless)
        self.hoodController = self.hoodMotor.getPIDController()
        self.hoodEncoder = self.hoodMotor.getEncoder()

        self.hoodMotor.setInverted(True) # Might be incorrect, wait for model.


    def stop(self):
        self.hoodMotor.stopMotor()



