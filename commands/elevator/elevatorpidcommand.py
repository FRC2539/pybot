from wpilib.command.command import Command

import robot

class ElevatorPidCommand(Command):

    def __init__(self, target):
        super().__init__('Elevator Pid')

        self.requires(robot.elevator)
        self.target = target

    def initialize(self):
        if self.target > 2 and self.target < 55:
            robot.elevator.setPosition(self.target)
        else:
            print('target is not within parameters')


    def execute(self):
        #self.position = robot.elevator.getPosition

        pass


    def end(self):
        pass
