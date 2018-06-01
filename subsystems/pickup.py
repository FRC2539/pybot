from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX, ControlMode

import ports

class Pickup(Subsystem):
    '''
    A subsystem designed for picking up balls from the floor.
    '''

    def __init__(self):
        super().__init__('Pickup')

        self.motor = WPI_TalonSRX(ports.pickup.motorID)
        self.motor.setSafetyEnabled(False)
        self.motor.setNeutralMode(False)
        self.motor.setInverted(True)
        self.motor.set(ControlMode.PercentOutput, 0)


    def run(self, speed):
        self.motor.set(speed)


    def stop(self):
        self.motor.set(0)
