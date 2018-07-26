from .debuggablesubsystem import DebuggableSubsystem

import ports
from ctre import WPI_TalonSRX


class Climbhook(DebuggableSubsystem):
    '''Make the robot talk'''

    def __init__(self):
        super().__init__('Climbhook')

        self.hook = WPI_TalonSRX(ports.climbhook.hookMotor)
        self.hook.setSafetyEnabled(False)

    def moveHook(self, speed=1):
        self.hook.set(speed)
