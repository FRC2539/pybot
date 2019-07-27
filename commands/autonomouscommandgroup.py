from wpilib.command import CommandGroup
from wpilib.command import PrintCommand
from wpilib.driverstation import DriverStation
from custom.config import Config
from commands.network.alertcommand import AlertCommand
from wpilib.command.waitcommand import WaitCommand
import commandbased.flowcontrol as fc

from networktables import NetworkTables

import robot

from commands.drivetrain.movecommand import MoveCommand

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')
        print("auto init")

        #@fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'TEST')
        #def testAuto(self):
            #self.addParallel(SetArmCommandGroup(2.0))
            #self.addSequential(StrafeCommand(32))
            #self.addSequential(TransitionMoveCommand(25,80,30,100,0,0))

            #self.addSequential(SetArmCommandGroup(12.0))
            #print("turn")
            #self.addSequential(TurnCommand(180))
            #self.addSequential(MoveCommand(-48))
            #self.addSequential(HolonomicMoveCommand(0,-140,-255))
            #self.addSequential(HolonomicMoveCommand(-130,-50,-25))
            #self.addSequential(HolonomicMoveCommand(-90,225,55))
            #self.addSequential(SetArmCommandGroup(12.0))

            #self.addSequential(WaitCommand(.5))

            #self.addSequential(LowerCommand())

            #self.addSequential(SuperStructureGoToLevelCommand("lowHatches"))
            #self.addSequential(SuperStructureGoToLevelCommand("floor"))
            #self.addSequential(StrafeCommand(-20))


       ## Reset to field orientation.
        #@fc.IF(lambda: not robot.drivetrain.isFieldOriented)
        #def toggleBackToFieldOrientation(self):
            #self.addSequential(ToggleFieldOrientationCommand())


        ##Reset vision pipeline to 'closest' sorting option.
        #@fc.IF(lambda: True)
        #def setPipeline(self):
            #self.addSequential(SetPipelineCommand(0))
