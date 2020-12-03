from wpilib.command import Command

import robot


class FireSequenceCommand(Command):

    def __init__(self, autoEnd):
        super().__init__('Fire Sequence')

        self.requires(robot.revolver)
        self.requires(robot.balllauncher)

        robot.revolver.sequenceEngaged = False
        self.proceed = False
        self.beganLaunching = False
        self.autoEnd = autoEnd

    def initialize(self):
        self.proceed = False
        
        robot.revolver.sequenceEngaged = True
        
        robot.revolver.resetRevolverEncoder()
        
        robot.revolver.setStaticSpeed()

        self.startPos = robot.revolver.getPosition()
        self.goTo = self.startPos - 10 
        
        if self.goTo < 0:
            self.goTo += 360

    def execute(self):
        if abs(self.goTo - robot.revolver.getPosition()) <= 5 and robot.turret.onTarget and not self.proceed:# and all(abs(x) <= 10 for x in robot.drivetrain.getSpeeds()):
            self.proceed = True
        
        if robot.shooter.atGoal and robot.revolver.inDropZone() and self.proceed:
            robot.revolver.setStaticSpeed()
            robot.balllauncher.launchBalls()
            robot.pneumatics.extendBallLauncherSolenoid()
            self.beganLaunching = True
            self.loopedOnce = False
            self.shootUntil = robot.revolver.getPosition() + 15 # Invert if need to reverse.
            self.lastPos = robot.revolver.getPosition()
            
    def isFinished(self):
        if self.beganLaunching and self.autoEnd:
            if self.loopedOnce:
                if robot.revolver.getPosition() > self.shootUntil: # Might need to invert. 
                    return True # We done. 
            else:
                if self.lastPos > robot.revolver.getPosition(): # The revolver just went from 359 to 0. Might need to invert.
                    self.loopedOnce = True 
                    
                self.lastPos = robot.revolver.getPosition()
        
        return False
    
    def isFinishedV2(self): # I thought of an issue; if the grabber skips a ball, it won't shoot it. Try both?
        if self.beganLaunching and self.autoEnd:
            if not robot.revolver.sawItAt() == -1:
                lastSeen = robot.revolver.sawItAt()
                self.loopedOnce = False # Found a new target, so reset this. 
            
            if self.loopedOnce:
                if robot.revolver.getPosition() > self.shootUntil: # Might need to invert. 
                    return True # We done. 
            else:
                if self.lastPos > robot.revolver.getPosition(): # The revolver just went from 359 to 0. Might need to invert.
                    self.loopedOnce = True 
                    
                self.lastPos = robot.revolver.getPosition()
        
        return False

    def end(self):
        robot.revolver.sequenceEngaged = False
        self.proceed = False
        self.beganLaunching = False
        self.loopedOnce = False

        robot.pneumatics.retractBallLauncherSolenoid()
        robot.balllauncher.stopLauncher()
        robot.revolver.stopRevolver()
