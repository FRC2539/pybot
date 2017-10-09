from wpilib.command import Command

import subsystems

class StayClosedCommand(Command):

    def __init__(self):
        super().__init__('StayClosedCommand')

        self.requires(subsystems.feeder)

    def initialize(self):
        subsystems.feeder.close()

    def execute(self):
        if not subsystems.feeder.isClosed():
            subsystems.feeder.close()
