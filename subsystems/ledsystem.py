from wpilib.command import Subsystem

from .debuggablesubsystem import DebuggableSubsystem

from wpilib import Spark

import ports


class LEDSystem(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('LEDSystem')

        self.blinkin = Spark(ports.ledsystem.controllerID)
        self.onTarget = False

        self.setOrange()

    def turnOff(self):
        self.blinkin.set(0.99)

    def setRed(self):
        self.blinkin.set(0.61)

    def setGold(self):
        self.blinkin.set(0.67)

    def setBlue(self):
        self.blinkin.set(0.87)

    def setOrange(self):
        self.blinkin.set(0.63) # does not look like orange lol

    def setGreen(self):
        self.blinkin.set(0.77)

    def flashRed(self):
        self.blinkin.set(-0.11)

    def flashWhite(self):
        self.blinkin.set(-0.05)

    def rainbowLava(self):
        self.blinkin.set(-0.93)

    def setPurple(self):
        self.blinkin.set(0.91)
