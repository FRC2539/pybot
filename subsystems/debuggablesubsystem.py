from __future__ import print_function

import builtins as __builtin__

from wpilib.command import Subsystem
from wpilib import LiveWindow

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

