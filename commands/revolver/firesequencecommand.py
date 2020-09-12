from wpilib.command import Command

import robot


class FireSequenceCommand(Command):

    def __init__(self):
        super().__init__('Fire Sequence')

        self.requires(robot.revolver)
        self.requires(robot.balllauncher)

        robot.revolver.sequenceEngaged = False
        self.proceed = False

    def initialize(self):
        self.proceed = False
        
        robot.revolver.sequenceEngaged = True
        
        robot.revolver.resetRevolverEncoder()
        robot.pneumatics.retractBallLauncherSolenoid()

        robot.revolver.setStaticSpeed()

        self.startPos = robot.revolver.getPosition()
        self.goTo = self.startPos - 10 
        
        if self.goTo < 0:
            self.goTo += 360

    def execute(self):
        print('\ngoto\n' + str(self.goTo))
        print('\npos\n ' + str(robot.revolver.getPosition())) 
        
        if abs(self.goTo - robot.revolver.getPosition()) <= 5:
            self.proceed = True
            
        if robot.shooter.atGoal and robot.revolver.inDropZone() and self.proceed:
            robot.balllauncher.launchBalls()
            robot.pneumatics.extendBallLauncherSolenoid()

    def end(self):
        robot.revolver.sequenceEngaged = False
        self.proceed = False

        robot.pneumatics.retractBallLauncherSolenoid()
        robot.balllauncher.stopLauncher()
        robot.revolver.stopRevolver()
