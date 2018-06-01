
from wpilib.command.command import Command
import subsystems
from custom import driverhud

class AlignGearCommand(Command):
    '''Drives the robot forward and turns until it is in front of the lift.'''

    def __init__(self, handOffDistance):
        super().__init__('Align Gear at x Inches')
        self.handOffDistance = handOffDistance

        self.requires(subsystems.drivetrain)

    def initialize(self):
        self.lostCount = 0
        self.bogusCount = 0
        self._finished = False
        self.speed = 1

    def execute(self):
        center = subsystems.gear.getLiftCenter()
        if center is None:
            self.lostCount += 1
            return

        self.lostCount = 0

        distanceToLift = subsystems.gear.getLiftDistance()
        remainingDistance = distanceToLift - self.handOffDistance

        self._finished = remainingDistance < 2

        if remainingDistance > 10 and self.speed < 0.8:
            self.bogusCount += 1
            if self.bogusCount >= 10:
                self.speed = 1
        else:
            self.bogusCount = 0

        onTarget = True
        rotate = 0
        # Needs to be 12 & 0.2
        if center < -12:
            rotate = -0.2
            onTarget = False

        elif center > 12:
            rotate = 0.2
            onTarget = False

        if not onTarget:
            if remainingDistance < 10:
                self.speed = max(remainingDistance / 10.0, 0)

            self._finished = False

        subsystems.drivetrain.move(0, self.speed, rotate)


    def isFinished(self):
        if self.lostCount > 5:
            driverhud.showAlert('Lost Sight of Lift')
            return True

        return self._finished
