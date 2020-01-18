from wpilib.command.command import Command
from custom.config import Config
from networktables import NetworkTables
import math

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




    def initialize(self):
        self.speed = -4850
        robot.arm.shoot(self.speed)
        #y = self.y.getValue() + 29
        #h = 68

        #self.distance = h / math.tan(math.radians(y))



    def execute(self):
        print(robot.arm.encoder.getVelocity())
        #robot.arm.shoot()
        #self.rotate = self.x * .05
        #robot.drivetrain.move(0, 0, self.rotate)


    def end(self):
        robot.arm.stop()
