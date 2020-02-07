from wpilib.command import Command

import robot

class RunLowerCommand(Command):

    def __init__(self):
        super().__init__('Run Lower')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.runLowerConveyor()

    def end(self):
        robot.ballsystem.stopLowerConveyor()
