from wpilib.command.command import Command
from networktables import NetworkTables
from custom.config import Config

import robot
import time

class TeamColorLightsCommand(Command):

    def killAllLights():
        return Config('killLights', False)

    def __init__(self):
        super().__init__('Team Color Lights')

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
        lightTable = NetworkTables.getTable('Lights')

        if self.colorvalue <= 1:
            robot.lights.solidOrange()
            self.colorvalue += 1

        elif self.colorvalue <= 2:
            robot.lights.solidWhite()
            self.colorvalue += 1

        elif self.colorvalue <= 3:
            robot.lights.off()
            self.colorvalue = 0

        else:
            print('uh oh')

        time.sleep(0.6)

    def end(self):
        robot.lights.off()
