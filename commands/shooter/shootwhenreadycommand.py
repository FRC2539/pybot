from wpilib.command import Command

import robot

class ShootWhenReadyCommand(Command):

    def __init__(self, targetRPM=None, tol=100):
        super().__init__('Shoot When Ready')

        self.requires(robot.balllauncher)
        self.requires(robot.revolver)

        self.targetRPM = targetRPM
        self.tol = tol
        self.startRot = 0

        self.proceedVal = False
        self.targetLocated = True

    def initialize(self):
        robot.limelight.setPipeline(0)

        self.proceedVal = False
        self.startRot = 0
        robot.revolver.resetRevolverEncoder()

        robot.pneumatics.retractBallLauncherSolenoid()

        print('og dist ' + str(robot.limelight.bensDistance()))

        if self.targetRPM is None and robot.limelight.getTape(): # We need speed calc, and we see it.
            self.targetRPM = robot.limelight.generateVelocity(robot.limelight.bensDistance()) # May be the wrong method; look on the web config later.
            robot.shooter.setRPM(self.targetRPM)

        elif self.targetRPM is None: # We need speed calc, but we don't see it.
            self.targetLocated = False

        else: # We don't want velocity based off of a distance.
            print('here')
            robot.shooter.setRPM(self.targetRPM)

    def execute(self):
        print("rev pos: " + str(robot.revolver.getPosition()))

        if self.targetLocated: # If we found one, lock in and proceed.
            print(robot.shooter.getRPM())
            print('target ' + str(self.targetRPM))
            print('distance ' + str(robot.limelight.bensDistance()))
            print('calc distance ' +str(robot.limelight.calcDistanceGood()))
            robot.revolver.setStaticSpeed()
            if abs(robot.shooter.getRPM()) + self.tol >= self.targetRPM and not self.proceedVal:
                robot.revolver.setStaticSpeed()
               # robot.balllauncher.launchBalls() TEST

                self.proceedVal = True

            elif robot.revolver.inDropZone() and self.proceedVal:
                robot.revolver.stopRevolver() # TEST

                #for x in range(10000): # TEST
                #    print('ahh')

                robot.revolver.setStaticSpeed()



                #for x in range(2500): # TEST
                #    print('ahh')



                robot.balllauncher.launchBalls() # END TEST

                for x in range(200): # TEST
                    print('run launcher delay')

                robot.pneumatics.extendBallLauncherSolenoid()

        elif robot.limelight.getTape(): # Search for a target until we find one
            self.targetRPM = robot.limelight.generateVelocity(robot.limelight.bensDistance()) # May be the wrong method; look on the web config later.
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

        robot.limelight.setPipeline(1)
