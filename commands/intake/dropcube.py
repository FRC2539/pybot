from wpilib.command import CommandGroup
from commands.drivetrain.movecommand import MoveCommand
from commands.intake.slowouttakecommand import SlowOuttakeCommand
from wpilib.command.waitcommand import WaitCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand



class DropCube(CommandGroup):

    def __init__(self):
        super().__init__('DropCube')
        
        self.addSequential(SetSpeedCommand(2600))
        self.addParallel(MoveCommand(-20))
        self.addSequential(WaitCommand(0.5))
        self.addSequential(SlowOuttakeCommand())
       
       
