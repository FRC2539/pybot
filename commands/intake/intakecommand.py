from wpilib.command.command import Command
import time
import robot

class IntakeCommand(Command):

    def __init__(self):
        super().__init__('Intake')

        self.requires(robot.intake)


    def initialize(self):
        robot.lights.solidGreen()
        robot.intake.intake()


    def end(self):
        robot.lights.off()
        time.sleep(0.25)
        robot.intake.stop()
        robot.intake.hasCargo = True
