from .debuggablesubsystem import DebuggableSubsystem

from ctre import WPI_VictorSPX

from wpilib import I2C

import ports


class Turret(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Turret')
        self.motor = WPI_VictorSPX(ports.turret.motorID)
        self.motor.setSafetyEnabled(False)

        self.colorSensor = I2C(I2C.Port.kOnboard, 0x52)

        #self.colorSensor.write(0x00, b'000000011')

    def initSensor(self):
        self.colorSensor.write(0x00, b'000000011')

    def readSensor(self):
        return self.colorSensor.read(0x06, 3)

    def raiseTurret(self):
        self.motor.set(0.25)

    def lowerTurret(self):
        self.motor.set(-0.18)

    def slowRaise(self):
        self.motor.set(0.25)

    def slowLower(self):
        self.motor.set(-0.18)

    def stop(self):
        self.motor.set(0)
