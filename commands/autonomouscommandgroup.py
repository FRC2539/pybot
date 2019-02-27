from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from custom.config import Config

from commands.drivetrain.holonomicmovecommand import HolonomicMoveCommand
from commands.drivetrain.visionmovecommand import VisionMoveCommand
from commands.drivetrain.transitionmovecommand import TransitionMoveCommand
from commands.drivetrain.movewithgyrocommand import MoveWithGyroCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.movecommand import MoveCommand

from commands.intake.slowejectcommand import SlowEjectCommand

from commands.superstructure.superstructuregotolevelcommand import SuperStructureGoToLevelCommand


class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        self.addParallel(SuperStructureGoToLevelCommand('lowHatches'))

        #self.addSequential(MoveCommand(100))
        #Config('DriveTrain/ticksPerInch', 350)
        #self.addSequential(TransitionMoveCommand(30,60,30,150,0,0))

 #       self.addSequential(VisionMoveCommand())

        #self.addSequential(HolonomicMoveCommand(70, 54, 45))

        #go to rocket then go to ham play place
        #self.addSequential(TransitionMoveCommand(30,60,30,220,1,45))
        #self.addSequential(VisionMoveCommand())
        #self.addSequential(TransitionMoveCommand(-50,60,-60,220,1,145))

        #cargoship to place first hatch then go to ham play place
        #self.addSequential(TransitionMoveCommand(30,60,30,240,1,-30))
        #self.addSequential(SlowEjectCommand(), 1)
        #self.addSequential(TurnCommand(-160))
        #self.addSequential(TransitionMoveCommand(30,60,30,270,140,-50))
        #self.addSequential(VisionMoveCommand())

        #start right to rocket1
        #self.addSequential(TransitionMoveCommand(30,60,30,310,35,15))
        #self.addSequential(TransitionMoveCommand(60,60,0,115,10,150))
        #self.addSequential(TurnCommand(90))
        #self.addSequential(VisionMoveCommand())
        '''
        @fc.IF(lambda: Config('Autonomous/Auto') == '1')
        def centerauto(self):
            ###cargoship to place first hatch then go to ham play place
            self.addSequential(TransitionMoveCommand(30,60,30,240,1,-30))
            self.addSequential(VisionMoveCommand())
            self.addSequential(MoveWithGyroCommand(-5))
            self.addSequential(TurnCommand(160))
            self.addSequential(TransitionMoveCommand(30,60,30,270,140,50))
            self.addSequential(VisionMoveCommand())
            self.addSequential(MoveWithGyroCommand(-10))

        @fc.IF(lambda: Config('Autonomous/Auto') == '1')
        def leftAuto(self):
            self.addSequential(TransitionMoveCommand(30,60,30,220,1,-45))
            self.addSequential(VisionMoveCommand())
            self.addSequential(ElevatorGoToLevelCommand('midHatches'))
            self.addSequential(MoveWithGyroCommand(2))
            self.addParallel(ElevatorGoToLevelCommand('floor'))
            self.addSequential(MoveWithGyroCommand(-2))
            self.addSequential(TransitionMoveCommand(-50,60,-60,220,1,-145))
        '''
