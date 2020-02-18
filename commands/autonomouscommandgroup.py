from wpilib.command import CommandGroup
from wpilib import DriverStation as _ds

from networktables import NetworkTables

import commandbased.flowcontrol as fc
from custom.config import Config

from commands.ballsystem.runballflowcommandgroup import RunBallFlowCommandGroup

from commands.network.alertcommand import AlertCommand

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand

from commands.hood.activesethoodcommand import ActiveSetHoodCommand

from commands.shooter.shootcommand import ShootCommand
from commands.shooter.controlledshootcommand import ControlledShootCommand

from commands.colorwheel.autosetwheel import AutoSetWheelCommand

from commands.limelight.sudocommandgroup import SudoCommandGroup

class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__('Autonomous')

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Eat Beans') # Put given game data here through network tables.
        def simpleAuto(self):
            self.addParallel(ShootCommand(4200)) # prespin the shooter.
            self.addSequential(SudoCommandGroup(), 1) # sets turret and hood
            self.addSequential(RunBallFlowCommandGroup(), 7) # runs the ball feed to shoot.
            self.addSequential(MoveCommand(-12)) # goes back 12 inches.
