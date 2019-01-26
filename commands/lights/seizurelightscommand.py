from wpilib.command.command import Command

import robot
import time

from custom.config import Config
from networktables import NetworkTables

def killAllLights():
    return Config('killLights', False)

class SeizureLightsCommand(Command):

    def __init__(self):
        super().__init__('Seizure Lights')

        self.requires(robot.lights)
        self.colorvalue = 0
        NetworkTables.initialize(server='roborio-2539-frc.local')

    def initialize(self):
        lightTable = NetworkTables.getTable('Lights')

        self.lightsOn = Config('lightsRunning', False)
        self.killLights = Config('killLights', False)

        if self.lightsOn:
            lightTable.putBoolean('killLights', True)

        lightTable.putBoolean('lightsRunning', True)

    def execute(self):
        if killAllLights():
            pass
        else:
            if self.colorvalue <= 1:
                robot.lights.solidRed()
                self.colorvalue += 1

            elif self.colorvalue <= 2:
                robot.lights.solidGreen()
                self.colorvalue += 1

            elif self.colorvalue <= 3:
                robot.lights.solidBlue()
                self.colorvalue += 1

            elif self.colorvalue <= 4:
                robot.lights.solidOrange()
                self.colorvalue += 1

            elif self.colorvalue <= 5:
                robot.lights.solidPink()
                self.colorvalue += 1

            elif self.colorvalue <= 6:
                robot.lights.solidYellow()
                self.colorvalue += 1

            elif self.colorvalue <= 7:
                robot.lights.solidWhite()
                self.colorvalue += 1

            elif self.colorvalue <= 8:
                robot.lights.solidViolet()
                self.colorvalue = 0

            else:
                self.colorvalue = 0
                print('Uh-oh')

            time.sleep(0.2)

    def end(self):
        robot.lights.off()

