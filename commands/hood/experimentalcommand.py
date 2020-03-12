from wpilib.command import Command

import robot
import math

class ExperimentalCommand(Command):

    def __init__(self):
        super().__init__('Experimental')

        self.requires(robot.hood)


    def initialize(self):
        robot.limelight.setPipeline(1)


    def execute(self):
        distance = robot.limelight.calcDistanceGood()
        print('distance ' + str(distance))
        robot.limelight.updateNetworkTables()

        if robot.limelight.getTape():
            if(distance < 240):
                robot.hood.setAngle(math.degrees(math.atan(77.25/distance)) - 2)

            else:
                #Constant angle after 200 inches
                robot.hood.setAngle(math.degrees(math.atan(77.25/240)) - 2)

            robot.ledsystem.onTarget = (robot.limelight.getX() <= 3.0)

        else:
            robot.hood.stopHood()

    def end(self):
        robot.limelight.setPipeline(0)
        robot.hood.stopHood()
