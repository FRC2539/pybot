from wpilib.command import CommandGroup
from wpilib import DriverStation as _ds

from networktables import NetworkTables

import commandbased.flowcontrol as fc
from custom.config import Config

from commands.network.alertcommand import AlertCommand

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand

from commands.hood.activesethoodcommand import ActiveSetHoodCommand

from commands.shooter.shootcommand import ShootCommand
from commands.shooter.controlledshootcommand import ControlledShootCommand

from commands.colorwheel.autosetwheel import AutoSetWheelCommand

class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__('Autonomous')

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Eat Beans') # Put given game data here through network tables.
        def simpleAuto(self):
            print('I RAN!!!')
            #self.addParallel(ActiveSetHoodCommand(27)) # Sets the hood position
            self.addParallel(ShootCommand(4200)) # spins the shooter up while moving
            self.addSequential(MoveCommand(-36)) # goes back 90 inches.
            #self.addSequential(TurnCommand(-10)) # turns ten degrees left
            #self.addSequential(ControlledShootCommand(4200), 8) # only shoots when around 4200, gives 8 seconds
