from wpilib.command.command import Command

import robot
import time

from networktables import NetworkTables

class SeizureLightsCommand(Command):

    def __init__(self):
        super().__init__('Seizure Lights')

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

        time.sleep(0.03634273462768745736756824367364)
    def end(self):
        robot.lights.off()
