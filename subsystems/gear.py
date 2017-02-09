from .debuggablesubsystem import DebuggableSubsystem
from networktables import NetworkTables
from custom.config import Config
import ports

class Gear(DebuggableSubsystem):
    '''
    A subsystem designed for feeding balls to the shooter.
    '''

    def __init__(self):
        super().__init__('Gear')

        self.liftVision = NetworkTables.getTable('cameraTarget')

    def hasGear(self):
        return ports.gear.sensorID
    def visionStuff(self):
        if self.liftVision.getBoolean('liftVisible'):
            return True
        if self.liftVision.getValue('liftCenter') < 0:
            return True
        if self.liftVision.getValue('liftDistance') < 10:
            return True
