from wpilib.command.instantcommand import InstantCommand
from networktables import NetworkTables

import robot

class SetPipelineCommand(InstantCommand):
    '''
    0 / closest
    1 / left
    2 / right
    '''

    def __init__(self, pipeline):
        super().__init__('Set Pipeline')

        self.setRunWhenDisabled(True)

        self.pipeline = pipeline
        self.table = NetworkTables.getTable('limelight')


    def initialize(self):
        self.table.putNumber('pipeline', self.pipeline)
