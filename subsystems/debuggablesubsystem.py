from __future__ import print_function

import builtins as __builtin__

import csv

from wpilib.command import Subsystem
from wpilib import LiveWindow

import pprint

import robot

import sys

ALLOWPRINTS = True # Specific to each class, allows us to debug one class in particular when we have multiple prints around the code.

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

def print(output, doubleSpace):
    if ALLOWPRINTS:
        __builtin__.print(str(output))

def disablePrint():
    ALLOWPRINTS = False

def enablePrint():
    ALLOWPRINTS = True

def getFromCSV(name):
    try:
        with open('saveddata.csv', 'r', newline='') as f:
            reader = csv.reader(f, delimiter=' ', quotechar='|') # The spaced delimiter allows us to sort.
            for row in reader: # Read it, and look through all of the lines, attempting to find requested variable.
                if row[0] == name:
                    return row[2]

    except(Exception):
        print('Could not fetch variable. Does it exist? Is it spelled correctly? Did the Russians delete it?!?!?!') # lol

def saveVar(value):
    variable = value # Reassigns to reassure that it's in the scope.

    presentVars = dict(globals())

    string = list(presentVars.keys())[list(presentVars.values()).index(variable)]

    with open('saveddata.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow([string, self, None, value]) # Name, system, current val, original val


