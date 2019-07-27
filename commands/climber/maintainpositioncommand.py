from wpilib.command.command import Command

import robot

class MaintainPositionCommand(Command):

    def __init__(self):
        super().__init__('Maintain Position')

        self.requires(robot.climber)


    def initialize(self):
        self._finished = False

        self.startLeft = robot.climber.getLeftPos()
        self.startRight = robot.climber.getRightPos()
        self.startRear = robot.climber.getRearPos()

        print('l ' + str(self.startLeft) + '\n r ' + str(self.startRight) + '\n rear ' + str(self.startRear))


    def execute(self):
        print('Running execute')
        if robot.climber.checkLeft(self.startLeft):
            robot.climber.popLeft()
            print('raise left')
        else:
            robot.climber.stopLeftRack()

        if robot.climber.checkRight(self.startRight):
            robot.climber.popRight()
            print('raise right')
        else:
            robot.climber.stopRightRack()

        if robot.climber.checkRear(self.startRear):
            robot.climber.popRear()
            print('raise rear')
        else:
            robot.climber.stopRearRack()

        robot.climber.creepBackward()

    def end(self):
        robot.climber.stopDrive()
