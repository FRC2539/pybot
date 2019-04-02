from wpilib.command.command import Command
from commandbased import flowcontrol as fc
from networktables import NetworkTables as nt
from custom.config import Config

import robot


class AutonomousMeasureCommand(Command):

    def __init__(self):
        super().__init__('Autonomous Measure')

        self.requires(robot.drivetrain)

        nt.initialize(server='10.25.39.2')
        self.table = nt.getTable('DriveTrain')
        self.table.putBoolean('DriveTrain/recordingMovements', False)

    def initialize(self):
        self.table.putBoolean('DriveTrain/recordingMovements', True)
        print('self.recording is True')

        self.ticksPerInch = Config('DriveTrain/ticksPerInch')

        robot.drivetrain.resetEncoders()
        self.previousPosition = robot.drivetrain.getPositions()
        self.movements = {}

    def execute(self):
        trueStraight = []
        #Read values
        currentPos = robot.drivetrain.getPositions()
        for position, prevPosition in zip(currentPos, self.previousPosition):
            if position - 1.0 > prevPosition or prevPosition > position + 1.0:
                trueStraight.append(position)

        #test for trueForwards
        if len(trueStraight) == 4:
            self.inchesStraight = int((currentPos[0] - self.previousPosition[0]) / self.ticksPerInch)
            self.movements['MoveCommand'] = self.inchesStraight
            #TODO: receive the total move in a motion

        #Reset
        self.previousPosition = robot.drivetrain.getPositions()
        print(' previous position ' + str(self.previousPosition))
    def end(self):
        print(str(self.movements))
        print('self.recording is False')
        print(str(self.movements))
        return self.movements

        self.table.putBoolean('DriveTrain/recordingMovements', False)
