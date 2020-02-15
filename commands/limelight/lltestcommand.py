from wpilib.command import Command

import robot


class llTestCommand(Command):

    def __init__(self):
        super().__init__('ll Test')

        self.requires(robot.limelight)
        #self.requires(robot.drivetrain)




    def initialize(self):
        robot.limelight.setPipeline(1)



    def execute(self):
        #self.rotate = robot.limelight.getX()*.03
        #robot.drivetrain.move(0,0,self.rotate)
        print(str(robot.limelight.calcDistance()))


    def end(self):
        robot.limelight.setPipeline(0)
