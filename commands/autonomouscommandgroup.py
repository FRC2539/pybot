from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from custom.config import Config
from networktables import NetworkTables
from commands.network.alertcommand import AlertCommand

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')
        NetworkTables.initialize(server='roborio-2539-frc.local')

        distanceToCargo = Config('cameraInfo/distanceToCargo', None)
        hasCargo = Config('cameraInfo/cargoFound', False)
        print(str(hasCargo))
        if hasCargo:
            self.addSequential(AlertCommand('Distance to cargo: %s' % float(distanceToCargo)))
