from wpilib.command.command import Command

import robot

class MoveOneFootCommand(Command):

    def __init__(self):
        super().__init__('Move One Foot')

        self.requires(robot.drivetrain)

    def initialize(self):
        self.targetPositions = []
        offset = robot.drivetrain.inchesToRotations(12.0)
        sign = 1
        print('OLD POSITIONS ' + str(robot.drivetrain.getPositions()))
        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + offset * sign)
            sign *= -1

        robot.drivetrain.setPositions(self.targetPositions)

        #print('Targets: ' + str(self.targetPositions))
        #print('Starting: ' + str(robot.drivetrain.getPositions()))


        #print('\nSET POSITIONS')
