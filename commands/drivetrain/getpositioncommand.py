from wpilib.command.command import Command

import robot

class GetPositionCommand(Command):

    def __init__(self):
        super().__init__('Get Position', 0.5)

        self.requires(robot.drivetrain)


    def initialize(self):
        try:
            print(str(robot.drivetrain.getPositions()))
        except:
            print('\nI CRASHED \n')

    def end(self):
        robot.drivetrain.initDefaultCommand()
