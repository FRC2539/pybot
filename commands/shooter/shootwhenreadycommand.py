from wpilib.command import Command

import robot

class ShootWhenReadyCommand(Command):

    def __init__(self, targetRPM=None, tol=100):
        super().__init__('Shoot When Ready')

        self.requires(robot.balllauncher)
        self.requires(robot.revolver)

        self.targetRPM = 4500#targetRPM
        self.tol = tol
        self.closeShotRPM = robot.limelight.minShooterRPM
        self.swapArea = robot.limelight.swapArea
        self.endPos = None
        
        self.targetLocated = True

    def initialize(self):
        robot.limelight.setPipeline(0)
        
        robot.revolver.resetRevolverEncoder()

        robot.pneumatics.retractBallLauncherSolenoid()

        if self.targetRPM is None and robot.limelight.getTape():
            if robot.limelight.getA() > self.swapArea: # Dummy value. Close shot, static rpm and align the axises. Find the limit tho.
                robot.shooter.setRPM(3800)
                robot.limelight.closeShot = True
            else:
                robot.shooter.setRPM(robot.limelight.generateVelocity(robot.limelight.getA(), self.swapArea))
                robot.limelight.closeShot = False
                
        elif self.targetRPM is None: # We need speed calc, but we don't see it.
            self.targetLocated = False

        else: # We don't want velocity based off of a distance.
            robot.shooter.setRPM(self.targetRPM)

    def execute(self):
        print("rev pos: " + str(robot.revolver.getPosition()))

        if self.targetLocated: # If we found one, lock in and proceed.
            robot.revolver.setStaticSpeed()
            if abs(robot.shooter.getRPM()) + self.tol >= self.targetRPM and robot.revolver.inDropZone():
                robot.balllauncher.launchBalls() 
                robot.pneumatics.extendBallLauncherSolenoid()
                
        elif robot.limelight.getTape(): # Search for a target until we find one.
            if robot.limelight.getA() > self.swapArea: # Dummy value. Close shot, static rpm and align the axises. Find the limit tho.
                robot.shooter.setRPM(3800)
                robot.limelight.closeShot = True
            else:
                robot.shooter.setRPM(robot.limelight.generateVelocity(robot.limelight.getA(), self.swapArea))
                robot.limelight.closeShot = False
                
            self.targetLocated = True

    def end(self):
        robot.pneumatics.retractBallLauncherSolenoid()
        robot.shooter.stopShooter()
        robot.revolver.stopRevolver()
        robot.balllauncher.stopLauncher()

        self.targetLocated = False
        self.endPos = None
        
        robot.revolver.resetRevolverEncoder()

        robot.limelight.setPipeline(1)
