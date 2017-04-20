from .debuggablesubsystem import DebuggableSubsystem
from wpilib.servo import Servo
from wpilib.relay import Relay
import ports

class Feeder(DebuggableSubsystem):
    '''
    A subsystem designed for feeding balls to the shooter.
    '''

    def __init__(self):
        super().__init__('Feeder')

        self.gate = Servo(ports.feeder.gateID)
        self.agitator = Relay(ports.shooter.agitatorPort)


    def open(self):
        self.gate.set(1)


    def close(self):
        self.gate.set(.8)


    def startAgitator(self):
        self.agitator.set(Relay.Value.kForward)


    def stopAgitator(self):
        self.agitator.set(Relay.Value.kOff)
