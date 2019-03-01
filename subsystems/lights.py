from .debuggablesubsystem import DebuggableSubsystem
from custom import driverhud
from custom.config import Config

from wpilib import Spark
from networktables import NetworkTables

import time
import ports

class Lights(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Lights')
        self.lights = Spark(ports.lights.lightControllerID)

        cameraTable = NetworkTables.getTable('cameraTable')

        self.colors = {
                        'black' : 0.99,
                        'white' : 0.93,
                        'red' : 0.61,
                        'green' : 0.71,
                        'blue' : 0.83,
                        'purple' : 0.91,
                        'pink' : 0.57,
                        'yellow' : 0.69,
                        'orange' : 0.63,
                        'fire' : -0.57,
                        'chase' : -0.31
            }


        self.position = Config('cameraTable/finalCenter', 0)
        self.width = Config('cameraTable/screenWidth', 0)
        self.distance = Config('cameraTable/distanceToTape', 0)

    '''
    Light Mapping:
        Intake:     - Has Game Piece:       Solid Green

        Auto:       - No Target             Solid Red
                    - Sees Target, Moving   Solid Purple
                    - In position           Solid Blue

        Loading:    - Hatch Panel           Blink Yellow (fast)
                    - Cargo                 Blink Pink (fast)

        Seizure Mode at end of match        Seizure Mode

        Issue                               Blink Red (slow)
    '''


    def set(self, pulseWidth):
        self.lights.set(pulseWidth)

    def setSpecific(self, val):
        self.set(val)

    def off(self):
        self.set(self.colors['black'])

    def solidRed(self):
        self.set(self.colors['red'])

    def solidGreen(self):
        self.set(self.colors['green'])

    def solidYellow(self):
        self.set(self.colors['yellow'])

    def solidBlue(self):
        self.set(self.colors['blue'])

    def solidWhite(self):
        self.set(self.colors['white'])

    def solidPink(self):
        self.set(self.colors['pink'])

    def solidOrange(self):
        self.set(self.colors['orange'])

    def solidPurple(self):
        self.set(self.colors['purple'])

    def fire(self):
        self.set(self.colors['fire'])

    def chase(self):
        self.set(self.colors['chase'])

    def visionBasedLights(self):

        if self.position == 0 or self.width == 0 or self.distance == 0:
            print('pos ' + str(self.position) + 'width ' + str(self.width) + ' dis ' + str(self.distance))
            return -10, -10
        else:
            return abs((self.width / 2) - self.position), self.distance
