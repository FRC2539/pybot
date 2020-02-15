from wpilib.command import Command

import robot

class ReverseHorizontalCommand(Command):

    def __init__(self):
        super().__init__('Reverse Horizontal')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.setHorizontalCoast()
        robot.ballsystem.reverseLowerConveyor()

    def end(self):
        robot.ballsystem.setHorizontalBrake()
        robot.ballsystem.stopLowerConveyor()
