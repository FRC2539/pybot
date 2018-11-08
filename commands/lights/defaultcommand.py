from wpilib.command import Command

import subsystems

class DefaultCommand(Command):
    '''Describe what this command does.'''

    def __init__(self):
        super().__init__('Default for Lights')

        self.requires(subsystems.lights)


    def initialize(self):
        subsystems.lights.solidOrange()
