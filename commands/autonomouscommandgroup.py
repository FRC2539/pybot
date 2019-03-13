from wpilib.command import CommandGroup
from wpilib.command import PrintCommand
from wpilib.driverstation import DriverStation
from custom.config import Config
from commands.network.alertcommand import AlertCommand
from wpilib.command.waitcommand import WaitCommand
import commandbased.flowcontrol as fc

from networktables import NetworkTables

import robot

from commands.drivetrain.strafecommand import StrafeCommand
from commands.drivetrain.movewithgyrocommand import MoveWithGyroCommand
from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
from commands.drivetrain.visionmovecommand import VisionMoveCommand
from commands.drivetrain.transitionmovecommand import TransitionMoveCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.strafecommand import StrafeCommand
from commands.drivetrain.pivotcommand import PivotCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand
from commands.drivetrain.togglefieldorientationcommand import ToggleFieldOrientationCommand

from commands.superstructure.superstructuregotolevelcommand import SuperStructureGoToLevelCommand

from commands.drivetrain.gototapecommand import GoToTapeCommand

from commands.intake.slowejectcommand import SlowEjectCommand

#from commands.superstructure.superstructuregotolevelcommand import SuperStructureGoToLevelCommand



class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')
        print("auto init")
        #NetworkTables.initialize(server='10.25.39.2')

        ds = DriverStation.getInstance()

        #NetworkTables.initialize()
        #dt = NetworkTables.getTable('DriveTrain')



        #am.delete()

        #NetworkTables.shutdown()
        #NetworkTables.initialize()


        #dt = NetworkTables.getTable('DriveTrain')
        #dt.putNumber('ticksPerInch', 300)
        #dt.putNumber('DriveTrain/width', 200)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('normalSpeed', 2500)
        #dt.putNumber('maxSpeed', 2500)

        #Config('DriveTrain/ticksPerInch', 350)
        #Config('DriveTrain/width', 29.5)
        #Config('DriveTrain/Speed/P', 1)
        #Config('DriveTrain/Speed/IZone', 30)
        #Config('DriveTrain/Speed/D', 31)
        #Config('DriveTrain/Speed/I', 0.001)
        #Config('DriveTrain/Speed/F', 0.7)
        #Config('DriveTrain/normalSpeed', 2500)
        #Config('DriveTrain/maxSpeed', 2500)

        dt = NetworkTables.getTable('DriveTrain')
        dt.putNumber('ticksPerInch', 250)
        dt.putNumber('normalSpeed', 2500)
        dt.putNumber('maxSpeed', 2500)

        #Config('DriveTrain/ticksPerInch', 250)
        #Config('DriveTrain/width', 29.5)
        #Config('DriveTrain/Speed/P', 1)
        #Config('DriveTrain/Speed/IZone', 30)
        #Config('DriveTrain/Speed/D', 31)
        #Config('DriveTrain/Speed/I', 0.001)
        #Config('DriveTrain/Speed/F', 0.7)
        #Config('DriveTrain/normalSpeed', 2500)
        #Config('DriveTrain/maxSpeed', 2500)


        print('dtms: '+str(Config('DriveTrain/maxSpeed', '')))
        print('citf: '+str(Config('CameraInfo/tapeFound', '')))
        print('ac: '+str(Config('Autonomous/autoModeSelect', 'None')))
        print('dt: '+str(Config('DriveTrain/ticksPerInch')))

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'RRF')
        def rrfAuto(self):
            self.addSequential(TransitionMoveCommand(25,60,25,70,0,30))
            self.addSequential(SuperStructureGoToLevelCommand("floor"))

            self.addSequential(StrafeCommand(40))
            #self.addSequential(TransitionMoveCommand(60,60,25,50,0,30))
            self.addSequential(GoToTapeCommand())
            self.addSequential(SuperStructureGoToLevelCommand("aboveFloor"))
            self.addSequential(MoveCommand(2))
            self.addSequential(SuperStructureGoToLevelCommand("floor"))
            self.addSequential(TransitionMoveCommand(-50,80,-85,150,1,162.5))
            self.addSequential(GoToTapeCommand())


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'RRB')
        def rrbAuto(self):
            #RightRocketback
            self.addSequential(TransitionMoveCommand(50,80,30,180,40,25))
            self.addSequential(TurnCommand(250))
            self.addSequential(SuperStructureGoToLevelCommand("floor"))
            self.addSequential(SuperStructureGoToLevelCommand("aboveFloor"))
            self.addSequential(StrafeCommand(-70), 5)
            self.addSequential(GoToTapeCommand())
            self.addSequential(MoveCommand(5))


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'RCF')
        def rcfAuto(self):
            self.addSequential(TransitionMoveCommand(30,90,15,40,1,0))
            #position arm
            self.addSequential(SuperStructureGoToLevelCommand("floor"))
            self.addSequential(SuperStructureGoToLevelCommand("aboveFloor"))
            self.addSequential(StrafeCommand(-20))
            self.addSequential(GoToTapeCommand())
            self.addSequential(MoveCommand(6))
            #lower arm
            self.addSequential(MoveCommand(-8))
            self.addSequential(TransitionMoveCommand(-90,90,-60,140,1,155.5))
            self.addSequential(StrafeCommand(-50))
            self.addSequential(GoToTapeCommand())


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'LRF')
        def lrfAuto(self):
            self.addSequential(TransitionMoveCommand(25,60,25,70,0,-30))
            self.addSequential(SuperStructureGoToLevelCommand("floor"))
            self.addSequential(SuperStructureGoToLevelCommand("aboveFloor"))
            self.addSequential(StrafeCommand(-39))
            self.addSequential(GoToTapeCommand())
            self.addSequential(MoveCommand(2))
            self.addSequential(SuperStructureGoToLevelCommand("floor"))
            self.addSequential(TransitionMoveCommand(-50,80,-60,120,1,-147.5))
            self.addSequential(GoToTapeCommand())


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'LRB')
        def lrbAuto(self):
            self.addSequential(TransitionMoveCommand(50,80,30,180,40,-25))
            self.addSequential(TurnCommand(-250))
            self.addSequential(SuperStructureGoToLevelCommand("floor"))
            self.addSequential(SuperStructureGoToLevelCommand("aboveFloor"))
            self.addSequential(StrafeCommand(70))
            self.addSequential(GoToTapeCommand())
            self.addSequential(MoveCommand(5))


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'RCB')
        def rcbAuto(self):
            self.addSequential(TransitionMoveCommand(50,80,30,180,50,15))
            self.addSequential(TurnCommand(-90))


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'LCB')
        def lcbAuto(self):
            self.addSequential(TransitionMoveCommand(50,80,30,180,50,-15))
            self.addSequential(TurnCommand(90))



        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'DEMO')
        def demoAuto(self):
            self.addSequential(VisionMoveCommand())


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'TEST')
        def testAuto(self):
            #self.addSequential(TransitionMoveCommand(25,80,30,100,0,0))
            #self.addSequential(SuperStructureGoToLevelCommand("floor"))
            #self.addSequential(SuperStructureGoToLevelCommand("aboveFloor"))
            #self.addSequential(SuperStructureGoToLevelCommand("floor"))
            self.addSequential(StrafeCommand(-20), 1)


        @fc.IF(lambda: not robot.drivetrain.isFieldOriented)
        def toggleBackToFieldOrientation(self):
            self.addSequential(ToggleFieldOrientationCommand())
