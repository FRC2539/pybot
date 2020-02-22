from .debuggablesubsystem import DebuggableSubsystem
from wpilib import Timer

from rev import CANSparkMax, MotorType

import ports

class WindshieldWiper(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('WindshieldWiper')

        self.wwMotor = CANSparkMax(ports.windshieldwiper.motorID, MotorType.kBrushed)

        self.wwMotor.setInverted(False)

        self.timer = Timer()
        self.timer.reset()

        self.direction = 1 # 1 is forward, -1 is reverse (or should be)

        self.wwMotor.burnFlash()

    def fastWipe(self):
        self.wwMotor.set(0.5 * self.direction)

    def fastReverse(self):
        self.wwMotor.set(-0.3)

    def slowWipe(self):
        self.wwMotor.set(0.1 * self.direction)

    def swapDirection(self):
        print('switched')
        self.direction *= -1

    def getAmperage(self):
        return self.wwMotor.getOutputCurrent()

    def stop(self):
        self.wwMotor.stopMotor()

    def startTimer(self):
        self.timer.start()

    def stopTimer(self):
        self.timer.stop()

    def resetTimer(self):
        self.timer.reset()

    def getTime(self):
        return self.timer.get()
