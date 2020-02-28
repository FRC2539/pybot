from .debuggablesubsystem import DebuggableSubsystem

from rev import CANSparkMax, MotorType, IdleMode

import ports

class Climber(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Climber')

        self.climberMotor = CANSparkMax(ports.climber.motorID, MotorType.kBrushless)

        self.climberMotor.setIdleMode(IdleMode.kBrake)
        self.climberMotor.setInverted(False)

        self.climberMotor.burnFlash()

    def raiseClimber(self):
        self.climberMotor.set(0.12)

    def elevateClimber(self):
        self.climberMotor.set(0.25)

    def lowerClimber(self):
        self.climberMotor.set(-0.25)

    def stop(self):
        self.climberMotor.stopMotor()
