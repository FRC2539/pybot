from wpilib.command.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for hatch')

        self.requires(robot.hatch)


    def execute(self):
        print('hatch ' + str(robot.hatch.hasHatchPanel()))
        if robot.hatch.hasHatchPanel():
            robot.hatch.hold()
        else:
            robot.hatch.stop()
