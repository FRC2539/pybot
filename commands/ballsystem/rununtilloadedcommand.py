from wpilib.command import Command

from wpilib import Timer

import robot

class RunUntilLoadedCommand(Command):

    def __init__(self):
        super().__init__('Run Until Loaded')

        self.requires(robot.ballsystem)
        self.requires(robot.intake)
        self.requires(robot.ledsystem)

        #self.timerRunning = False
        #self.timer = Timer()

    def initialize(self):
        robot.intake.intake(0.6)
        robot.ledsystem.setGreen()

        if not robot.ballsystem.areTwoBallsPrimed():
            if not robot.ballsystem.isLowBallPrimed() and robot.ballsystem.isUpperBallPrimed():
                robot.ballsystem.runLowerConveyorSlow()
            else:
                robot.ballsystem.runAllSlow()

    def execute(self):
        if robot.ballsystem.isLowBallPrimed() and robot.ballsystem.isUpperBallPrimed():
            robot.ballsystem.stopLowerConveyor()

        elif robot.ballsystem.isUpperBallPrimed():
            #if not self.timerRunning:
                #self.timerRunning = True
                #self.timer.start()

            #if self.timer.get() >= 0.1 and self.timerRunning:
            robot.ballsystem.stopVerticalConveyor()

    def end(self):
        robot.intake.stop()
        robot.ballsystem.stopAll()

        robot.ledsystem.turnOff()

        #self.timer.stop()
        #self.timer.reset()
        #self.timerRunning = False
