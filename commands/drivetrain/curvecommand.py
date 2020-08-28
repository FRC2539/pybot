from wpilib.command import Command

import robot
import math


class CurveCommand(Command):

    def __init__(self):
        super().__init__('Curve')

        self.requires(robot.drivetrain)



    def initialize(self):
        self.degrees = 90
        self.radius = 48
        self.distanceL = ( self.degrees / 360 ) * 2 * ( self.radius + 12 ) * math.pi
        self.distanceR = ( self.degrees / 360 ) * 2 * ( self.radius - 12 ) * math.pi
        self.speedRatio = self.distanceL / self.distanceR
        self.startDistanceL = robot.basedrive.getposition(0)
        self.startDistanceR = robot.basedrive.getposition(1)
        self.finishDistanceL = self.startDistanceL + self.distanceL
        self.finishDistanceR = self.startDistanceR + self.distanceR


    def execute(self):
        self.currentDistanceL = robot.basedrive.getposition(0)
        self.currentDistanceR = robot.basedrive.getposition(1)
        self.speedL = ( self.finishDistanceL - self.currentDistanceL ) * .1
        self.speedR = ( self.finishDistanceR - self.currentDistanceR ) * .1



    def end(self):
        pass
