from wpilib.command import Command

import robot

class CamTranTurretLimelight(Command):

    def __init__(self):
        super().__init__('Cam Tran Turret Limelight')

        self.requires(robot.turret)

    def initialize(self):
        robot.turret.stop()

    def execute(self):
        diff = (robot.limelight.getX() / 360) * 4096 # Puts it into ticks.

        #robot.turret.followTarget(diff, robot.limelight.get3D_Z())
        robot.turret.followTargetPID(diff + robot.turret.getPosition()) # Try this out tonight.

        print('At: ' +  str(robot.turret.getPosition()))

    def isFinished(self):
        if (abs(robot.limelight.getX()) < 0.1) or (robot.turret.outOfRange()):
            return True

    def end(self):
        robot.turret.stop()
