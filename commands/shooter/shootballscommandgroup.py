import commandbased.flowcontrol as fc

from wpilib.command import WaitCommand

from commands.revolver.shooterdirectioncommand import ShooterDirectionCommand
from commands.shooter.setrpmcommand import SetRPMCommand

class ShootBallsCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Shoot Balls')

        self.addParallel(SetRPMCommand(4500))
        self.addSequential(WaitCommand(4)) # Alots four seconds for rev up.
        self.addParallel(ShooterDirectionCommand())

        # Add commands here with self.addSequential() and self.addParallel()
