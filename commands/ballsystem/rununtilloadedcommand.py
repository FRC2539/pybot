from wpilib.command.command import Command

import robot

class RunUntilLoadedCommand(Command):

    def __init__(self):
        super().__init__('Run Until Loaded')

        self.requires(robot.ballsystem)
        self.requires(robot.intake)

    def initialize(self):
        robot.intake.intake()
        if not robot.ballsystem.isBallPrimed():
            robot.ballsystem.runLowerConveyorSlow()

    def execute(self):
        if robot.ballsystem.isBallPrimed():
            robot.ballsystem.stopLowerConveyor()

    def end(self):
        robot.intake.stop()
        robot.ballsystem.stopLowerConveyor()
