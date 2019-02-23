from wpilib.command.command import Command

import robot

class DescendLevelCommand(Command):

    def __init__(self):
        super().__init__('Descend Level')

        self.requires(robot.elevator)
        self.levels = robot.elevator.levels

    def initialize(self):
        pos = robot.elevator.getPosition()
        if pos >= self.levels['highBalls']:
            robot.elevator.setPosition(self.levels['highBalls'])

        elif self.levels['highHatches'] <= pos < self.levels['highBalls']:
            robot.elevator.setPosition(self.levels['highHatches'])

        elif self.levels['midBalls'] <= pos < self.levels['highHatches']:
            robot.elevator.setPosition(self.levels['highHatches'])

        elif self.levels['midHatches'] <= pos < self.levels['midBalls']:
            robot.elevator.setPosition(self.levels['highHatches'])

        elif self.levels['lowBalls'] <= pos < self.levels['midHatches']:
            robot.elevator.setPosition(self.levels['highHatches'])

        elif self.levels['lowHatches'] <= pos < self.levels['lowBalls']:
            robot.elevator.setPosition(self.levels['highHatches'])

        elif self.levels['lowHatches'] > pos:
            robot.elevator.setPosition(self.levels['floor'])


    def end(self):
        robot.elevator.stop()
