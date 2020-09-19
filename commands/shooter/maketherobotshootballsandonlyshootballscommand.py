from wpilib.command import Command

import robot


class MakeTheRobotShootBallsAndOnlyShootBallsCommand(Command):
    
    # extremely basic command that just makes the robot shoot

    def __init__(self):
        super().__init__('Make The Robot Shoot Balls And Only Shoot Balls')

        self.requires(robot.shooter)


    def initialize(self):
        #print("shooting balls and only balls")
        pass


    def execute(self):
        #print("executing the shooting of the balls")
        robot.shooter.setRPM(4500) # placeholder value
        robot.revolver.setStaticSpeed()
        robot.pneumatics.extendBallLauncherSolenoid()
        pass


    def end(self):
        #print("no longer shooting balls")
        robot.shooter.setRPM(0)
        robot.pneumatics.retractBallLauncherSolenoid()
        robot.revolver.stopRevolver()
        pass
