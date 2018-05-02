from wpilib.command.command import Command

import robot

class ForcedLowerCommand(Command):

    def __init__(self):
        super().__init__('Override Elevator')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.enableLowerLimit(False)
        robot.elevator.down()


    def end(self):
        robot.elevator.stop()
        robot.elevator.enableLowerLimit(True)
        if robot.elevator.getHeight() < 0:
            robot.elevator.reset()
