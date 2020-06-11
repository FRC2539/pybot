import commandbased.flowcontrol as fc

from commands.drivetrain.turncommand import TurnCommand
from commands.shooter.shooterlimelightcommand import ShooterLimelightCommand


class ASeriousCommandThatWeCanActuallyUnderstandCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('A Serious Command That We Can Actually Understand')

        # Add commands here with self.addSequential() and self.addParallel()

        self.addSequential(ShooterLimelightCommand())
        #self.addSequential(ShooterLimelightCommand(),2)
        #self.addSequential(TurnCommand(500))
