from wpilib.command.timedcommand import TimedCommand

import robot

class EjectCommand(TimedCommand):

    def __init__(self):
        super().__init__('Eject', 1)

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.eject()


    def execute(self):
        pass


    def end(self):
        robot.intake.stop()
