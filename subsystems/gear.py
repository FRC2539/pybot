from wpilib.relay import Relay
from wpilib.digitalinput import DigitalInput
from networktables import NetworkTables

from wpilib.command.subsystem import Subsystem
from custom.config import Config
from subsystems.drivetrain import DriveTrain
import ports

class Gear(Subsystem):
    '''
    A subsystem designed for hanging gears on the lifts.
    '''

    def __init__(self):
        super().__init__('Gear')

        self.liftVision = NetworkTables.getTable('cameraTarget')
        self.sensor = DigitalInput(ports.gear.sensorID)
        self.lightRing = Relay(ports.gear.lightRingPort)


    def initDefaultCommand(self):
        from commands.gear.smartlightcommand import SmartLightCommand

        #self.setDefaultCommand(SmartLightCommand())


    def hasGear(self):
        return self.sensor.get()


    def isLiftVisible(self):
        try:
            return self.liftVision.getBoolean('liftVisible', 0)
        except KeyError:
            return False


    def getLiftDistance(self):
        if self.isLiftVisible():
            return self.liftVision.getValue('liftDistance')

        return None


    def getLiftCenter(self):
        if self.isLiftVisible():
            return self.liftVision.getValue('liftCenter')

        return None


    def isLightOn(self):
        return self.lightRing.get() == Relay.Value.kReverse


    def turnOnLight(self):
        self.lightRing.set(Relay.Value.kReverse)


    def turnOffLight(self):
        self.lightRing.set(Relay.Value.kOff)
