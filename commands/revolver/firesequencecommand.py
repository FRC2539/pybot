from wpilib.command import Command

import robot


class FireSequenceCommand(Command):

    def __init__(self):
        super().__init__('Fire Sequence')

        self.requires(robot.revolver)
        self.requires(robot.balllauncher)

        robot.revolver.sequenceEngaged = False

    def initialize(self):
        robot.revolver.sequenceEngaged = True
        
        robot.revolver.resetRevolverEncoder()
        robot.pneumatics.retractBallLauncherSolenoid()

        robot.revolver.setStaticSpeed()

    def execute(self):
        if robot.shooter.atGoal and robot.revolver.inDropZone():
            robot.balllauncher.launchBalls()
            robot.pneumatics.extendBallLauncherSolenoid()

    def end(self):
        robot.revolver.sequenceEngaged = False

        robot.pneumatics.retractBallLauncherSolenoid()
        robot.balllauncher.stopLauncher()
        robot.revolver.stopRevolver()
