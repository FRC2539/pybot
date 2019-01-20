from wpilib.command import CommandGroup
from wpilib.command import PrintCommand
from wpilib.driverstation import DriverStation
from custom.config import Config
from networktables import NetworkTables
from commands.network.alertcommand import AlertCommand
from wpilib.command.waitcommand import WaitCommand
import commandbased.flowcontrol as fc

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.movewithgyrocommand import MoveWithGyroCommand
from commands.drivetrain.pivotcommand import PivotCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.runintowallcommand import RunIntoWallCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand
from commands.drivetrain.gotowallcommand import GoToWallCommand
from commands.elevator.gotoheightcommand import GoToHeightCommand
from commands.intake.intakecommand import IntakeCommand
from commands.intake.outtakecommand import OuttakeCommand
from commands.intake.slowouttakecommand import SlowOuttakeCommand

def noCargo():
    if Config('cameraInfo/cargoFound', False):
        return False
    else:
        return True

def hasCargo():
    if Config('cameraInfo/cargoFound', False):
        return True
    else:
        return False



class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        ds = DriverStation.getInstance()

        print("auto start")

        #self.addSequential(TurnCommand(-10))
        #self.addSequential(MoveWithGyroCommand(10))

        @fc.WHILE(noCargo)
        def lookforcargo(self):
            print("look for cargo")


        #@fc.WHILE(True)
        #def cargoLoop(self):


        @fc.WHILE(hasCargo)
        def foundcargo(self):
            cargoX = Config('cameraInfo/cargoX', -1)
            distanceToCargo = Config('cameraInfo/distanceToCargo',-1)

            #self.addSequential(AlertCommand('X: %s' % float(cargoX)))

            if cargoX >= 175:
                self.addSequential(TurnCommand(-10))

            if cargoX <= 125:
                self.addSequential(TurnCommand(10))

            #lookforcargo(noCargo)
            self.addSequential(MoveWithGyroCommand(distanceToCargo))


        print("auto end")
