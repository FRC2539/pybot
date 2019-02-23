from wpilib.command.command import Command

import robot

class DescendLevelCommand(Command):

    def __init__(self):
        super().__init__('Descend Level')

        self.requires(robot.elevator)
        self.levels = robot.elevator.levels

    def initialize(self):
        pos = robot.elevator.getPosition()
        if pos > self.levels['highBalls']:
            robot.elevator.goToLevel('highBalls')

        elif pos > self.levels['highHatches']:
            robot.elevator.goToLevel('highHatches')

        elif pos > self.levels['midBalls']:
            robot.elevator.goToLevel('midBalls')

        elif pos > self.levels['midHatches']:
            robot.elevator.goToLevel('midHatches')

        elif pos > self.levels['lowBalls']:
            robot.elevator.goToLevel('lowBalls')

        elif pos > self.levels['lowHatches']:
            robot.elevator.goToLevel('lowHatches')

        elif pos > self.levels['floor']:
            robot.elevator.goToFloor()

        else:
            print('rip lol it doidnt eork')
