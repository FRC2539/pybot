from .debuggablesubsystem import DebuggableSubsystem

import ports


class Pneumatics(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Pneumatics')
