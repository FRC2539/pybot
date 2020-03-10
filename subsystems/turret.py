from .debuggablesubsystem import DebuggableSubsystem

import wpilib

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
        self.motor.config_kP(0, 0.0001, 0)
        self.motor.config_kI(0, 0, 0)
        self.motor.config_kD(0, 0.001, 0)
        self.motor.config_kF(0, 0.00019, 0)
        #self.motor.config_IntegralZone(0, 0, 0)
        self.max = 2150# Dummy values
        self.min = 0 # Dummy values

        self.table = nt.getTable('Turret')

        self.limitSwitch = wpilib.DigitalInput(ports.turret.limitSwitch)

        self.fieldAngle = 100

        self.motor.setNeutralMode(NeutralMode.Brake)


        self.motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder)
        self.motor.setSelectedSensorPosition(1061, 0, 0) #1061 starting position
        #self.motor.setPulseWidthPosition(0, 0)  # NOTE: Temporary reset at beginning in attmept to zero the sensor.

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
        self.updateNetworkTables()
        if (self.getPosition() < self.max - self.getPosition()):
            self.speedLimit = self.getPosition() * .0015
        else:
            self.speedLimit = (self.max- self.getPosition()) * .0015

        if self.speedLimit < .2:
            self.speedLimit = .2

        if self.speedLimit > .4:
            self.speedLimit = .4

        if abs(val) > self.speedLimit :
            val = math.copysign(self.speedLimit, val)

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
        if self.getFieldPosition() > 25 and self.getFieldPosition() < 2150 :
            self.setPosition(self.getFieldPosition())
        else:
            self.stop()
            #if self.getFieldPosition() > self.getFieldPosition() - 2150 :
                #self.setPosition(25)
            #elif self.getFieldPosition() < self.getFieldPosition() - 2150:
                #self.setPosition(2150)
            #else:
                #self.stop

    def getFieldPosition(self):
        self.degrees = robot.drivetrain.getAngle()
        print(self.degrees)
        self.ticks = ((180-self.degrees)*4096)/360 + self.fieldAngle
        if self.ticks < 0 :
            self.ticks = self.ticks + 4096
        return self.ticks

    def setPosition(self, position):
        self.error = self.getPosition() - position
        self.rotate = self.error * 0.00075
        #if abs(self.rotate) > .5:
            #self.rotate = math.copysign(.5, self.rotate)
        self.testMove(self.rotate)
        print('rotate: '+ str(self.rotate))



    def printPosition(self):
        #print(str(self.motor.getSelectedSensorPosition(0)))
        pass

    def updateNetworkTables(self, angle=85.00):
        self.table.putNumber('TurretPosition', round(self.motor.getSelectedSensorPosition(0), 2))

    def getPosition(self):
        #return (self.motor.getSelectedSensorPosition(0) % 360)
        return (self.motor.getSelectedSensorPosition(0))

    #def setZero(self):
        #self.zero = self.getPosition() % 360 # keeps below 360 degrees
        #if self.zero > 180:
            #self.zero = (self.zero - 180) * -1 # sets a zero between -180 and 180. IT WORKS.

    def setZero(self):
        self.motor.setSelectedSensorPosition(0, 0, 0)

    def isZeroed(self):
        if not self.limitSwitch.get():
            self.stop()
            self.setZero()
            return True

        return False

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


