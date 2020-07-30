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

        self.proceedVal = False

    def initialize(self):
        robot.shooter.setRPM(self.targetRPM)

    def execute(self):
        print(robot.shooter.getRPM())
        if robot.shooter.getRPM() + self.tol >= self.targetRPM and not self.proceedVal:
            robot.revolver.setStaticSpeed()
            robot.balllauncher.launchBalls()

            self.startRot = robot.revolver.getRotations()
            self.proceedVal = True

        elif robot.revolver.isTriggered() and robot.revolver.getRotations() >= self.startRot + 2 \
            and self.proceedVal: # Wait at least two rotations for revolver spinup.

            robot.pneumatics.extendBallLauncherSolenoid()

    def end(self):
        robot.pneumatics.retractBallLauncherSolenoid()
        robot.shooter.stopShooter()
        robot.revolver.stopRevolver()
        robot.balllauncher.stopLauncher()

        self.proceedVal = False
