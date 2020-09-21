from .cougarsystem import *

import wpilib

from wpilib.command import Subsystem
from wpilib.controller import PIDController

import ports
from ctre import ControlMode, FeedbackDevice, WPI_TalonSRX, NeutralMode

from networktables import NetworkTables as nt

import robot
import math

class Turret(CougarSystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Turret')
        self.motor = WPI_TalonSRX(ports.turret.motorID)
        self.motor.config_kP(0, 3.9, 0)
        self.motor.config_kI(0, 0, 0)
        self.motor.config_kD(0, 30, 0)
        self.motor.config_kF(0, 0.07, 0)

        self.max = 1365 # Max value
        self.middle = 957.5
        self.min = 650.0 # Min value

        self.turretActiveMode = True
        self.onTarget = False

        self.turretDeadband = 0.1

        self.table = nt.getTable('Turret')

        self.limitSwitch = wpilib.DigitalInput(ports.turret.limitSwitch)

        self.fieldAngle = 860

        self.motor.setNeutralMode(NeutralMode.Brake)

        self.tollerance = 5 # ticks

        self.motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder)

        self.adjustment = 0

        disablePrints()

        #self.capture('position', 'getPosition')

        #print('\n\n received ' + str(self.get('position', 'ewwwwwwww')) + '\n\n')

        #self.motor.setSelectedSensorPosition(self.get('position', 0.0), 0, 0)
        self.motor.setSelectedSensorPosition(0, 0, 0)
    def rotateClockwise(self, val):
        if self.getPosition() < self.max and self.getPosition() > self.min:
            self.motor.set(val)
            return False
        else:
            self.stop()

    def increaseAdjustment(self, val):
        self.adjustment = self.adjustment - val

    def decreaseAdjustment(self, val):
        self.adjustment = self.adjustment + val

    def setAdjustment(self, val):
        self.adjustment = val

    def getAdjustment(self):
        return self.adjustment

    def move(self, val):
        if self.isMin() and val < 0:
            self.stop() # does not let a positive direction proceed if zeroed.
        elif self.isMax() and val > 0:
            self.stop() # does not let a negative direction proceed if maxed.
        else:
            self.motor.set(val)

    def testMove(self, val): # Don't use this.
        self.updateNetworkTables()
        if (self.getPosition() < self.max - self.getPosition()):
            self.speedLimit = self.getPosition() * .0015
        else:
            self.speedLimit = (self.max- self.getPosition()) * .0015

        self.speedLimit = max([.2, self.speedLimit])

        #if self.speedLimit > .4:
            #self.speedLimit = .4

        val = val * self.speedLimit

        if self.isZeroed() and val > 0:
            self.stop() # does not let a positive direction proceed if zeroed.
        elif self.getPosition() >= self.max and val < 0:
            self.stop() # does not let a negative direction proceed if maxed.
        else:
            self.motor.set(val)

    def accelMove(self, direction):
        direction = math.copysign(max(abs(direction) - self.turretDeadband, 0), direction)

        if direction != 0.0:

            speed = 0.5 - (abs(self.getPosition() - self.middle) / self.max)

            self.motor.set(ControlMode.PercentOutput, math.copysign(max(min(0.6, abs(speed)), 0.1), direction))

        else:
            self.stop()

    def stop(self):
        self.motor.stopMotor()

    def givePosition(self):
        self.motor.setSelectedSensorPosition(1500)

    def returnToZero(self):
        self.motor.set(ControlMode.Position, self.min)

    def captureOrientation(self):
        self.fieldAngle = robot.drivetrain.getAngle()

    def turretFieldOriented(self): # Use for when traveling round the field.
        if self.getFieldPosition() > 25 and self.getFieldPosition() < self.max - 25 :
            self.setPosition(self.getFieldPosition())
        else:
            self.stop()

    def getFieldPosition(self):
        self.degrees = robot.drivetrain.getAngle()
        #print(self.degrees)
        self.ticks = -1*((self.degrees)*4096)/360 + self.fieldAngle
        if self.ticks < 0 :
            self.ticks = self.ticks + 4096
        if self.ticks > 4096:
            self.ticks = self.ticks - 4096
        return self.ticks

    def setPosition(self, position):
        self.error = self.getPosition() - position
        self.rotate = self.error * 0.00075
        #if abs(self.rotate) > .5:
            #self.rotate = math.copysign(.5, self.rotate)
        self.testMove(self.rotate)
        if self.getPosition() > position - self.tollerance and self.getPosition() < position + self.tollerance:
            return True
        else:
            return False

    def updateNetworkTables(self, angle=85.00):
        self.table.putNumber('TurretPosition', round(self.motor.getSelectedSensorPosition(0), 2))
        self.table.putNumber('TurretAdjustment', round(self.adjustment, 2))

    def outOfRange(self):
        return (self.getPosition() > self.max) or (self.getPosition() < self.min)

    def getPosition(self):
        return self.motor.getSelectedSensorPosition(0)

    def setMax(self):
        self.motor.setSelectedSensorPosition(self.max, 0, 0)

    def simpleMove(self, x):
        self.motor.set(ControlMode.PercentOutput, math.copysign(min([abs(x), 0.4]), x))

    def isLimitSwitch(self): # Limit switch is at the upper end.
        if not self.limitSwitch.get() or self.getPosition() >= self.max + 10:
            self.stop()
            self.setMax()
            return True

        return False

    def followTargetPID(self, newPosition):
        pos = self.clampYaBoi(newPosition)

        self.motor.set(ControlMode.Position, pos)

    def moveFieldAngle(self, val):
        self.fieldAngle = self.fieldAngle + (val * 1)

    def isMax(self):
        return self.getPosition() >= self.max

    def isMin(self):
        return self.getPosition() <= self.min + 12

    def initDefaultCommand(self):
        '''
        By default, unless another command is running that requires this
        subsystem, we will drive via joystick using the max speed stored in
        Config.
        '''
        from commands.turret.turretmovecommand import TurretMoveCommand

        self.setDefaultCommand(TurretMoveCommand())

    def clampYaBoi(self, number):
        return max(min(self.max, number), self.min)

