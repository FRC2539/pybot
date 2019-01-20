from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from custom.config import Config
from networktables import NetworkTables
from commands.network.alertcommand import AlertCommand
from commands.drivetrain.turntocommand import TurnToCommand
import commandbased.flowcontrol as fc

#from commands.drivetrain.turncommand import TurnCommand
#from commands.drivetrain.movecommand import MoveCommand
#from commands.drivetrain.setspeedcommand import setSpeedCommand

def noCargo():
    #NetworkTables.initialize(server='roborio-2539-frc.local')
    if Config('cameraInfo/cargoFound', False):
        return False
    else:
        return True


class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        print('auto on')
        #self.addSequential(TurnToCommand(5))

        NetworkTables.initialize(server='roborio-2539-frc.local')

        #hasCargo = Config('cameraInfo/cargoFound', False)
        #self.addSequential(AlertCommand('Cargo: %s' % str(hasCargo)))
        #print(str(hasCargo))

        @fc.WHILE(noCargo)
        def lookingforcargo(self):
            print('looking for cargo')

        print('after while')
