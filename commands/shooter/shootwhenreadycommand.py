from wpilib.command import Command

import robot

class ShootWhenReadyCommand(Command):

    def __init__(self, targetRPM=None, tol=40):
        super().__init__('Shoot When Ready')

        self.requires(robot.balllauncher)
        self.requires(robot.revolver)

        self.targetRPM = targetRPM
        self.tol = tol
        self.startRot = 0

        self.proceedVal = False
        self.targetLocated = True

    def initialize(self):

        self.proceedVal = False
        self.startRot = 0
        robot.revolver.resetRevolverEncoder()

        if self.targetRPM is None and robot.limelight.getTape(): # We need speed calc, and we see it.
            self.targetRPM = robot.shooter.generateVelocity(robot.limelight.get3D_Z()) # May be the wrong method; look on the web config later.
            robot.shooter.setRPM(self.targetRPM)

        elif self.targetRPM is None: # We need speed calc, but we don't see it.
            self.targetLocated = False

        else: # We don't want velocity based off of a distance.
            print('here')
            robot.shooter.setRPM(self.targetRPM)

    def execute(self):

        print('i am stupid')

        if self.targetLocated: # If we found one, lock in and proceed.
            if robot.shooter.getRPM() + self.tol >= self.targetRPM and not self.proceedVal:
                robot.revolver.setStaticSpeed()
                robot.balllauncher.launchBalls()

                self.startRot = robot.revolver.getRotations()
                self.proceedVal = True

            elif robot.revolver.isTriggered() and abs(self.startRot - robot.revolver.getRotations()) >= 3 \
                and self.proceedVal: # Wait at least three rotations for revolver spinup.

                robot.pneumatics.extendBallLauncherSolenoid()

        elif robot.limelight.getTape(): # Search for a target until we find one
            self.targetRPM = robot.shooter.generateVelocity(robot.limelight.get3D_Z()) # May be the wrong method; look on the web config later.
            robot.shooter.setRPM(self.targetRPM)

            self.targetLocated = True

    def end(self):
        robot.pneumatics.retractBallLauncherSolenoid()
        robot.shooter.stopShooter()
        robot.revolver.stopRevolver()
        robot.balllauncher.stopLauncher()

        self.proceedVal = False

        self.startRot = 0
        robot.revolver.resetRevolverEncoder()
