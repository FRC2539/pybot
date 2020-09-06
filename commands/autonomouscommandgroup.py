from wpilib.command import CommandGroup, PrintCommand
from wpilib import DriverStation as _ds

from networktables import NetworkTables

import commandbased.flowcontrol as fc
from custom.config import Config

#from commands.network.alertcommand import AlertCommand

from commands.drivetrain.movecommand import MoveCommand
#from commands.drivetrain.turncommand import TurnCommand
#from commands.drivetrain.gyromovecommand import GyroMoveCommand

class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__('Autonomous')

        #establish the auto modes for dashboard and use these values in auto if string check
        table = NetworkTables.getTable('Autonomous')
        autoNames = ['Move Test','Move Test 2','More Move Test']
        autoString = ''
        for auto in autoNames:
            autoString += str(auto + '$')
        autoString = autoString[:-1]
        table.putString('autoModes', autoString)

        startingBalls = 3#Config('Autonomous/NumberOfBallsAtStart', 3)


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Move Test')
        def MoveTest(self):#should be good for now
            self.addSequential(MoveCommand(80))
            self.addSequential(PrintCommand("move: 80"))
            ##self.addSequential(GyroMoveCommand(15))

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Move Test 2')
        def MoveTest2(self):#should be good for now
            self.addSequential(MoveCommand(30))
            self.addSequential(PrintCommand("move2: 30"))
            ##self.addSequential(GyroMoveCommand(15))
