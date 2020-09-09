from wpilib.command import Subsystem

from .cougarsystem import *

import ports

class Climber(Subsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Climber')
    
        disablePrints()
