from wpilib.command.timedcommand import TimedCommand

import robot

class EjectCommand(TimedCommand):

    def __init__(self):
        super().__init__('Eject', 1)

        self.requires(robot.intake)
        self.requires(robot.lights)


    def initialize(self):
        robot.intake.eject()
        robot.lights.solidRed()


    def end(self):
        robot.lights.off()
        robot.intake.stop()
