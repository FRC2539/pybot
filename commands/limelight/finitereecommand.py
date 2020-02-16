from wpilib.command import Command

import robot

class finiteReeCommand(Command):

    def __init__(self):
        super().__init__('finite Ree')

        self.requires(robot.limelight)


    def initialize(self):
        print('re')


    def execute(self):
        print('eee')


    def end(self):
        pass
