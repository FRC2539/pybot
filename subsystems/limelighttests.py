from .debuggablesubsystem import DebuggableSubsystem
from networktables import NetworkTables as nt

from custom.config import Config

import ports


class LimelightTests(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('LimelightTests')

        self.limelight = nt.getTable('limelight')
        self.tapeVal = Config('limelight/tv', 0)
        self.tapeY = Config('limelight/ty', 0)


 #   def initDefaultCommand(self):
  #      from commands.limelighttests.autointakecommand import AutoIntakeCommand

   #     self.setDefaultCommand(AutoIntakeCommand(4)) # Pipeline


    def seesCargo(self):
        if self.tapeVal.getValue() == 1:
            return True
        else:
            return False


    def withinRange(self):
        if float(self.tapeY.getValue()) > -12.0:
            return True
        else:
            return False


    def getY(self):
        return self.tapeY.getValue()


    def setPipeline(self, pipeline):
        self.limelight.putNumber('pipeline', pipeline)
