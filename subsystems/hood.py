from .debuggablesubsystem import DebuggableSubsystem

import ports
import wpilib

from rev import CANSparkMax, MotorType, ControlType
from custom.config import Config

from networktables import NetworkTables as nt

class Hood(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Hood')

        self.motor = CANSparkMax(ports.hood.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.controller = self.motor.getPIDController()

        self.table = nt.getTable('Hood')

        #self.controller.setFF(0.00019, 0)
        #self.controller.setP(0.0001, 0)
        #self.controller.setI(0, 0)
        #self.controller.setD(0.001, 0)
        #self.controller.setIZone(0, 0)

        source_ = wpilib.DigitalInput(9)
        self.tbEnc = wpilib.DutyCycle(source_)

        self.dir = 'u'
        self.setSpeed = 0.3

        self.angleMax = 155.00 # NOTE DO not actually make this 0 and 90. Place-holder only; make like 20, 110
        self.angleMin = 85.00

        self.zeroNetworkTables()

    def getPosition(self):
        return self.tbEnc.getOutput() * 360

    def stopHood(self):
        self.motor.stopMotor()

    def setPercent(self, speed):
        self.motor.set(speed)

    def raiseHood(self):
        if self.getPosition() < self.angleMax:
            self.motor.set(0.4)
        else:
            self.motor.stopMotor()

    def lowerHood(self):
        if self.getPosition() > self.angleMin:
            self.motor.set(-0.4)
        else:
            self.motor.stopMotor()

    def atHighest(self):
        if self.getPosition() >= self.angleMax:
            self.motor.stopMotor()
            return True
        else:
            return False

    def atLowest(self):
        if self.getPosition() <=  self.angleMin:
            self.motor.stopMotor()
            return True
        else:
            return False

    def updateNetworkTables(self, angle=85.00):
        self.table.putNumber('HoodAngle', round(self.getPosition(), 2))
        self.table.putNumber('DesiredHoodAngle', round(angle, 2))

    def zeroNetworkTables(self):
        self.table.putNumber('HoodAngle', self.angleMin)
        self.table.putNumber('DesiredHoodAngle', self.angleMin)

    def initializeSetPosition(self, angle):
        self.angle = angle

        if self.getPosition() >= self.angle:
            self.setSpeed = -0.3
            self.dir = 'd'
            self.angle += 5 # compensating for gear lash
        else:
            self.setSpeed = 0.3
            self.dir = 'u'
            self.angle -= 5

        print(self.dir)
        if abs(self.getPosition() - self.angle) < 1:
            self.stopHood()

        else:
            self.setPercent((self.setSpeed))

    def executeSetPosition(self):
        if (self.getPosition() <= self.angle and self.dir == 'd') or (self.getPosition() >= self.angle and self.dir == 'u'):
            self.stopHood()
        else:
            self.setPercent((self.setSpeed))

    def isFinishedSetPosition(self):
        if abs(self.getPosition() - self.angle) <= 1:
            return True

        return False

    def endSetPosition(self):
        self.stopHood()
        self.updateNetworkTables()


    def OpenLoopSetPos(self, pos):
        self.angle = pos # give it in terms between min and max as of now, add 85 onto an angle between 0 and 35,
        # multiply that by 2: 85 + (2 * x). THIS WILL WORK
        if abs(self.getPosition() - self.angle) >= 2: # this way is better, angle will not be negative. 2 degrees of play
            self.rotate = .005 * (self.angle - self.getPosition()) # this should work
            self.setPercent(self.rotate)
        else:
            self.stopHood()
