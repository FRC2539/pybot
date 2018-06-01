from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX, TalonSRX, ControlMode
from wpilib.digitalinput import DigitalInput

import ports

class Climber(Subsystem):
    '''
    A subsystem designed to climb a rope.
    '''

    def __init__(self):
        super().__init__('Climber')

        self.motor = WPI_TalonSRX(ports.climber.motorID)
        self.motor.setNeutralMode(True)
        self.motor.setSafetyEnabled(False)
        self.motor.set(ControlMode.PercentOutput, 0)


    def start(self):
        self.motor.set(1)


    def stop(self):
        self.motor.set(0)


    def atTop(self):
        return False
