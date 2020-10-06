from wpilib.command import Command

import robot

class KickCommand(Command):

    def __init__(self):
        super().__init__('Kick Command')

        self.requires(robot.intake)

    def initialize(self):
        robot.intake.stopIntake()

        if robot.pneumatics.isIntakeLowered():
            robot.pneumatics.retractIntakeSolenoid()
            robot.intake.stopIntake()
        else:
            robot.pneumatics.extendIntakeSolenoid()
            robot.intake.kickBalls()
