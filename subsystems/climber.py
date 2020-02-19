from .debuggablesubsystem import DebuggableSubsystem

from rev import ControlType, MotorType, CANSparkMax, IdleMode

import ports


class Climber(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Climber')

        self.winchMotor = CANSparkMax(ports.climber.motorID, MotorType.kBrushless)
        self.winchController = self.winchMotor.getPIDController()
        self.winchEncoder = self.winchMotor.getEncoder()

        self.winchMotor.setIdleMode(IdleMode.kBrake)

        self.winchMotor.setInverted(False)

    def retract(self): # 'pull' up.
        self.winchMotor.set(0.8)

    def loosen(self):
        self.winchMotor.set(-0.8)

    def slowRetract(self):
        self.winchMotor.set(0.4)
