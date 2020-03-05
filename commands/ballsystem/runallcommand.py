from wpilib.command import Command

from wpilib import Timer

import robot

class RunAllCommand(Command):

    def __init__(self):
        super().__init__('Run All')

        self.requires(robot.ballsystem)
        self.requires(robot.ledsystem)

        self.timer = Timer()

    def initialize(self):
        robot.ballsystem.runVerticalConveyor()
        robot.ballsystem.reverseLowerConveyorSlow()
        self.timer.start()
        robot.ledsystem.setBlue()

    def execute(self):
        if self.timer.hasElapsed(1):
            robot.ballsystem.runLowerConveyor()
            self.timer.stop()

    def end(self):
        robot.ballsystem.stopAll()
        self.timer.reset()
        robot.ledsystem.turnOff()
