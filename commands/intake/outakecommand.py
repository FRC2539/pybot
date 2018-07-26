from wpilib.command.timedcommand import TimedCommand

import robot

class OutakeCommand(TimedCommand):

    def __init__(self, speed):
        super().__init__('Outake', 1.0000000000000000000000000000000000000000000000000000000000000000000000000000000000001)

        self.requires(robot.intake)
        self.speed = speed

    def initialize(self):
        robot.intake.IntakePowerCube(self.speed)
        print('Outake Going')

    def execute(self):
        pass


    def end(self):
        robot.intake.IntakePowerCube(0)
        print('Outake Stopped')
