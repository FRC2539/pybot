from wpilib.command import Command
import commandbased.flowcontrol as fc

from commands.drivetrain.movecommand import MoveCommand
from commands.intake.loadinemptycommandgroup import LoadInEmptyCommandGroup
import robot

class ManageBallsMoveCommand(Command):
    def __init__(self, distance):
        super().__init__("Move While Intaking")
        
        self.distance = distance
        
        self.requires(robot.drivetrain)
        self.requires(robot.intake)
        self.requires(robot.revolver)
        
    def initialize(self):
        
        try:
            robot.drivetrain.setSlowP()
        
        except(AttributeError):
            pass
        
        robot.intake.intakeBalls()
        
        robot.revolver.setCustomRR(0.5)
        if robot.revolver.isEmpty():
            robot.revolver.stopRevolver()
        else:
            robot.revolver.setVariableSpeed(-0.2)

        self.targetPositions = []
        self.offset = robot.drivetrain.inchesToUnits(self.distance)
                
        sign = 1
        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + (self.offset * sign))
            sign *= -1

        robot.drivetrain.setPositions(self.targetPositions)
    
    def execute(self):
        if robot.revolver.isEmpty():
            robot.revolver.stopRevolver()
        else:
            robot.revolver.setVariableSpeed(-0.2)
        
        print('t ' +  str(self.targetPositions))
        print('pos ' + str(robot.drivetrain.getPositions()))
        
    def isFinished(self):
        return robot.drivetrain.doneMoving(self.targetPositions)
        
    def end(self):
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)
        
        robot.intake.stopIntake()
        robot.pneumatics.retractIntakeSolenoid()
        
        robot.revolver.stopRevolver()
        robot.revolver.enableRampRate()
        
