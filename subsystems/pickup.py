from .debuggablesubsystem import DebuggableSubsystem
from ctre import CANTalon

import ports

class Pickup(DebuggableSubsystem):
    '''
    A subsystem designed for picking up balls from the floor.
    '''

    def __init__(self):
        super().__init__('Pickup')

        self.motor = CANTalon(ports.pickup.motorID)
        self.motor.setSafetyEnabled(False)
        self.motor.enableBrakeMode(False)
        self.motor.setInverted(True)
        self. motor.setControlMode(CANTalon.ControlMode.PercentVbus)


    def run(self, speed):
        self.motor.set(speed)


    def stop(self):
        self.motor.set(0)
