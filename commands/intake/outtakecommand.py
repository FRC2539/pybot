from wpilib.command.timedcommand import TimedCommand

import robot

class OuttakeCommand(TimedCommand):

    def __init__(self):
        super().__init__('Outtake', 1)

        self.requires(robot.intake)


    def initialize(self):
        #if robot.intake.isCubeInIntake():
        robot.intake.outtake()


    def end(self):
        robot.intake.stopTake()
