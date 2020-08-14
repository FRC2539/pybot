from __future__ import print_function

import builtins as __builtin__

import pprint

from wpilib.command import Subsystem

ALLOWPRINTS = True

def print(output):
    if ALLOWPRINTS:
        __builtin__.print(str(output))

def disablePrints():
    ALLOWPRINTS = False

def enablePrints():
    ALLOWPRINTS = True

class CougarSystem(Subsystem):

    def __init__(self, name):
        super().__init__(name)

        self.data = {} # Individual to each subsystem. {Name : Method}
        self.writeOnDisable = [] # [Parent, Name, Value]

        self.name = name

        #with open('.data.txt', 'r') as f:
            #for line in f:
                #if eval(str(line[:-1]) + '[0]') == self.name: # Checks the data file for data for the subsystem.
                    #self.data[eval(str(line[:-1]) + '[1]')] = eval(str(line[:-1]) + '[2]')

    def get(self, var):
        return #self.data[var] # Returns the data recorded in disabledInit

    def capture(self, var, method):
        self.writeOnDisable.append([self.name, str(var), '.' + str(method) + '()'])
