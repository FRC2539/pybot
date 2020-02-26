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

        self.fieldAngle = 0

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

            #self.speed = val * 1
            #if self.getPosition() < self.max and self.getPosition() > self.min:
                #self.motor.set(ControlMode.PercentOutput, self.speed)
            #elif self.getPosition() > self.max and val > 0:
                ##self.motor.set(ControlMode.PercentOutput, self.speed)
            #elif self.getPosition() < self.min and val < 0:
                #self.motor.set(ControlMode.PercentOutput, self.speed)
            #else:
                #self.stop()

    def stop(self):
        self.motor.stopMotor()

    def givePosition(self):
        self.motor.setSelectedSensorPosition(1500)

    def returnZero(self):
        self.motor.set(ControlMode.Position, 0)

    def captureOrientation(self):
        self.fieldAngle = robot.drivetrain.getAngle()

    def turretFieldOriented(self): # Use for when traveling 'round the field.
        degrees = (self.fieldAngle - robot.drivetrain.getAngle()) * 0.003
        if self.getPosition() + 2 < self.max and self.getPosition() - 2 > self.min:
            self.motor.set(ControlMode.PercentOutput, degrees)
        else:
            self.stop()

    def setPosition(self, position):
        self.error = self.getPosition() - position
        self.rotate = self.error * 0.005
        print('self.error = '+ str(self.rotate))
        if abs(self.rotate) > .3:
            self.rotate = math.copysign(.3, self.rotate)

        self.move(self.rotate)
        #if self.error > 1:
            #self.move(self.rotate)
            #print('self.rotate = '+ str(self.rotate))
        #else:
            #self.stop()



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

        self.setDefaultCommand(TurretMoveCommand())


