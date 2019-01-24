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

def dcargoX():
    return Config('cameraInfo/cargoX', -1)

def ddistanceToCargo():
    return Config('cameraInfo/distanceToCargo', -1)

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        ds = DriverStation.getInstance()

        #print("auto start")
        self.addSequential(AlertCommand('auto start'))

        #self.addSequential(TurnCommand(-10))
        #self.addSequential(MoveWithGyroCommand(10))

        #self.addSequential(AlertCommand('Start X: %s' % float(dcargoX())))

        @fc.WHILE(hasCargo)
        def initfoundcargo(self):
            #distanceToCargo = Config('cameraInfo/distanceToCargo')

            #self.addSequential(AlertCommand('X: %s' % float(dcargoX())))
            #self.addSequential(AlertCommand('moveX: %s' % float(moveX)))
            #self.addSequential(TurnCommand(moveX))
            @fc.IF(lambda: dcargoX() >= 240)
            def cargoLeft(self):
                self.addSequential(TurnCommand(4))
                #self.addSequential(AlertCommand('X: %s' % float(dcargoX())))

            @fc.IF(lambda: dcargoX() <= 280)
            def cargoRight(self):
                self.addSequential(TurnCommand(-4))
                #self.addSequential(AlertCommand('X: %s' % float(dcargoX())))

            #@fc.IF(lambda: dcargoX() <= 280)
            #def getCargo(self):
                #lookforcargo(noCargo)
            #self.addSequential(MoveWithGyroCommand(ddistanceToCargo()))

        #self.addSequential(AlertCommand('before no cargo'))
        @fc.WHILE(noCargo)
        def lookforcargo(self):


            @fc.WHILE(hasCargo)
            def foundcargo(self):

                #distanceToCargo = Config('cameraInfo/distanceToCargo')

                self.addSequential(AlertCommand('X: %s' % float(dcargoX())))
                #self.addSequential(AlertCommand('moveX: %s' % float(moveX)))
                #self.addSequential(TurnCommand(moveX))
                @fc.IF(lambda: dcargoX() >= 240)
                def cargoLeft(self):
                    self.addSequential(TurnCommand(4))
                    #self.addSequential(AlertCommand('X: %s' % float(dcargoX())))

                @fc.IF(lambda: dcargoX() <= 280)
                def cargoRight(self):
                    self.addSequential(TurnCommand(-4))
                    #self.addSequential(AlertCommand('X: %s' % float(dcargoX())))

                #self.addSequential(MoveWithGyroCommand(ddistanceToCargo() -2))


        #print("auto end")
        self.addSequential(AlertCommand('auto end'))
