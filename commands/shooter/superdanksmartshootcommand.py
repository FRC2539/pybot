from wpilib.command import Command
from wpilib import Timer

import robot

class SuperDankSmartShootCommand(Command):

    def __init__(self, rpm, tolerance=1000, startTol=100):
        super().__init__('Super Dank Smart Shoot')

        self.desiredRPM = rpm
        self.tolerance = tolerance
        self.startTol = startTol

        self.timer = Timer()

        self.requires(robot.shooter)
        self.requires(robot.ballsystem)
        self.requires(robot.intake)
        self.requires(robot.ledsystem)

        self.fullStart = True

    def initialize(self):
        #self.ballCount = 3 # add auto measure by kieren later.

        robot.shooter.setRPM(self.desiredRPM)

    def execute(self):
        if robot.shooter.getRPM() >= (self.desiredRPM - self.tolerance) and not self.fullStart:
            robot.ballsystem.runAll() # try this for now
            robot.ledsystem.setRed()
            robot.intake.intake(0.3)

            #if robot.ballsystem.isUpperBallPrimed():
                #robot.ballsystem.runVerticalConveyor()
                #robot.ballsystem.stopLowerConveyor()
            #else:
                #robot.ballsystem.runAll()

        elif self.fullStart and robot.shooter.getRPM() >= (self.desiredRPM - self.startTol):
            robot.ballsystem.runAll()
            robot.ledsystem.setRed()
            robot.intake.intake(0.3)

            self.fullStart = False


        else: # if the wheels not up to speed, don't run the vertical, but chamber one.
            #if not robot.ballsystem.areTwoBallsPrimed(): # make sure none are there before stopping important belts.
                #robot.ballsystem.stopVerticalConveyor()
                #robot.ballsystem.runLowerConveyorSlow()

            robot.ballsystem.stopAll()
            robot.ledsystem.flashRed()

    #def isFinished(self):
     #   return self.ballCount <= 0

    def end(self):
        robot.shooter.stop()
        robot.ballsystem.stopAll()
        robot.intake.stop()

        robot.ledsystem.turnOff()




