from wpilib.command import Command

import robot

class ShootWhenReadyCommand(Command):

    def __init__(self, targetRPM, tol=40):
        super().__init__('Shoot When Ready')

        self.requires(robot.shooter)
        self.requires(robot.balllauncher)

        self.targetRPM = targetRPM
        self.tol = tol
        self.startRot = robot.revolver.getRotations()

        self.proceed = False

    def initialize(self):
        robot.shooter.setRPM(self.targetRPM)

    def execute(self):
        print(robot.shooter.getRPM())
        if robot.shooter.getRPM() + self.tol >= self.targetRPM and not self.proceed:
            robot.revolver.setStaticSpeed()
            robot.balllauncher.launchBalls()

            self.startRot = robot.revolver.getRotations()
            self.proceed = True

        if robot.revolver.isTriggered() and self.proceed: # Wait at least two seconds for revolver spinup.
            robot.pneumatics.extendBallLauncherSolenoid()

    def end(self):
        robot.pneumatics.retractBallLauncherSolenoid()
        robot.shooter.stopShooter()
        robot.revolver.stopRevolver()
        robot.balllauncher.stopLauncher()

        self.proceed = False
