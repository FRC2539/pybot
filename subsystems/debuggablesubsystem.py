from __future__ import print_function

import builtins as __builtin__

import csv

from wpilib.command import Subsystem
from wpilib import LiveWindow

import pprint

import robot

import sys

class DebuggableSubsystem(Subsystem):
    '''
    Simplifies sending sensor and actuator data to the SmartDashboard. This
    should be used as the base class for any subsystem that has motors or
    sensors.
    '''

    def debugSensor(self, label, sensor):
        return
        sensor.SetName(self.getName(), label)

    def debugMotor(self, label, motor):
        return
        motor.SetName(self.getName(), label)

def print(output):
    if robot.globalObject.enabledPrints:
        __builtin__.print(str(output))

def disablePrint():
    robot.globalObject.enabledPrints = False

def enablePrint():
    robot.globalObject.enabledPrints = True

def getFromCSV(name):
    pass # Read it, and look through all of the lines, attempting to find requested variable.

def saveVar(value):
    variable = value # Reassigns to reassure that it's in the scope.

    presentVars = dict(globals())

    string = list(presentVars.keys())[list(presentVars.values()).index(variable)]

    with open('saveddata.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([string, self, None, value]) # Name, system, current val, original val


