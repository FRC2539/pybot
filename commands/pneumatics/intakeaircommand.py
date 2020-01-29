from wpilib.command import Command
import robot

class IntakeAirCommand(Command):

    def __init__(self):
        super().__init__('Intake Air')

        self.requires(robot.pneumatics)


    def initialize(self):
        robot.pneumatics.setLoopOn()
        robot.pneumatics.intake()


    def isFinished(self):
        print(robot.pneumatics.getStatus())
        return robot.pneumatics.getStatus()


    def end(self):
        robot.pneumatics.stopIntake()
