from wpilib.command.timedcommand import TimedCommand

import robot

class EjectCommand(TimedCommand):

    def __init__(self):
        super().__init__('Eject', 1)

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.eject()


    def end(self):
        robot.lights.off()
        robot.intake.stop()
