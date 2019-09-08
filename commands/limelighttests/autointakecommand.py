from wpilib.command.command import Command
from wpilib import Timer

import robot

class AutoIntakeCommand(Command):

    def __init__(self, pipeline):
        super().__init__('Auto Intake')

        self.requires(robot.limelighttests)
        self.requires(robot.intake)
        self.requires(robot.lights)

        self.pipeline = pipeline


    def initialize(self):

        robot.limelighttests.setPipeline(self.pipeline)


    def execute(self):
        if robot.limelighttests.seesCargo() and robot.limelighttests.withinRange() and not robot.intake.hasCargo:
            robot.intake.intake()
            robot.lights.solidGreen()

        else:
            robot.intake.stop()
            robot.lights.off()


    def end(self):
        robot.intake.stop()
        robot.lights.off()
