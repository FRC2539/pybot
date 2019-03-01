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

        cameraInfo = NetworkTables.getTable('cameraInfo')
        self.position = Config('cameraInfo/tapeX', 0)
        self.distance = Config('cameraInfo/distanceToTape', 0)

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
        pos = self.position.getValue()
        distance = self.distance.getValue()

        if pos == -1:
            pos = 20
        self.width = 320 #Config('cameraInfo/screenWidth', 320)

        if distance == -1:
            distance = 20
        print('pos ' + str(pos) + 'width ' + str(self.width) + ' dis ' + str(distance))

        if int(pos) == 20 and int(distance) == 20:
            print('pos ' + str(pos) + 'width ' + str(self.width) + ' dis ' + str(distance))
            return 20
        else:
            return abs(pos)

        # CONFIG ASSIGNMENT MUST BE IN __INIT__, (OR MAYBE AS AN ARGUEMENT, THIS WORKED)), USE SELF.POSITION AS EXAMPLE. -2019 HATBORO-HORSHAM BEN
