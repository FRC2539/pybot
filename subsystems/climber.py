from .debuggablesubsystem import *

from wpilib import Timer

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

        self.timer = Timer()

    def raiseClimber(self):
        self.climberMotor.set(0.12)

    def elevateClimber(self):
        self.climberMotor.set(0.25)

    def lowerClimber(self):
        self.climberMotor.set(-0.4)

    def stop(self):
        self.climberMotor.stopMotor()

    def instantiateTime(self):
        self.timer.start()

    def stopTimer(self):
        self.timer.stop()
        self.timer.reset()

    def isClimbLegal(self):
        if self.timer.getMatchTime() <= 30: # climbs only if there is 30 or less seconds.
            return True
        return False
