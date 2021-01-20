from wpilib.command import Command

import robot
from controller import logicalaxes
from custom.config import Config, MissingConfigError
from custom import driverhud
import math

logicalaxes.registerAxis('forward')
logicalaxes.registerAxis('strafe')
logicalaxes.registerAxis('rotate')

class DriveCommand(Command):
    def __init__(self, speedLimit):
        super().__init__('DriveCommand %s' % speedLimit)

        self.requires(robot.drivetrain)
        self.speedLimit = speedLimit


    def initialize(self):
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)
        self.lastY = None
        self.slowed = False

    def execute(self):
        # Avoid quick changes in direction
        y = logicalaxes.forward.get()
        if self.lastY is None:
            self.lastY = y
        else:
            cooldown = 0.05
            self.lastY -= math.copysign(cooldown, self.lastY)

            # If the sign has changed, don't move
            if self.lastY * y < 0:
                y = 0

            if abs(y) > abs(self.lastY):
                self.lastY = y

        robot.drivetrain.move(
            logicalaxes.strafe.get(),
            y,
            logicalaxes.rotate.get()
        )

        print(robot.drivetrain.speeds)
        print('a ' + str(robot.drivetrain.angles))
