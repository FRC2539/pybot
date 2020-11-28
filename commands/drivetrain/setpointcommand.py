from wpilib.command import InstantCommand

import robot

class SetPointCommand(InstantCommand):

    def __init__(self):
        super().__init__('Set Point')

        self.requires(robot.drivetrain)        

    def initialize(self):
        if not robot.drivetrain.capturedPoints is []:
            robot.drivetrain.capturedPoints.append(robot.drivetrain.getPositions())
