from .debuggablesubsystem import DebuggableSubsystem
import ports
from ctre import WPI_TalonSRX, ControlMode, FeedbackDevice

class Elevator(DebuggableSubsystem):
    '''For lifting and lowering elevator'''

    def __init__(self):
        super().__init__('Elevator')

        self.motor = WPI_TalonSRX(ports.elevator.motorID)
        self.motor.setSafetyEnabled(False)

        self.lowerlimit = 0
        self.upperlimit = 3000
        self.motor.configReverseSoftLimitEnable(True, 0)
