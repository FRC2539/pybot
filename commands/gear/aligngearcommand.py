from wpilib.command.command import Command
import subsystems
from custom import driverhud

class AlignGearCommand(Command):
    '''Drives the robot forward and turns until it is in front of the lift.'''

    def __init__(self, handOffDistance):
        super().__init__('Align Gear at %d Inches' % handOffDistance)
        self.handOffDistance = handOffDistance

        self.requires(subsystems.drivetrain)

    def initialize(self):
        self.lostCount = 0
        self._finished = False
        self.speed = 1

    def execute(self):
        center = subsystems.gear.getLiftCenter()
        if center is None:
            self.lostCount += 1
            return

        self.lostCount = 0

        distanceToLift = subsystems.gear.getLiftDistance()
        print("%s : %f" % (distanceToLift, self.handOffDistance))
        remainingDistance = distanceToLift - self.handOffDistance

        self._finished = remainingDistance < 0

        onTarget = True
        rotate = 0

        if center < -5:
            rotate = -0.1
            onTarget = False

        elif center > 5:
            rotate = 0.1
            onTarget = False

        if not onTarget:
            if remainingDistance < 10:
                self.speed = max(remainingDistance / 10.0, 0)

            self._finished = False

        subsystems.drivetrain.move(0, self.speed, rotate)


    def isFinished(self):
        if self.lostCount > 5:
            if self.getGroup() is not None:
                self.getGroup().cancel()

            driverhud.showAlert('Lost Sight of Lift')
            return True

        return self._finished
