from wpilib.command import Command

import robot

class CamTranTurretLimelight(Command):

    def __init__(self):
        super().__init__('Cam Tran Turret Limelight')

        self.requires(robot.turret)

    def initialize(self):
        robot.turret.stop()

    def execute(self):
        print(robot.limelight.get3D_Yaw())
        diff = (robot.limelight.getX() / 360) * 4096 # Puts it into ticks.

        robot.turret.followTarget(robot.turret.getPosition() + diff)

    def end(self):
        robot.turret.stop()
