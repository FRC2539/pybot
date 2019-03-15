from wpilib.command.command import Command

import robot

class StrafeCommand(Command):

    def __init__(self, distance, name=None):
        '''
        Takes a distance in inches and stores it for later. We allow overriding
        name so that other autonomous driving commands can extend this class.
        '''

        if name is None:
            name = 'Strafe %f inches' % distance

        super().__init__(name, 0.2)

        self.distance = distance
        self.requires(robot.drivetrain)


    def _initialize(self):
        super()._initialize()
        self.precision = robot.drivetrain.strafeInchesToTicks(1)


    def initialize(self):
        self.onTarget = 0
        self.targetPositions = []
        offset = robot.drivetrain.strafeInchesToTicks(self.distance)
        sign = 1
        count = 1
        for position in robot.drivetrain.getPositions():
            if count >= 3:
                sign = -1
            self.targetPositions.append(position + offset * sign)
            count += 1

        print('Targets: ' + str(self.targetPositions))
        print('Starting: ' + str(robot.drivetrain.getPositions()))

        robot.drivetrain.setPositions(self.targetPositions)


    def execute(self):
        print('Current: ' + str(robot.drivetrain.getPositions()))


    def isFinished(self):
        if robot.drivetrain.atPosition(self.precision): #self.isTimedOut() and
            self.onTarget += 1

        else:
            self.onTarget = 0

        print("targets: "+str(self.onTarget))

        return self.onTarget > 5
