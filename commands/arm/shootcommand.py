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

        self.tape = Config('limelight-low/tv', 0)
        self.x = Config('limelight-low/tx', 0)
        self.y = Config('limelight-low/ty', 0)

        self.nt = NetworkTables.getTable('limelight-low')




    def initialize(self):
        self.speed = -4850
        #robot.arm.shoot(-4850)
        y = self.y.getValue() + 29
        h = 68

        self.distance = h / math.tan(math.radians(y))



    def execute(self):
        print(robot.arm.encoder.getVelocity())
        robot.arm.shoot(-4100)
        self.rotate = self.x.getValue() * .05
        #if (abs(self.rotate)<.15):
         #   self.rotate = math.copysign(.15, self.rotate)
        if (abs(self.rotate) > .3):
            self.rotate = math.copysign(.3, self.rotate)
        robot.drivetrain.move(0, 0, self.rotate)


    def end(self):
        robot.arm.stop()
