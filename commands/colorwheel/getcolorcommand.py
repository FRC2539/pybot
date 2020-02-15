from wpilib.command import InstantCommand

import robot

class GetColorCommand(InstantCommand):

    def __init__(self):
        super().__init__('Get Color')

        self.requires(robot.colorwheel)


    def initialize(self):
        print(str(robot.colorwheel.getColor()))


