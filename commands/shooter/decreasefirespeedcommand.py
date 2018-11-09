from wpilib.command.instantcommand import InstantCommand

import robot

class DecreaseFireSpeedCommand(InstantCommand):

    def __init__(self):
        super().__init__('Decrease Fire Speed')

        self.requires(robot.shooter)

    def initialize(self):
        robot.shooter.decreaseSpeed()

    def end(self):
        robot.shooter.stop()
