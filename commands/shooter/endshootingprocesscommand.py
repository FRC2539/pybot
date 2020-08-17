from wpilib.command import InstantCommand

import robot

class EndShootingProcessCommand(InstantCommand):

    def __init__(self):

        # This in theory should call the end methods of any command using these systems.

        super().__init__('End Shooting Process')

        self.requires(robot.shooter)
        self.requires(robot.limelight)
        self.requires(robot.hood)
        self.requires(robot.turret)
        self.requires(robot.revolver)
        self.requires(robot.balllauncher)

    def initialize(self):
        robot.limelight.setPipeline(1)
