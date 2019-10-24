from wpilib.command.command import Command
from custom.config import Config
import math
import robot

from networktables import NetworkTables
class PsuedoVisionMoveCommand(Command):

    def __init__(self, pipeID=1):
        super().__init__('Psuedo Vision Move')

        self.requires(robot.drivetrain)
        self.requires(robot.hatch)

        self.tape = Config('limelight/tv', 0)
        self.strafe = Config('limelight/tx', 0)
        self.distance = Config('limelight/ty', 0)

        self.tapeLow = Config('limelight-low/tv', 0)
        self.strafeLow = Config('limelight-low/tx', 0)
        self.distanceLow = Config('limelight-low/ty', 0)

        self.tapeoffset = Config('DriveTrain/tapeoffset', 0)

        self.nt = NetworkTables.getTable('limelight')
        self.ntLow = NetworkTables.getTable('limelight-low')

        self.pipeID = pipeID

        self.drivePipeID = 0 # Make this your basic drive pipeline.

        self.x = 0
        self.y = 0
        self.rotate = 0

        self.speedBoost = Config('DriveTrain/tapespeedboost', 1)

        self.needHatch = False

        self.originallyFieldOriented = True

    def initialize(self):
        if robot.hatch.hasHatchPanel():
            self.needHatch = False
        else:
            self.needHatch = True

    def execute(self):
        if self.tape.getValue() == 1:
            x = self.strafe.getValue()

            self.x = math.copysign((x * 4) / 100, x)

            if abs(self.x) > 0.35:
                self.rotate = math.copysign(0.35, self.x)
            elif abs(self.x) <= 1.0:
                self.rotate = (x / 10.0)/1.5
            elif abs(self.x) > 1.0 and abs(self.x) < 0.2:
                self.rotate = math.copysign(0.1, x)/1.5

            self.rotate = self.rotate * 2

            robot.drivetrain.move(0, 0.2, self.rotate)

    def isFinished(self):
        if self.needHatch:
            return robot.hatch.hasHatchPanel()
        else:
            return not robot.hatch.hasHatchPanel()

    def end(self):
        robot.drivetrain.stop()
