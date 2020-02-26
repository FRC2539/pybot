from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Ballsystem')

        self.requires(robot.ballsystem)

    def execute(self):
        if abs(robot.drivetrain.getTilt()) > 10.0: # if the angle is greater than ten degrees any way, it reverses the belt slowly.
            robot.ballsystem.slowVerticalReverse()
        else:
            robot.ballsystem.stopVerticalConveyor()
