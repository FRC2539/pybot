from wpilib.command.instantcommand import InstantCommand

import robot

class IncreaseFireSpeedCommand(InstantCommand):

    def __init__(self):
        super().__init__('Increase Fire Speed')

        self.requires(robot.shooter)


    def initialize(self):
        robot.shooter.increaseSpeed()

    def end(self):
        robot.shooter.stop()
