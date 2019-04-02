from wpilib.command.command import Command

import robot
import time

from networktables import NetworkTables

class SeizureLightsCommand(Command):

    def __init__(self):
        super().__init__('Seizure Lights')

        self.setRunWhenDisabled(True)

        self.requires(robot.lights)
        self.colorvalue = 0
        NetworkTables.initialize(server='roborio-2539-frc.local')

    def execute(self):
        if self.colorvalue <= 1:
            robot.lights.solidRed()
            self.colorvalue += 1

        elif self.colorvalue <= 2:
            robot.lights.solidGreen()
            self.colorvalue += 1

        elif self.colorvalue <= 3:
            robot.lights.solidBlue()
            self.colorvalue = 1

        time.sleep(0.04)

    def end(self):
        robot.lights.off()
