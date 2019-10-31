from wpilib.command.command import Command
from custom.config import Config
import math
import robot

from networktables import NetworkTables

class TestGoToTapeCommand(Command):

    def __init__(self):
        super().__init__('Test Go To Tape')

        self.requires(robot.drivetrain)

        self.tape = Config('limelight/tv', 0)
        self.strafe = Config('limelight/tx', 0)
        self.area = Config('limelight/ta', 0)

        self.tapeLow = Config('limelight-low/tv', 0)
        self.strafeLow = Config('limelight-low/tx', 0)
        self.areaLow = Config('limelight-low/ta', 0)

        self.tapeoffset = Config('DriveTrain/tapeoffset', 0)

        self.nt = NetworkTables.getTable('limelight')
        self.ntLow = NetworkTables.getTable('limelight-low')

        self.pipeID = 1

        self.drivePipeID = 0 # Make this your basic drive pipeline.

        self.x = 0
        self.y = 0
        self.rotate = 0

        self.speedBoost = Config('DriveTrain/tapespeedboost', 1)


    def initialize(self):
        self.wantsHatch = not robot.hatch.hasHatchPanel()

        self.low = False

        if (not self.wantsHatch) and robot.elevator.getPosition() >= 10.0:
            self.low = True

        if not self.low:
            self.nt.putNumber('pipeline', self.pipeID)
            self.ntLow.putNumber('pipeline', 0)
        else:
            self.ntLow.putNumber('pipeline', 1)

        self.count = 0

        self._finished = False



    def execute(self):

        if not self.low:

            if self.tape.getValue() == 1:
                oX = self.strafe.getValue() + self.tapeoffset #0.0 #3.5 #Adjust for off center camera position
                oA = self.area.getValue()

                if (self.count < 4):
                    self.count += 1
                else:
                    self.count = 0
                    self.nt.putNumber('snapshot', 1)


                self.rotate = .05 * oX

                eA = 4.9 - oA

                self.y = eA * .1 * self.speedBoost

                if (self.y < .15) :
                    self.y = .15

                if (self.y > .5):
                    self.y = .5

                robot.drivetrain.move(self.x, self.y, self.rotate)

                if self.wantsHatch:
                    self._finished = robot.hatch.hasHatchPanel()

                elif not self._finished:
                    self._finished = oA >= 4.9

        elif self.low:
            if self.tapeLow.getValue() == 1:
                oX = self.strafeLow.getValue() + self.tapeoffset
                oA = self.areaLow.getValue()

                if (self.count < 4):
                    self.count += 1
                elif (self.count == 4):
                    self.count = 0
                    self.ntLow.putNumber('snapshot', 1)

                eA = 5 - oA

                self.y = .1 * eA * self.speedBoost

                self.rotate = .05 * oX

                if (self.y < .15) :
                    self.y = .15

                if (self.y > .5):
                    self.y = .5

                robot.drivetrain.move(self.x, self.y, self.rotate)

                if not self._finished:
                    self._finished = oA >= 5

            if self._finished:
                robot.lights.solidGreen()
            else:
                robot.lights.solidBlue()

        else:
            robot.lights.solidRed()
            print('No vision target found!')
            robot.drivetrain.move(0, 0, 0)

    def isFinished(self):
        return self._finished


    def end(self):
        robot.drivetrain.move(0, 0, 0)

        self.nt.putNumber('pipeline', 0)
        self.ntLow.putNumber('pipeline', 0)
        #if not self.low:
            #self.nt.putNumber('snapshot', 1)
        #else:
            #self.ntLow.putNumber('snapshot', 1)

        robot.lights.off()
        pass
