from wpilib.command.command import Command

import robot

class AscendLevelCommand(Command):

    def __init__(self):
        super().__init__('Ascend Level')

        self.requires(robot.elevator)
        self.levels = robot.elevator.levels

    def initialize(self):
        pos = robot.elevator.getPosition()
        if pos <= self.levels['lowHatches']:
            robot.elevator.setPosition(self.levels['lowHatches'])

        elif pos <= self.levels['lowBalls']:
            robot.elevator.setPosition(self.levels['lowBalls'])

        elif pos <= self.levels['midHatches']:
            robot.elevator.setPosition(self.levels['midHatches'])

        elif pos <= self.levels['midBalls']:
            robot.elevator.setPosition(self.levels['midBalls'])

        elif pos <= self.levels['highHatches']:
            robot.elevator.setPosition(self.levels['highHatches'])

        elif pos <= self.levels['highBalls']:
            robot.elevator.setPosition(self.levels['highBalls'])


    def end(self):
        robot.elevator.stop()
