from wpilib.command import Command

import robot

class LoadBallFromHopperCommand(Command):

    def __init__(self):
        super().__init__('Load Ball From Hopper')

        self.requires(robot.ballsystem)

    def initialize(self):
        if not robot.ballsystem.areTwoBallsPrimed():
            if not robot.ballsystem.isLowBallPrimed() and robot.ballsystem.isUpperBallPrimed():
                robot.ballsystem.runLowerConveyorSlow()
            else:
                robot.ballsystem.runAllSlow()

    def execute(self):
        print('low ' + str(robot.ballsystem.isLowBallPrimed()))
        print('up ' + str(robot.ballsystem.isUpperBallPrimed()))
        if robot.ballsystem.isLowBallPrimed() and robot.ballsystem.isUpperBallPrimed():
            robot.ballsystem.stopLowerConveyor()

        elif robot.ballsystem.isUpperBallPrimed():
            robot.ballsystem.stopVerticalConveyor()

    def end(self):
        robot.ballsystem.stopAll()
