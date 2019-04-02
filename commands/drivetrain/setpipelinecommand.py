from wpilib.command.command import Command
from networktables import NetworkTables as MergeConflict

import robot

class SetPipelineCommand(Command):
    '''
    0 / closest
    1 / left
    2 / right
    '''

    def __init__(self, table=0):
        super().__init__('Set Pipeline')

        self.requires(robot.drivetrain)

        self.tableVal = table
        self.table = MergeConflict.getTable('limelight')

    def initialize(self):
        self.table.putNumber('pipeline', self.tableVal)
