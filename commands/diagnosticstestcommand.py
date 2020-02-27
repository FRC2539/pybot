from wpilib.command import InstantCommand

from networktables import NetworkTables as nt

from wpilib import Timer

import robot

class DiagnosticsTestCommand(InstantCommand):

    def __init__(self):
        super().__init__('Diagnostics Test')

        self.requires(robot.ballsystem)
        self.requires(robot.intake)
        self.requires(robot.shooter)
        self.requires(robot.drivetrain)

        self.timer = Timer()

        self.table = nt.getTable('Diagnostics')

    def initialize(self):
        self.records = 'Record: '

        self.timer.start()
        self.table.putString('Status', 'Began Diagnostics Test')

        self.table.putString('Status', 'Please confirm that the drivebase wheels are clear!\n')

        if self.timer.hasElapsed(2):
            robot.intake.slowIntake()

        if self.timer.hasElapsed(4):
            robot.intake.slowIntake()

        if self.timer.hasElapsed(6):
            robot.intake.stop()

        self.table.putString('Status', 'Intake done!')

        if self.timer.hasElapsed(8):
            robot.ballsystem.runLowerConveyorSlow()

        if self.timer.hasElapsed(10):
            robot.ballsystem.reverseLowerConveyorSlow()

        if self.timer.hasElapsed(12):
            robot.ballsystem.stopAll()

        if self.timer.hasElapsed(14):
            robot.ballsystem.runVerticalSlow()

        if self.timer.hasElapsed(16):
            robot.ballsystem.reverseVerticalSlow()

        if self.timer.hasElapsed(18):
            robot.ballsystem.stopAll()

        self.table.putString('Status', 'Ballsystem done!\n\nWarning! Setting shooter to speed!')

        if self.timer.hasElapsed(20):
            robot.shooter.runAtSpeed(0.6)

        if self.timer.hasElapsed(22):
            robot.shooter.stop()

        self.table.putString('Status', 'Shooter done!')

        if self.timer.hasElapsed(24):
            if robot.ballsystem.isUpperBallPrimed():
                self.table.putString('Status', 'Shooter sensor working!')

            else:
                self.table.putString('Status', 'WARNING: Shooter sensor either not blocked, or not found!')
                self.records += 'WARNING: Shooter sensor either not blocked, or not found!\n '


        if self.timer.hasElapsed(26):
            if robot.ballsystem.isLowBallPrimed():
                self.table.putString('Status', 'Chamber sensor working!')

            else:
                self.table.putString('Status', 'WARNING: Chamber sensor either not blocked, or not found!')
                self.records += 'WARNING: Chamber sensor either not blocked, or not found!\n '

        self.table.putString('Status', 'Starting Drive Base')

        if self.timer.hasElapsed(28):
            robot.drivetrain.move(0, 0.4, 0)
            self.table.putString('Status', 'Running Drive Base Forward')

        if self.timer.hasElapsed(30):
            robot.drivetrain.move(0, -0.4, 0)
            self.table.putString('Status', 'Running Drive Base Forward')

        if self.timer.hasElapsed(32):
            robot.drivetrain.stop()


    def end(self):
        self.table.putString('Status', self.records)

        self.timer.stop()
        self.timer.reset()
