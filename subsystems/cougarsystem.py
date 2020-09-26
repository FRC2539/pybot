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

        try:

            with open('/home/lvuser/py/data.txt', 'r') as f:
                for line in f:
                    if eval(str(line[:-1]) + '[0]') == self.name: # Checks the data file for data for the subsystem.
                        self.data[eval(str(line[:-1]) + '[1]')] = eval(str(line[:-1]) + '[2]')

            #print('\n\n updated ' + str(self.data) + ' \n\n\n')

        except(FileNotFoundError):
            pass

    def get(self, var, default=None):
        if var in self.data:
            return self.data[var] # Returns the data recorded in disabledInit
        else:
            #print('\n\n USING DEFAULT \n\n')
            return default

    def capture(self, var, method):
        self.writeOnDisable.append([self.name, str(var), '.' + str(method) + '()'])
