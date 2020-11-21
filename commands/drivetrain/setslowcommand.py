from wpilib.command import InstantCommand

import robot

class SetSlowCommand(InstantCommand):

    def __init__(self, speed=4000):
        super().__init__('Set Fast')

        self.requires(robot.drivetrain)
        
        self.speed = speed

    def initialize(self):
        robot.drivetrain.setSlowSpeed(self.speed)
