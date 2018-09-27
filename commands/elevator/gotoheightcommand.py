from wpilib.command.command import Command

import robot

class GoToHeightCommand(Command):

    def __init__(self, height):
        super().__init__('Go To Height', 0.75)

        self.requires(robot.elevator)
        self.height = height

    def initialize(self):
        robot.elevator.goToHeight(self.height)
        self.stopped = 0

    def isFinished(self):
        currentHeight = robot.elevator.getHeight()

        if self.isTimedOut():
            print(robot.elevator.getSpeed())
            return robot.elevator.getSpeed() <= 0.01


        #if robot.elevator.getSpeed() < 0.01:
            #self.stopped += 1

        #return self.stopped >= 6

        #if self.height <= currentHeight:
            #robot.elevator.stop()
            #print('Good as gold')
            #return True
        #return False
