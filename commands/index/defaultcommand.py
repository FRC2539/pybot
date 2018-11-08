from wpilib.command import Command

import subsystems

class DefaultCommand(Command):
    '''Describe what this command does.'''

    def __init__(self):
        super().__init__('Default for Index')

        self.requires(subsystems.index)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
