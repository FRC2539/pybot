from .debuggablesubsystem import DebuggableSubsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX
from wpilib import DigitalInput
from custom.config import Config

from networktables import NetworkTables as nt

import ports


class Hatch(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Hatch')

        self.motor = WPI_TalonSRX(ports.hatch.motorID)
        self.motor.setNeutralMode(NeutralMode.Brake)
        self.motor.setSafetyEnabled(False)

        self.rightLimitSwitch = DigitalInput(ports.hatch.rightLimitSwitch)
        self.leftLimitSwitch = DigitalInput(ports.hatch.leftLimitSwitch)

        #self.tape = Config('limelight/tv', 0)

        #self.nt = nt.getTable('limelight')
        #self.ntLow = nt.getTable('limelight-low')

        #self.pipeID = 1

        self.hasHatch = False


    def hold(self):
        self.motor.set(0.2)


    def hasHatchPanel(self):
        return (not self.rightLimitSwitch.get()) or (not self.leftLimitSwitch.get())


    def hasSecureHatchPanel(self):
        return (not self.rightLimitSwitch.get()) and (not self.leftLimitSwitch.get())


    def stop(self):
        self.motor.set(0)


    def eject(self):
        self.motor.set(-1)


    def slowEject(self):
        self.motor.set(-0.5)


    def grab(self):
        self.motor.set(0.9)


    def initDefaultCommand(self):
        from commands.hatch.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())

    #def getTapeValue(self):
        #self.nt.putNumber('pipeline', 1)
        #self.ntLow.putNumber('pipeline', 0)
        #x=0
        #while x<125000:
            #x+=1


        #if self.tape == 0 :
            #self.nt.putNumber('pipeline', 0)
            #self.ntLow.putNumber('pipeline', 1)
            #x=0
            #while x<125000:
                #x+=1

            #if self.tape == 1:
                #self.nt.putNumber('pipeline', 0)
                #self.ntLow.putNumber('pipeline', 0)
                #return True

            #else:
                #self.nt.putNumber('pipeline', 0)
                #self.ntLow.putNumber('pipeline', 0)
                #return False

        #elif self.tape == 1 :
            #self.nt.putNumber('pipeline', 0)
            #self.ntLow.putNumber('pipeline', 0)
            #return True


    #def limeLightOff(self):
        #self.nt.putNumber('pipeline', 0)
        #self.ntLow.putNumber('pipeline', 0)
