from wpilib.command.timedcommand import TimedCommand

import robot

class HatchEjectCommand(TimedCommand):

    def __init__(self):
        super().__init__('Hatch Eject', 1)

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.hatchEject()


    def end(self):
        robot.intake.hasCargo = False
        robot.intake.stop()
