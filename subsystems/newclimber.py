from .debuggablesubsystem import DebuggableSubsystem

from rev import CANSparkMax, MotorType, ControlType

import ports

class NewClimber(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('NewClimber')

        self.climbMotor = CANSparkMax(ports.newclimber.motorID, MotorType.kBrushless)

        self.stopMotor = CANSparkMax(ports.newclimber.motorID, MotorType.kBrushed)

        self.climbMotor.setInverted(False)
        self.stopMotor.setInverted(False)

    def runUp(self):
        self.climbMotor.set(0.5)

    def pullUp(self):
        self.climbMotor.set(-0.6)

    def watchAmperage(self):
        return self.stopMotor.getOutputCurrent()

