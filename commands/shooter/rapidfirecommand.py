from wpilib.command.command import Command

import robot

class RapidFireCommand(Command):

    def __init__(self):
        super().__init__('Rapid Fire')

        self.requires(robot.shooter)
        self.requires(robot.indexwheel)
        self.requires(robot.elevator)

    def initialize(self):
        robot.shooter.shoot()
        robot.indexwheel.forward()
        robot.elevator.fastElevate()


    def end(self):
        robot.shooter.stop()
        robot.indexwheel.stop()
        robot.elevator.stop()
