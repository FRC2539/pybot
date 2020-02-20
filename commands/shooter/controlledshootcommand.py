from wpilib.command import Command

import robot

class ControlledShootCommand(Command):

    def __init__(self, rpm):
        super().__init__('Controlled Shoot')

        self.requires(robot.shooter)
        self.requires(robot.ballsystem)
        self.requires(robot.intake)

        self.rpm = rpm

    def initialize(self):
        robot.shooter.setRPM(self.rpm)
        robot.shooter.setGoalNetworkTables(self.rpm)

    def execute(self):
        print('rpom ' + str(robot.shooter.getRPM()))
        if (robot.shooter.getRPM() + 10) >= self.rpm:
            robot.ballsystem.runAll()
            robot.intake.intake(0.4)
        else:
            robot.ballsystem.stopAll()

        robot.shooter.updateNetworkTables()

    def end(self):
        robot.shooter.stop()
        robot.ballsystem.stopAll()
        robot.intake.stop()

        robot.shooter.zeroNetworkTables()
