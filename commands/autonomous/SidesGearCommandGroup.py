from wpilib.command import CommandGroup
from .movecommand import MoveCommand
from .turncommand import TurnCommand

class SidesGearCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('SidesGearCommandGroup')
        '''self.AddSequential(MoveCommand())
        self.AddSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.AddSequential(MoveCommand(NetworkTables(cameraTarget)))
        self.AddSequential(releaseGear)'''





