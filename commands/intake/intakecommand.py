from wpilib.command.command import Command
from wpilib.digitalinput import DigitalInput

import robot

class IntakeCommand(Command):

    def __init__(self, speed):
        super().__init__('Intake')

        self.requires(robot.intake)
        self.speed = speed

    def initialize(self):
        robot.intake.IntakePowerCube(self.speed)
        print('Intake Running')

    def execute(self):
        pass


    def end(self):
        robot.intake.IntakePowerCube(0)
        print('Intake Stopped')

    def isFinished(self):
        if robot.intake.isCubeInIntake():
            robot.intake.IntakePowerCube(0)
            return True
