from wpilib.command.command import Command
import math
import robot

class HolonomicMoveCommand(Command):

    def __init__(self, x, y):
        super().__init__('Holonomic Move')

        self.requires(robot.drivetrain)

        self.x = x
        self.y = y
        #self.rotate = rotate

        self.finished = False


    def initialize(self):
        if robot.drivetrain.isFieldOriented:
            robot.drivetrain.toggleFieldOrientation()

        robot.drivetrain.resetGyro()
        robot.drivetrain.resetNavXDisplacement()


    def execute(self):
        print('X:  ' + str(robot.drivetrain.getXDisplacement()) + '             Y:  ' + str(robot.drivetrain.getYDisplacement()))

        #if abs(robot.drivetrain.getAngle()) >= abs(self.rotate):
        #    self.rotate = 0
        if abs(robot.drivetrain.getXDisplacement()) >= abs(self.x):
            self.x = 0
        if abs(robot.drivetrain.getYDisplacement()) >= abs(self.y):
            self.y = 0

        if (self.x == 0 and self.y == 0 and self.rotate == 0):
            self.finished = True

        robot.drivetrain.move(self.x / 12, self.y / 24, 0)


    def isFinished(self):
        return self.finished


    def end(self):
        robot.drivetrain.stop()
