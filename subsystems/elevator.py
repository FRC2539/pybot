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

        self.lowerLimit = DigitalInput(ports.elevator.lowerLimit)

        self.upperLimit = 150

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

        isTop = self.getPosition() + self.zero >= self.upperLimit

        if isTop:
            self.stop()
        else:
            self.set(1.0)
            #self.PIDController.setReference(4000, ControlType.kVelocity)

        return isTop

    def down(self):

        isZero = self.isAtZero()

        if isZero:
            self.stop()
            self.zero = self.getPosition()
        else:
            self.set(-1)


           #self.PIDController.setReference(-4000, ControlType.kVelocity)

        return isZero

    def stop(self):
        self.motor.disable()


    def hold(self):
        self.setPosition(self.getPosition())


    def set(self, speed):
        self.motor.set(speed)


    def setPosition(self, position):
        self.PIDController.setReference(position, ControlType.kPosition)


    def getPosition(self):
        return self.encoder.getPosition()


    def isAtZero(self):
        return not self.lowerLimit.get()


    def reZero(self):
        self.zero = self.getPosition()
        self.setPosition(self.zero)


    def goToLevel(self, level):
        self.setPosition(self.zero + self.levels[level])


    def goToFloor(self):
        self.goToLevel('floor')

    def panelEject(self):
        self.setPosition(float(self.getPosition()) - 0.1)
