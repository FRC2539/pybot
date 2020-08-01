from wpilib.command import Command

import robot
import math

class TurretLimelightCommand(Command):

    def __init__(self):
        super().__init__('Turret Limelight')

        self.requires(robot.turret)

    def initialize(self):
        robot.limelight.setPipeline(1)

        robot.turret.stop()
        robot.turret.motor.setSensorPhase(True) # I need to invert this stuff for whatever reason.
        robot.turret.motor.setInverted(True)

        self.goal = robot.turret.getPosition() + (robot.limelight.getX() / 360) * 4096

    def execute(self):
        robot.turret.followTargetPID(self.goal)

    def isFinished(self):
        if ((abs(robot.limelight.getX()) < 0.1) and (robot.limelight.getTape())) or (robot.turret.outOfRange()):
            return True

        return False

    def end(self):
        robot.turret.stop()
        robot.turret.motor.setSensorPhase(False) # I need to invert this stuff for whatever reason.
        robot.turret.motor.setInverted(False)

        robot.limelight.setPipeline(0)
