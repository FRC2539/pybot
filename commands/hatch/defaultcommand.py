from wpilib.command.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for hatch')

        self.requires(robot.hatch)


    def execute(self):
        if robot.hatch.hasSecureHatchPanel():
            robot.hatch.hold()
            robot.lights.solidOrange()
            #print("Running")
        elif robot.hatch.hasHatchPanel():
            robot.hatch.grab()
            #print('error')
        else:
            robot.hatch.stop()
            #print('idc')
