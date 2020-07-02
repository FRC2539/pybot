from wpilib.command import Command

from wpilib import Timer

import robot

import time

class TestRunAllCommand(Command):

    def __init__(self):
        super().__init__('Test Run All')

        self.requires(robot.ballsystem)
        self.requires(robot.ledsystem)

        self.runming = False # do not change, says whether or not the ball system is running
        self.iterations = 0 # also do not change, says how many times the execute() has been done since the last time the ball system stopped
        self.atRPMTolerance = 18 # tolerance value for shooter.atRPM()
        self.iterTimeout = 10 # timeout for waiting on the rpm to go back up

    def initialize(self): # turn everything off and set some variables
        robot.ballsystem.stopAll()
        robot.intake.stop()

        self.runming = "Beans"
        self.iterations = 0

    def execute(self): # execute
        print("TESTRUNALLCOMMAND: " + str(self.runming) + " " + str(robot.shooter.atRPM(self.atRPMTolerance)) + " " + str(self.iterations))
        if ((not self.runming or self.runming == "Beans") and robot.shooter.atRPM(self.atRPMTolerance)) or (self.iterations >= self.iterTimeout and self.iterations < self.iterTimeout*2):
            self.runming = True
            robot.ballsystem.runAll()
            robot.intake.intake()
            print("TESTRUNALLCOMMAND: RUNNING")
            robot.ledsystem.setRed()
        elif (self.runming or self.runming == "Beans") and (not robot.shooter.atRPM(self.atRPMTolerance)) or self.iterations >= self.iterTimeout*2:
            self.runming = False
            robot.ballsystem.stopAll()
            robot.intake.stop()
            print("TESTRUNALLCOMMAND: STOPPING")
            self.iterations = 0
            robot.ledsystem.setBlue()
        self.iterations += 1

    def end(self): # turn everything off again but don't set some variables
        print("According to all known laws of aviation, there is no way a bee should be able to fly.")
        robot.ballsystem.stopAll()
        robot.intake.stop()
        robot.ledsystem.turnOff()
        self.runming = False
