from .debuggablesubsystem import DebuggableSubsystem
from rev import CANSparkMax, MotorType, ControlType, ConfigParameter
from wpilib import DigitalInput

from custom.config import Config
from networktables import NetworkTables

import ports
import robot

class Elevator(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Elevator')

        NetworkTables.initialize(server='10.25.39.2')
        self.Elevator = NetworkTables.getTable('Elevator')

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

        self.upperLimit = DigitalInput(ports.elevator.upperLimit)

        self.encoder.setPositionConversionFactor(1)
        self.encoder.setPosition(0.0)

        #These are temporary and need to be finalized for DEFENSE COMPETITION.
        self.levels = {
                        'floor' : 0.0,
                        'cargoBalls' : 10.2,
                        'lowBalls' : 5.0
                        }

    def forceDown(self):
        self.set(-1.0)


    def up(self):
        isTop = not self.upperLimit.get()

        if isTop:
            self.stop()
            print('at Top')
        else:
            if self.getPosition() >= 60.0:
                self.set(0.3)
            else:
                self.set(0.9)

        print(self.getPosition())

        return isTop


    def down(self):
        isZero = self.isAtZero()

        print(self.getPosition())

        if isZero:
            self.stop()
            self.resetEncoder()

        else:
            if self.getPosition() <= 40.0:
                self.set(-0.3)
            else:
                self.set(-0.7)

        return isZero

    def downReset(self):
        isZero = self.isAtZero()

        print(self.getPosition())

        if isZero:
            self.stop()
            self.resetEncoder()

        else:
            if self.getPosition() > 10.0:
                self.set(-0.7)
            else:
                self.set(-0.3)

        return isZero

    def stop(self):
        self.motor.set(0.0)


    def upOneFoot(self):
        currentPos = self.encoder.getPosition()
        self.encoder.setPosition(float(currentPos + 10.0))
        print('\nDONE\n')

    def hold(self):
        self.setPosition(self.getPosition())


    def set(self, speed):
        self.motor.set(speed)


    def resetEncoder(self):
        self.encoder.setPosition(0.0)


    def setPosition(self, target):
        position = self.getPosition()

        print("elevator position target: " + str(target))

        if not self.upperLimit.get() or target < 0.0:
            self.stop()
            print('Illegal elevator target position')
            return True

        elif position < target:
            return self.up()

        elif position > target:
            return self.down()

        else:
            self.stop()
            return True


    def getPosition(self):
        return self.encoder.getPosition()


    def isAtZero(self):
        print(str(self.lowerLimit.get()))
        return (self.getPosition() <= 0.0) or (not self.lowerLimit.get())


    def goToLevel(self, level):
        return self.setPosition(float(self.levels[level]))


    def goToFloor(self):
        self.goToLevel('floor')

    def elevatorIsHigh(self):
        self.high = False
        if (robot.elevator.getPosition() > 5) :
            self.high = True
        return self.high


    def panelEject(self):
        if not (self.getPosition() < 0.1):
            self.setPosition(float(self.getPosition()) - 0.1)
