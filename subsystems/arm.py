from .debuggablesubsystem import DebuggableSubsystem
from rev import CANSparkMax, MotorType, ControlType
import ports
from wpilib import DigitalInput


class Arm(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Arm')

        self.motor = CANSparkMax(ports.arm.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.PIDController = self.motor.getPIDController()

        self.motor.setInverted(True)

        self.motor.setOpenLoopRampRate(0.4)
        self.motor.setClosedLoopRampRate(0.4)

        self.lowerLimit = DigitalInput(ports.arm.lowerLimit)

        self.upperLimit = 90.0

        self.encoder.setPositionConversionFactor(1)
        self.encoder.setPosition(self.upperLimit)

        #These are temporary and need to be finalized for competition.
        self.levels = {
                        'floor' : 0,
                        'lowHatches' : -10,
                        'midHatches' : -20,
                        'highHatches' : -35,
                        'cargoBalls' : -55,
                        'lowBalls' : -75,
                        'midBalls' : -90,
                        'highBalls' : -100,
                        'start' : -105
                        }


    def up(self):
        isTop = self.getPosition() >= self.upperLimit

        if isTop:
            self.stop()
        else:
            self.set(1)

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
        self.PIDController.setReference(float(position), ControlType.kPosition)


    def getPosition(self):
        return self.encoder.getPosition()


    def isAtZero(self):
        return (not self.lowerLimit.get()) or (self.getPosition() <= 0)


    def goToLevel(self, level):
        self.setPosition(self.levels[level])


    def goToFloor(self):
        self.goToLevel('floor')


    def goToStartingPosition(self):
        self.goToLevel('start')
