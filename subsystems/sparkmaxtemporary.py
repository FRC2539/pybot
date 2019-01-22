from .debuggablesubsystem import DebuggableSubsystem
from rev import CANSparkMax, MotorType

import ports


class SparkMaxTemporary(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('SparkMaxTemporary')

        self.neo1 = CANSparkMax(ports.sparkmaxtemporary.neo1, MotorType.kBrushless)
        self.neo2 = CANSparkMax(ports.sparkmaxtemporary.neo2, MotorType.kBrushless)

        #self.neo1.setIdleMode(IdleMode.kCoast)
        #self.neo2.setIdleMode(IdleMode.kCoast)


    def set(self, output):
        self.neo1.set(output)
        self.neo2.set(output)

    def get(self):
        return self.neo1.getEncoder().getVelocity(), self.neo2.getEncoder().getVelocity()

    def stop(self):
        self.neo1.disable()
        self.neo2.disable()
