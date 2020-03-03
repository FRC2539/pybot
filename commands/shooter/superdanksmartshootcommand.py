from wpilib.command import Command
from wpilib.timer import Timer

import robot

class SuperDankSmartShootCommand(Command):

    def __init__(self, rpm, tolerance):
        super().__init__('Super Dank Smart Shoot')

        self.desiredRPM = rpm
        self.tolerance = tolerance

        self.timer = Timer()

        self.requires(robot.shooter)
        self.requires(robot.ballsystem)
        self.requires(robot.intake)

    def initialize(self):
        #self.ballCount = 3 # add auto measure by kieren later.

        robot.shooter.setRPM(self.desiredRPM)

    def execute(self):
        if robot.shooter.getRPM() >= (self.desiredRPM - self.tolerance):
            if robot.ballsystem.isUpperBallPrimed():
                robot.ballsystem.runVerticalConveyor()
                robot.ballsystem.stopLowerConveyor()

            else:
                robot.ballsystem.runAll()

        else: # if the wheels not up to speed, don't run the vertical, but chamber one.
            if not robot.ballsystem.areTwoBallsPrimed(): # make sure none are there before stopping important belts.
                robot.ballsystem.stopVerticalConveyor()
                robot.ballsystem.runLowerConveyorSlow()

    #def isFinished(self):
     #   return self.ballCount <= 0

    def end(self):
        robot.shooter.stop()
        robot.ballsystem.stopAll()
        robot.intake.stop()




