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

        self.motor.setOpenLoopRampRate(0.4)
        self.motor.setClosedLoopRampRate(0.4)

        self.lowerLimit = DigitalInput(ports.elevator.lowerLimit)

        self.upperLimit = 150.0

        self.encoder.setPositionConversionFactor(1)
        self.encoder.setPosition(0.0)


        #These are temporary and need to be finalized for competition.
        self.levels = {
                        'floor' : 0.0,
                        'lowHatches' : 2.0,
                        'midHatches' : 4.0,
                        'highHatches' : 6.0,
                        'cargoBalls' : 8.0,
                        'lowBalls' : 10.0,
                        'midBalls' : 12.0,
                        'highBalls' : 13.0
                        }


    def up(self):
        isTop = (self.getPosition() >= self.upperLimit)

        if isTop:
            self.stop()
        else:
            self.set(1.0)

        return isTop


    def down(self):
        isZero = self.isAtZero()

        if isZero:
            self.stop()
            self.resetEncoder()
        else:
            self.set(-1)

        return isZero


    def stop(self):
        self.motor.disable()


    def hold(self):
        self.setPosition(self.getPosition())


    def set(self, speed):
        self.motor.set(speed)


    def resetEncoder(self):
        self.encoder.setPosition(0.0)


    def setPosition(self, position):
        self.PIDController.setReference(position, ControlType.kPosition)


    def getPosition(self):
        return self.encoder.getPosition()


    def isAtZero(self):
        return (self.getPosition() <= 0.0) or (not self.lowerLimit.get())


    def goToLevel(self, level):
        self.setPosition(self.levels[level])


    def goToFloor(self):
        self.goToLevel('floor')


    def panelEject(self):
        if not (self.getPosition() < 0.1):
            self.setPosition(float(self.getPosition()) - 0.1)
