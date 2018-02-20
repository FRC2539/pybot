from wpilib.command import Command

import subsystems

class GoToHeightCommand(Command):

    def __init__(self, level):
        super().__init__('Go To %s' % level, 1)
        self.level=level

        self.requires(subsystems.elevator)


    def initialize(self):
        subsystems.elevator.setLevel(self.level)
        self.stopped = 0


    def isFinished(self):
        if not self.isTimedOut():
            return False

        if subsystems.elevator.getSpeed() < 0.01:
            self.stopped += 1
        else:
            self.stopped = 0

        return self.stopped >= 5
