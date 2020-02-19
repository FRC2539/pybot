from wpilib.command import Command

import robot

class LoadBallFromHopperCommand(Command):

    def __init__(self):
        super().__init__('Load Ball From Hopper')

        self.requires(robot.ballsystem)

    def initialize(self):
        if not robot.ballsystem.isBallPrimed():
            robot.ballsystem.setHorizontalCoast()
            robot.ballsystem.runLowerConveyorSlow()

    def execute(self):
        print(robot.ballsystem.isBallPrimed())

        if robot.ballsystem.isBallPrimed():
            robot.ballsystem.stopLowerConveyor()
        else:
            robot.ballsystem.runLowerConveyorSlow()

    def end(self):
        robot.ballsystem.stopLowerConveyor()
        robot.ballsystem.setHorizontalBrake()
