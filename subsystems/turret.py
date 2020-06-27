from .debuggablesubsystem import *

import wpilib

from wpilib.controller import PIDController

import ports
from ctre import ControlMode, FeedbackDevice, WPI_TalonSRX, NeutralMode

from networktables import NetworkTables as nt

import robot
import math

class Turret(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Turret')
        self.motor = WPI_TalonSRX(ports.turret.motorID)
        self.motor.config_kP(0, 1, 0)
        self.motor.config_kI(0, 0, 0)
        self.motor.config_kD(0, 0.001, 0)
        self.motor.config_kF(0, 0, 0)

        self.max = 1275# Dummy values
        self.min = 0 # Dummy values

        self.table = nt.getTable('Turret')

        self.limitSwitch = wpilib.DigitalInput(ports.turret.limitSwitch)

        self.fieldAngle = 860

        self.motor.setNeutralMode(NeutralMode.Brake)

        self.tollerance = 5 # ticks

        self.motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder)
        #self.motor.setSelectedSensorPosition(0, 0, 0)

    def rotateClockwise(self, val):
        if self.getPosition() < self.max and self.getPosition() > self.min:
            self.motor.set(val)
            return False
        else:
            self.stop()

    def move(self, val):
        self.updateNetworkTables()
        if self.isZeroed() and val > 0:
            self.stop() # does not let a positive direction proceed if zeroed.
        elif self.getPosition() >= self.max and val < 0:
            self.stop() # does not let a negative direction proceed if maxed.
        else:
            self.motor.set(val)

    def testMove(self, val):
        print('here')
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

    def stop(self):
        self.motor.stopMotor()

    def givePosition(self):
        self.motor.setSelectedSensorPosition(1500)

    def returnZero(self):
        self.motor.set(ControlMode.Position, 0)

    def captureOrientation(self):
        self.fieldAngle = robot.drivetrain.getAngle()

    def turretFieldOriented(self): # Use for when traveling 'round the field.
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

    def outOfRange(self):
        print('ma ' + str(self.getPosition() > self.max))
        print('mi ' + str(self.getPosition() < self.min) + str(self.getPosition()))
        return False#(self.getPosition() > self.max) or (self.getPosition() < self.min)

    def getPosition(self):
        return (self.motor.getSelectedSensorPosition(0))

    def setZero(self):
        self.motor.setSelectedSensorPosition(0, 0, 0)

    def isZeroed(self):
        if not self.limitSwitch.get():
            self.stop()
            self.setZero()
            return True

        return False

    def followTargetPID(self, newPosition):
        pos = self.clampYaBoi(newPosition)

        self.motor.set(ControlMode.Position, pos)

    def followTarget(self, diff, dist):

        val = abs(diff / 275)

        distMod = 0

        if abs(dist) > 120:
            distMod = abs((dist - 120) / 500) # We want to make the sign opposite of diff so we can combine them.

        print('out ' + str(math.copysign(val - distMod, -diff)))

        self.motor.set(math.copysign(val - distMod, -diff))

    def moveFieldAngle(self, val):
        self.fieldAngle = self.fieldAngle + (val * 1)

    def isMax(self):
        if (self.getPosition() >= self.max):
            return True
        else:
            return False

    def initDefaultCommand(self):
        '''
        By default, unless another command is running that requires this
        subsystem, we will drive via joystick using the max speed stored in
        Config.
        '''
        from commands.turret.turretmovecommand import TurretMoveCommand
        from commands.turret.fieldcommandgroup import FieldCommandGroup

        self.setDefaultCommand(TurretMoveCommand())

    def clampYaBoi(self, number):
        return max(min(self.max, number), self.min)

