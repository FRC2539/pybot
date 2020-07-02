from wpilib.command import Command

import robot

class CamTranTurretLimelight(Command):

    def __init__(self):
        super().__init__('Cam Tran Turret Limelight')

        self.requires(robot.turret)

    def initialize(self):
        robot.turret.stop()
        robot.turret.motor.setSensorPhase(True) # I need to invert this stuff for whatever reason.
        robot.turret.motor.setInverted(True)

        self.goal = robot.turret.getPosition() + (robot.limelight.getX() / 360) * 4096 # Puts it into ticks, and sets a position once!

    def execute(self):
        robot.turret.followTargetPID(self.goal) # Try this out tonight.

        print('Goal: ' + str(self.goal)) # GOAL SHOULD NOT BE CHANGING.

        print('At: ' +  str(robot.turret.getPosition()))

    def isFinished(self):
        print('x' + str(robot.limelight.getX()))
        if ((abs(robot.limelight.getX()) < 0.1) and (robot.limelight.getTape())) or (robot.turret.outOfRange()):
            return True

        return False

    def end(self):
        robot.turret.stop()
        robot.turret.motor.setSensorPhase(False)
        robot.turret.motor.setInverted(False)
