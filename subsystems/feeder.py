from .debuggablesubsystem import DebuggableSubsystem
from wpilib.servo import Servo
import ports

class Feeder(DebuggableSubsystem):
    '''
    A subsystem designed for feeding balls to the shooter.
    '''

    def __init__(self):
        super().__init__('Feeder')

        self.gate = Servo(ports.feeder.gateID)


    def open(self):
        self.gate.set(1)


    def close(self):
        self.gate.set(.8)
