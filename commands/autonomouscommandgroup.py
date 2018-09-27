from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from custom.config import Config

from wpilib.command.waitcommand import WaitCommand
from commands.drivetrain.pivotcommand import PivotCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.turntocommand import TurnToCommand
from commands.drivetrain.pivottocommand import PivotToCommand
from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
from commands.intake.intakecommand import IntakeCommand
from commands.intake.outakecommand import OutakeCommand
from commands.elevator.gotoheightcommand import GoToHeightCommand
from commands.resetcommand import ResetCommand
from commands.elevator.elevatorresetcommand import ElevatorResetCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand
from commands.network.alertcommand import AlertCommand
from wpilib.command.printcommand import PrintCommand

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        self.addSequential(ZeroGyroCommand())

        @fc.IF(lambda: True)
        def phase1(self):
            self.addParallel(GoToHeightCommand(5650))

#NOTE:  To Ben, Your problem was that you set the upper limit of the elevator subsystem too low Sincerely, Quentin

            self.addSequential(WaitCommand(1))
            self.addParallel(MoveCommand(36))

        self.addSequential(WaitCommand(1))

        @fc.IF(lambda: True)
        def phase2(self):
            self.addParallel(MoveCommand(-36))
            self.addSequential(WaitCommand(0.1))
            self.addParallel(OutakeCommand(-0.5))
            #self.addParallel(SetSpeedCommand(435))
#NOTE: To Bew and Quentle, your command went pycho . . . Not my fault, Samantha
#NOTE: To Bew and Quentle, I fixed your robot. -Maxim P.S. Your names are now Bew and Quentle

        self.addSequential(GoToHeightCommand(0))
        self.addSequential(AlertCommand('You have been hacked......................................... System Failing............... Detected Threat............................ ISIS ................. Programming attemps............ Robot will.............. Self Destruct.............. IN'))
        self.addSequential(WaitCommand(1))
        self.addSequential(AlertCommand('3', 'Info'))
        self.addSequential(WaitCommand(1))
        self.addSequential(AlertCommand('2', 'Info'))
        self.addSequential(WaitCommand(1))
        self.addSequential(AlertCommand('1', 'Info'))
        self.addSequential(WaitCommand(1))
        self.addSequential(AlertCommand('<b style="font-size:40px">BOOM</b>'))
        self.addSequential(SetSpeedCommand(1700))
        self.addSequential(MoveCommand(-35))
        self.addSequential(TurnCommand(-90))
        self.addSequential(MoveCommand(35))
        self.addSequential(AlertCommand('HI'))
        self.addSequential(TurnCommand(135))
        @fc.IF(lambda: True)
        def phase3(self):
            self.addParallel(MoveCommand(75.2728370662))
            self.addParallel(IntakeCommand(0.75))

        #self.addSequential(IntakeCommand(0.5))
        #self.addSequential(MoveCommand(34))
