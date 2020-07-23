from __future__ import print_function

import builtins as __builtin__

import pprint

ALLOWPRINTS = True

def print(output):
    if ALLOWPRINTS:
        __builtin__.print(str(output))

def disablePrints():
    ALLOWPRINTS = False

def enablePrints():
    ALLOWPRINTS = True
