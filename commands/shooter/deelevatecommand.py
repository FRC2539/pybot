from wpilib.command import Command

import subsystems

class DeelevateCommand(Command):

    def __init__(self):
        super().__init__('Deelevate')

        self.requires(subsystems.shooter)


    def initialize(self):
        subsystems.shooter.down()


    def end(self):
        subsystems.shooter.stop()
