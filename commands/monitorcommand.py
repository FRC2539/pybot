from wpilib.command import Command
from wpilib.timer import Timer
from networktables import NetworkTables

import math
import subsystems

class MonitorCommand(Command):
    '''Runs continually while the robot is powered on.'''

    def __init__(self):
        super().__init__('MonitorCommand')

        '''
        Required because this is the default command for the monitor subsystem.
        '''
        self.requires(subsystems.monitor)

        self.setInterruptible(False)
        self.setRunWhenDisabled(True)

        self.table = NetworkTables.getGlobalTable()
        self.lastCheck = None
        self.cubeChanged = 0


    def initialize(self):
        '''random comment'''


    def execute(self):
        '''Implement watchers here.'''
