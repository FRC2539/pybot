from .debuggablesubsystem import DebuggableSubsystem
from rev import CANSparkMax, MotorType, ControlType
import ports
from wpilib import DigitalInput

import robot
from networktables import NetworkTables

class Arm(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Arm')

        self.motor = CANSparkMax(ports.arm.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.PIDController = self.motor.getPIDController()

        self.motor.setInverted(True)

        self.PIDController.setFF(0.5, 0)
        self.PIDController.setP(0.1, 0)
        self.PIDController.setI(0.001, 0)
        self.PIDController.setD(10, 0)
        self.PIDController.setIZone(3, 0)

        self.motor.setOpenLoopRampRate(0.4)
        self.motor.setClosedLoopRampRate(0.4)

        self.lowerLimit = DigitalInput(ports.arm.lowerLimit)

        self.upperLimit = 70.0
        self.startPos = 105.0

        self.encoder.setPositionConversionFactor(1)
        self.encoder.setPosition(self.startPos)

        #These are temporary and need to be finalized for competition.
        self.levels = {
                        'floor' : 0.0,
                        'aboveFloor' : 1.0,
                        'lowHatches' : 2.0,
                        'midHatches' : 37.0,
                        'highHatches' : 35.0,
                        'cargoBalls' : 55.0,
                        'lowBalls' : 70.0,
                        'midBalls' : 55.0,
                        'highBalls' : 70.0,
                        'start' : 90.0
                        }


    def up(self):

        print('ARM ' + str(self.getPosition()))

        isTop = self.getPosition() >= self.upperLimit

        if isTop:
            self.setPosition(float(self.upperLimit), 'down')
            self.stop()
        else:
            self.set(1)

        return isTop


    def down(self, speed=-1.0):
        print('ARM ' + str(self.getPosition()))
        isZero = not self.lowerLimit.get()

        if isZero:
            self.stop()
            self.resetEncoder()

        else:
            self.set(speed)

        return isZero


    def downSS(self):
        print("down ss")
        return self.down(-0.7)


    def forceDown(self):
        print('Force Down ' + str(self.getPosition()))


    def downNoZero(self, speed=-1.0):
        print('ARM ' + str(self.getPosition()))
        isZero = self.isAtZero()

        if isZero:
            self.stop()

        else:
            self.set(speed)

        return isZero


    def forceDown(self):

        if self.lowerLimit.get():
            self.set(-1)
        else:
            self.stop()
            self.resetEncoder()

        return self.lowerLimit.get()


    def forceUp(self):
        print('Force Up ' + str(self.getPosition()))
        isTop = self.getPosition() >= self.startPos
        if not isTop:
            self.set(1.0)
        else:
            self.stop()

        return isTop

    def stop(self):
        self.set(0.0)


    def hold(self):
        self.setPosition(self.getPosition())


    def set(self, speed):
        self.motor.set(float(speed))


    def resetEncoder(self):
        self.encoder.setPosition(0.0)


    def setPosition(self, target, upOrDown):
        position = self.getPosition()

        print("arm position target: " + str(target))

        if target > self.upperLimit or target < -3.5:
            self.stop()
            print('Illegal arm target position')
            return True

        elif upOrDown == 'up' and position < target:
            return self.up()

        elif upOrDown == 'down' and position > target:
            return self.downNoZero()

        else:
            self.stop()
            return True


    def getPosition(self):
        return self.encoder.getPosition()


    def isAtZero(self):
        return (not self.lowerLimit.get()) or (self.getPosition() <= 0.0)


    def goToLevel(self, level, upOrDown=''):
        return self.setPosition(float(self.levels[level]), upOrDown)


    def goToFloor(self):
        self.goToLevel('floor')


    def goToStartingPosition(self):
        self.goToLevel('start')
