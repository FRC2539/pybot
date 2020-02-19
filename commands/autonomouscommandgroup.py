from wpilib.command import CommandGroup
from wpilib import DriverStation as _ds

from networktables import NetworkTables

import commandbased.flowcontrol as fc
from custom.config import Config

from commands.network.alertcommand import AlertCommand

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand

from commands.hood.setlaunchanglecommand import SetLaunchAngleCommand

from commands.shooter.shootcommand import ShootCommand
from commands.shooter.controlledshootcommand import ControlledShootCommand

from commands.colorwheel.autosetwheel import AutoSetWheelCommand

from commands.limelight.sudocommandgroup import SudoCommandGroup

from commands.ballsystem.rununtilloadedcommand import RunUntilLoadedCommand
from commands.ballsystem.runballflowcommandgroup import RunBallFlowCommandGroup

from commands.ballsystem.rununtilemptycommand import RunUntilEmptyCommand

class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__('Autonomous')

        startingBalls = Config('Autonomous/NumberOfBallsAtStart', 3)

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Eat Beans') # Put given game data here through network tables.
        def simpleAuto(self):
            self.addParallel(SudoCommandGroup(), 1) # Sets the hood & turret position
            self.addParallel(ShootCommand(4200)) # spins the shooter up while moving
            self.addSequential(MoveCommand(-36)) # goes back 90 inches. I recommend using the below commonly to monitor ball shots.
            self.addSequential(RunUntilEmptyCommand(startingBalls)) # NOTE: WARNING: RENNNA RENNNA RENNA: read pls :) ADD START NUMBER OF BALLS; THIS WILL START SHOOTER IF NOT STARTED (might remove that), BUT STILL START BEFOREHAND
            #self.addSequential(ControlledShootCommand(4200), 8) # only shoots when around 4200, gives 8 seconds

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Inner Power Port')
        def rennaFirstFunction(self):
            print ("I Shoot")
            self.addSequential(SudoCommandGroup(), 1) #Shoots Balls
            self.addSequential(RunBallFlowCommandGroup(), 7) #Take balls up to shoot.addParallel
            self.addSequential(MoveCommand(-36)) # Goes back 90 inches
            self.addSequential(TurnCommand(90)) #Turns 90 degrees right
            self.addSequential(MoveCommand(66)) # Go forward 66 inches
            self.addSequential(TurnCommand(90)) #Turns 90 degrees right (and face trench)
            self.addSequential(MoveCommand(114.63))#Go forward 114.63 inches
            self.addParallel(RunUntilLoadedCommand()) #Go through the trench while picking up balls

        @fc.IF (lambda: str(Config('Autonomous/autoModeSelect')) == 'SkSkSkirt off the init line')
        def getOffInitLine (self):
            print("sksksk")
            self.addSequential(MoveCommand(-36)) #Go back 90 inches Get off the initiation line
