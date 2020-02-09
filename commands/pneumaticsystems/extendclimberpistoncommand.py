from wpilib.command import Command

import robot

class ExtendClimberPistonCommand(Command):

    def __init__(self):
        super().__init__('Extend Climber Piston')

        self.requires(robot.pneumaticsystems)

    def initialize(self):
        robot.pneumaticsystems.extendClimberPiston()

    def end(self):
        robot.pneumaticsystems.retractClimberPiston()
