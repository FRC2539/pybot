from wpilib.command import CommandGroup
from wpilib.command import PrintCommand
from wpilib.driverstation import DriverStation
from custom.config import Config
from commands.network.alertcommand import AlertCommand
from wpilib.command.waitcommand import WaitCommand
import commandbased.flowcontrol as fc

from commands.drivetrain.movecommand import MoveCommand

from networktables import NetworkTables

from commands.resetcommand import ResetCommand

from commands.drivetrain.resetencoderscommand import ResetEncodersCommand
from commands.drivetrain.pathfindermovecommand import PathfinderMoveCommand

from commands.intake.intakecommand import IntakeCommand

import robot

from commands.drivetrain.movecommand import MoveCommand

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')
        print("auto init")

        self.addSequential(PathfinderMoveCommand([[6, 3, 0], [6, 5, 45], [6, -2, 0]]))
