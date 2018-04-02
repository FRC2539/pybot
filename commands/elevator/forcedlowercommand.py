from wpilib.command.command import Command

import subsystems

class ForcedLowerCommand(Command):

    def __init__(self):
        super().__init__('Override Elevator')

        self.requires(subsystems.elevator)


    def initialize(self):
        subsystems.elevator.enableLowerLimit(False)
        subsystems.elevator.down()


    def end(self):
        subsystems.elevator.stop()
        subsystems.elevator.enableLowerLimit(True)
        if subsystems.elevator.getHeight() < 0:
            subsystems.elevator.reset()
