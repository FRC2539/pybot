from wpilib.command import Command

from wpilib import Timer

import robot

class ShootWhenReadyCommand(Command):

    def __init__(self, targetRPM):
        super().__init__('Shoot When Ready')

        self.requires(robot.shooter)
        self.requires(robot.balllauncher)

        self.targetRPM = targetRPM

        self.proceed = False

        self.t = Timer()

    def initialize(self):
        robot.shooter.setRPM(self.targetRPM)

    def execute(self):
        if robot.shooter.getRPM() >= self.targetRPM and not self.proceed:
            robot.revolver.setStaticSpeed()
            self.proceed = True
            self.t.start()

        if self.proceed and self.t.get() >= 2: # Wait at least two seconds for revolver spinup.
            robot.balllauncher.launchBalls()
            robot.pneumatics.extendBallLauncherSolenoid()
            self.t.stop()
            self.t.reset()


    def end(self):
        robot.shooter.stopShooter()
        robot.revolver.stopRevolver()
        robot.balllauncher.stopLauncher()
        robot.pneumatics.retractBallLauncherSolenoid()

        self.proceed = False
