from wpilib.command import Command

import subsystems

class ElevateCommand(Command):

    def __init__(self):
        super().__init__('Elevate')

        self.requires(subsystems.shooter)


    def initialize(self):
        subsystems.shooter.up()


    def end(self):
        subsystems.shooter.stop()
