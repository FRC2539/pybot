from .debuggablesubsystem import DebuggableSubsystem
from wpilib.solenoid import Solenoid
from wpilib.compressor import Compressor

import ports


class Pneumatics(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Pneumatics')

        compressor = Compressor(0)
        compressor.setClosedLoopControl(True);

        self.solenoid1 = Solenoid(0)
        self.solenoid2 = Solenoid(1)

        self.solenoid1.set(False)
        self.solenoid2.set(True)

    def toggle(self):
        if(self.solenoid1.get()):
            self.solenoid1.set(False)
            self.solenoid2.set(True)
        else:
            self.solenoid2.set(False)
            self.solenoid1.set(True)

    def hold(self):
        if(self.solenoid1.get()):
            self.solenoid1.set(False)
            self.solenoid2.set(True)
        else:
            self.solenoid1.set(True)
            self.solenoid2.set(False)
