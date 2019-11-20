from wpilib.command.command import Command

import robot

class ArmPidCommand(Command):

    def __init__(self, target):
        super().__init__('Arm Pid')

        self.requires(robot.arm)
        self.target = target


    def initialize(self):
        robot.arm.positionPID(self.target)


    def execute(self):
        pass


    def end(self):
        pass
