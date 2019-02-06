from .debuggablesubsystem import DebuggableSubsystem
from rev import CANSparkMax, MotorType, ControlType
from wpilib import DigitalInput

import ports


class Elevator(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Elevator')

        self.motor = CANSparkMax(ports.elevator.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.PIDController = self.motor.getPIDController()

        self.limit = DigitalInput(ports.elevator.limit)

        self.zero = 0

        #These are temporary and need to be finalized for competition.
        self.levels = {
                        'floor' : 0,
                        'lowHatches' : 2000,
                        'midHatches' : 4000,
                        'highHatches' : 6000,
                        'cargoBalls' : 3000,
                        'lowBalls' : 2500,
                        'midBalls' : 4500,
                        'highBalls' : 6500
                        }


    def up(self):
        self.set(0.5)


    def down(self):
        self.set(-0.5)
        isZero = self.isAtZero()
        if isZero:
            self.zero = self.getPosition()
        return isZero


    def stop(self):
        self.setPosition(self.getPosition())


    def set(self, speed):
        self.motor.set(speed)


    def setPosition(self, position):
        self.PIDController.setReference(float(position), ControlType.kPosition)


    def getPosition(self):
        return self.encoder.getPosition()


    def isAtZero(self):
        return not self.limit.get()


    def reZero(self):
        self.zero = self.getPosition()
        self.setPosition(self.zero)


    def goToLevel(self, level):
        self.setPosition(self.levels[level])
