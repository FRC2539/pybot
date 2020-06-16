from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Ballsystem')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.stopAll() # Added this because it might need an initialize?

    def execute(self):
        #print('angle  ' +str(robot.drivetrain.getTilt()))
        if abs(robot.drivetrain.getTilt()) > 1.15: # if the angle is greater than ten degrees any way, it reverses the belt slowly.
            #print('\n\nshould be reversing')
            robot.ballsystem.slowVerticalReverse()
        else:
            robot.ballsystem.stopVerticalConveyor()
