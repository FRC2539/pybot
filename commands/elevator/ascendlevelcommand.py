from wpilib.command.command import Command

import robot

class AscendLevelCommand(Command):

    def __init__(self):
        super().__init__('Ascend Level')

        self.requires(robot.elevator)
        self.levels = robot.elevator.levels

    def initialize(self):
        pos = robot.elevator.getPosition()
        if pos < self.levels['lowHatches']:
            robot.elevator.goToLevel('lowHatches')
            print('\nIm in low hatches\n')

        elif pos < self.levels['lowBalls']:
            robot.elevator.goToLevel('lowBalls')

        elif pos < self.levels['midHatches']:
            robot.elevator.goToLevel('lowHatches')

        elif pos < self.levels['midBalls']:
            robot.elevator.goToLevel('lowHatches')

        elif pos < self.levels['highHatches']:
            robot.elevator.goToLevel('lowHatches')

        elif pos < self.levels['highBalls']:
            robot.elevator.goToLevel('lowHatches')

        else:
            print('rip lol it doidnt eork')
