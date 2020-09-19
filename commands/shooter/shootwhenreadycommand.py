from wpilib.command import Command

import robot

class ShootWhenReadyCommand(Command):

    def __init__(self, targetRPM=None, tol=300):
        super().__init__('Shoot When Ready')

        self.requires(robot.balllauncher)
        self.requires(robot.revolver)

        self.targetRPM = 6000#targetRPM
        self.tol = tol
        self.closeShotRPM = robot.limelight.minShooterRPM
        self.swapArea = robot.limelight.swapArea
        self.endPos = None
        
        self.targetLocated = True

    def initialize(self,ignoreLimelight=False):
        self.ignoreLimelight = ignoreLimelight
        
        robot.revolver.resetRevolverEncoder()

        robot.pneumatics.retractBallLauncherSolenoid()
        
        if not self.ignoreLimelight: #we don't need to do any limelight stuff if ignoreLimelight is true
            robot.limelight.setPipeline(0)
            
        robot.shooter.setRPM(self.targetRPM)

    def execute(self):
        #print("rev pos: " + str(robot.revolver.getPosition()))

        if self.targetLocated or self.ignoreLimelight: # If we found one (or don't need one), lock in and proceed.
            robot.revolver.setStaticSpeed()
            #print("located targeb; rpm = " + str(robot.shooter.getRPM()) + "; target rpm = " + str(self.targetRPM) + " (" + str(self.tol) + " tolerance)")
            if abs(robot.shooter.getRPM()) + self.tol >= self.targetRPM and robot.revolver.inDropZone():
                robot.balllauncher.launchBalls() 
                robot.pneumatics.extendBallLauncherSolenoid()
                #print("Heck")
                
        elif robot.limelight.getTape(): # Search for a target until we find one; will not run if ignoreLimelight is true.
            #print('weird')
            if robot.limelight.getA() > self.swapArea: # Dummy value. Close shot, static rpm and align the axises. Find the limit tho.
                robot.shooter.setRPM(3800)
                robot.limelight.closeShot = True
                #print('closeshot')
            else:
                robot.shooter.setRPM(robot.limelight.generateVelocity(robot.limelight.getA(), self.swapArea))
                robot.limelight.closeShot = False
                #print("farshot")
                
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
