from wpilib.command import Command

import robot
import math

class TurretLimelightCommand(Command):

    def __init__(self):
        super().__init__('Turret Limelight')

        self.requires(robot.turret)

        self.offset = 20

    def initialize(self):
        robot.limelight.setPipeline(0)

        robot.turret.stop()
        robot.turret.motor.setSensorPhase(True) # I need to invert this stuff for whatever reason.
        robot.turret.motor.setInverted(True)

        self.goal = robot.turret.getPosition() + (robot.limelight.getX() / 360) * 4096

    def execute(self):
        if robot.turret.turretActiveMode:
            self.goal = robot.turret.getPosition() - (robot.limelight.getX() / 360) * 4096

        robot.turret.followTargetPID(self.goal - self.offset)

    def isFinished(self):
        if ((abs(robot.limelight.getX()) < 0.001) and (robot.limelight.getTape())) or (robot.turret.outOfRange()):
            return True

        return False

    def end(self):
        robot.turret.stop()
        robot.turret.motor.setSensorPhase(False) # I need to invert this stuff for whatever reason.
        robot.turret.motor.setInverted(False)

        robot.limelight.setPipeline(1)
