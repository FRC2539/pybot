from .debuggablesubsystem import DebuggableSubsystem
from ctre import CANTalon
from wpilib.digitalinput import DigitalInput

import ports

class Climber(DebuggableSubsystem):
    '''
    A subsystem designed to climb a rope.
    '''

    def __init__(self):
        super().__init__('Climber')

        self.motor = CANTalon(ports.climber.motorID)
        self.motor.enableBrakeMode(True)
        self.motor.setSafetyEnabled(False)
        self.motor.setControlMode(CANTalon.ControlMode.PercentVbus)
        self.sensor = DigitalInput(ports.climber.sensorID)


    def start(self):
        self.motor.set(1)


    def stop(self):
        self.motor.set(0)


    def atTop(self):
        return False
        #if self.sensor.get() == False:
        #   return False
        #else:
        #  return True
