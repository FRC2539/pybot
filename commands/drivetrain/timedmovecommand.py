from wpilib.command.timedcommand import TimedCommand

import robot

class TimedMoveCommand(TimedCommand):

    def __init__(self, timeout, speed):
        super().__init__('Timed Move', timeout)

        self.requires(robot.drivetrain)
        self.speed = speed

    def initialize(self):
        robot.drivetrain.move(0, self.speed, 0)


    def execute(self):
        pass


    def end(self):
        robot.drivetrain.move(0,0,0)
