from .debuggablesubsystem import DebuggableSubsystem
from rev import CANSparkMax, MotorType, ControlType, ConfigParameter
from wpilib import DigitalInput

import ports


class Elevator(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Elevator')

        self.motor = CANSparkMax(ports.elevator.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.PIDController = self.motor.getPIDController()

        self.PIDController.setFF(0.5, 0)
        self.PIDController.setP(0.1, 0)
        self.PIDController.setI(0.001, 0)
        self.PIDController.setD(20, 0)
        self.PIDController.setIZone(3, 0)

        self.motor.setOpenLoopRampRate(0.6)
        self.motor.setClosedLoopRampRate(0.6)


        self.lowerLimit = DigitalInput(ports.elevator.lowerLimit)

        self.upperLimit = 135.0

        self.encoder.setPositionConversionFactor(1)
        self.encoder.setPosition(0.0)

        #These are temporary and need to be finalized for competition.
        self.levels = {
                        'floor' : 0.0,
                        'aboveFloor' : 0.0,
                        'lowHatches' : 0.0,
                        'midHatches' : 65.0,
                        'highHatches' : 130.0,
                        'cargoBalls' : 50.0,
                        'lowBalls' : 0.0,
                        'midBalls' : 90.0,
                        'highBalls' : 135.0,
                        'start' : 0.0
                        }


    def up(self):
        isTop = self.getPosition() >= self.upperLimit
        print('Elevator ' + str(self.getPosition()))

        if isTop:
            self.stop()
        else:
            self.set(1.0)

        return isTop

    def down(self):
        isZero = self.isAtZero()
        print('Elevator ' + str(self.getPosition()))

        if isZero:
            self.stop()
            self.resetEncoder()
        else:
            self.set(-1.0)

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
        self.PIDController.setReference(position, ControlType.kPosition, 0, 0)


    def getPosition(self):
        return self.encoder.getPosition()


    def isAtZero(self):
        return (self.getPosition() <= 0.0) or (not self.lowerLimit.get())


    def goToLevel(self, level):
        self.setPosition(float(self.levels[level]))
        return float(self.levels[level])


    def goToFloor(self):
        self.goToLevel('floor')


    def panelEject(self):
        if not (self.getPosition() < 0.1):
            self.setPosition(float(self.getPosition()) - 0.1)
