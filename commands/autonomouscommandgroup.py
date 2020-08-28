from wpilib.command import CommandGroup
from wpilib import DriverStation as _ds

from networktables import NetworkTables

import commandbased.flowcontrol as fc
from custom.config import Config

#from commands.network.alertcommand import AlertCommand


from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.gyromovecommand import GyroMoveCommand



class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__('Autonomous')

        startingBalls = 3#Config('Autonomous/NumberOfBallsAtStart', 3)
        #print('SET STUFFF ' + str(Config('Autonomous/autoModeSelect', None)))

        #@fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Move Test') # Put given game data here through network tables.


        @fc.IF(lambda: True) # Put given game data here through network tables.
        def ThreeBallAuto(self):#should be good for now
            #self.addSequential(MoveCommand(300), 2)
            #self.addSequential(MoveCommand(-300), 2)
            self.addSequential(TurnCommand(90))

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Move Test 2') # Put given game data here through network tables.
        def ThreeBallAuto2(self):#should be good for now
            self.addSequential(MoveCommand(30))
            #self.addSequential(GyroMoveCommand(15))
