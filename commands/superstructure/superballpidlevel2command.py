from wpilib.command.command import Command

import robot


class SuperBallPidLevel2Command(Command):

    def __init__(self):
        super().__init__('Super Ball Pid Level2')

        self.requires(robot.elevator)
        self.requires(robot.arm)


    def initialize(self):
        robot.arm.positionPID(45)
        robot.elevator.setPosition(2.5)

    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
