from __future__ import print_function

import builtins as __builtin__

import pprint

import inspect

from wpilib.command import Subsystem

ALLOWPRINTS = True

printsDisabled = []

def print(*args, **kwargs):
    if not inspect.stack()[1].filename in printsDisabled:
        return __builtin__.print(*args, **kwargs)

def disablePrints():
    caller = inspect.stack()[1].filename

    printsDisabled.append(str(caller))
    
def enablePrints():
    caller = inspect.stack()[1].filename
    
    try:
        printsDisabled.remove(str(caller))
    except(ValueError):
        pass
    
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
