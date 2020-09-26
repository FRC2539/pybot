import commandbased.flowcontrol as fc

from crapthatwillneverwork.kougarkoursegenerator import KougarKourseGenerator
from crapthatwillneverwork.kougarkourse import KougarKourse

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand

testTrajectory = KougarKourseGenerator(0)

class AutonomousCommandGroup(fc.CommandFlow):
        
    def __init__(self):
        super().__init__('Autonomous')

        #self.addSequential(KougarKourse(testTrajectory)) # The trajectory attribute is optional now; what I have here will enable students to define a trajectory at init, instead of building it at the start. This is possible, just replace trajectoryOne with the trajectory number, but this is strongly advised against. Label/name the variables based off of what they will do.

        self.addSequential(MoveCommand(60))
        self.addSequential(TurnCommand(180))
        self.addSequential(MoveCommand(60))
