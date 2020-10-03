from wpilib.command import Command

import robot


class MakeTheRobotShootBallsAndOnlyShootBallsCommand(Command):
    
    # extremely basic command that just makes the robot shoot

    def __init__(self):
        super().__init__('Make The Robot Shoot Balls And Only Shoot Balls')

        self.requires(robot.shooter)


    def initialize(self):
        #print("shooting balls and only balls")
        
        self.startPos = robot.revolver.getPosition()
        self.goTo = self.startPos - 10 
        
        self.proceed = False
        
        if self.goTo < 0:
            self.goTo += 360
        pass


    def execute(self):
        #print("executing the shooting of the balls")
        robot.shooter.setRPM(4500) # placeholder value
        robot.revolver.setStaticSpeed()
        
        robot.shooter.updateNetworkTables()
        
        if abs(self.goTo - robot.revolver.getPosition()) <= 5:
            print('proceed')
            self.proceed = True

        if robot.revolver.inDropZone() and self.proceed:
            print('shoot')
            robot.revolver.setStaticSpeed()
            robot.balllauncher.launchBalls()
            robot.pneumatics.extendBallLauncherSolenoid()

        pass


    def end(self):
        print("no longer shooting balls")
        robot.revolver.sequenceEngaged = False
        self.proceed = False
        
        robot.shooter.setRPM(0)
        robot.pneumatics.retractBallLauncherSolenoid()
        robot.revolver.stopRevolver()
        robot.balllauncher.stopLauncher()
        robot.shooter.zeroNetworkTables()
