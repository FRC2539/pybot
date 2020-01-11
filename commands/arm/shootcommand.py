from wpilib.command.command import Command

import robot

class ShootCommand(Command):

    def __init__(self):
        super().__init__('Shoot')

        self.requires(robot.arm)
        self.requires(robot.drivetrain)

        self.tape = Config('limelight/tv', 0)
        self.x = Config('limelight/tx', 0)
        self.y = Config('limelight/ty', 0)

        self.nt = NetworkTables.getTable('limelight')
        self.distance =


    def initialize(self):
        pass


    def execute(self):
        robot.arm.shoot(self.speed)


    def end(self):
        pass
