from wpilib.command import Command

import robot


class PullWinchCommand(Command):

    def __init__(self):
        super().__init__('Pull Winch')

        self.requires(robot.winch)
        #self.requires(robot.drivetrain)

    def initialize(self):
        robot.winch.retract()

    def execute(self):
        #if robot.winch.isHigh(): # enough hopefully
            #robot.drivetrain.killMoveVarSet() # kills drivetrain by setting mult to zero.
        pass
    def end(self):
        robot.winch.stopWinch()


