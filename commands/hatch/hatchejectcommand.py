from wpilib.command.timedcommand import TimedCommand

import robot

class HatchEjectCommand(TimedCommand):

    def __init__(self):
        super().__init__('Hatch Eject', 1)

        self.requires(robot.hatch)


    def initialize(self):
        print('eject')
        robot.hatch.eject()
        robot.lights.solidRed()


    def end(self):
        robot.lights.off()
        robot.hatch.hasHatch = False
        robot.hatch.stop()
