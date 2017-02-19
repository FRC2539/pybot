from .debuggablesubsystem import DebuggableSubsystem
from networktables import NetworkTables
from custom.config import Config
from subsystems.drivetrain import DriveTrain
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

    def isVisible(self):
        print(self.liftVision.getBoolean('liftVisible'))
        return self.liftVision.getBoolean('liftVisible')

    def offsetFromTarget(self):
        return self.liftVision.getValue('liftCenter')

    def distanceToTarget(self):
        return self.liftVision.getValue('liftDistance')


    def isLiftVisible(self):
        try:
            return self.liftVision.getBoolean('liftVisible')
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
