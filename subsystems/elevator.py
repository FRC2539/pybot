from .debuggablesubsystem import DebuggableSubsystem
from rev import CANSparkMax, MotorType, ControlType

import ports


class Elevator(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Elevator')

        self.motor = CANSparkMax(ports.elevator.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.PIDController = self.motor.getPIDController()

        self.encoderOffset = 0

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


    def stop(self):
        self.setPosition(self.getPosition())

    def set(self, speed):
        self.motor.set(speed)


    def setPosition(self, position):
        self.PIDController.setReference(float(position), ControlType.kPosition)


    def getPosition(self):
        return self.encoder.getPosition()


    def setZero(self):
        self.encoderOffset = self.getPosition()
        self.setPosition(self.encoderOffset)


    def goToLevel(self, level):
        self.setPosition(self.levels[level])
