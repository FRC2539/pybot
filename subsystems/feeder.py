from wpilib.command.subsystem import Subsystem
from wpilib.servo import Servo
from wpilib.relay import Relay
import ports

class Feeder(Subsystem):
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

    def isClosed(self):
        return self.gate.get() > .9 or self.gate.get() < .7

    def initDefaultCommand(self):
        '''
        By default, unless another command is running that requires this
        subsystem, we will drive via joystick using the max speed stored in
        Config.
        '''
        from commands.shooter.stayclosedcommand import StayClosedCommand

        self.setDefaultCommand(StayClosedCommand())

    def startAgitator(self):
        self.agitator.set(Relay.Value.kForward)


    def stopAgitator(self):
        self.agitator.set(Relay.Value.kOff)
