from wpilib.command import Command

import robot
from controller import logicalaxes
from custom.config import Config, MissingConfigError
from custom import driverhud
import math

logicalaxes.registerAxis('driveX')
logicalaxes.registerAxis('driveY')
logicalaxes.registerAxis('driveRotate')

class DriveCommand(Command):
    def __init__(self, speedLimit):
        super().__init__('DriveCommand %s' % speedLimit)

        self.requires(robot.drivetrain)
        self.speedLimit = speedLimit

        robot.drivetrain.resetPID()

    def initialize(self):
        robot.drivetrain.stop()
        try:
            robot.drivetrain.setSpeedLimit(self.speedLimit)
        except (ValueError, MissingConfigError):
            print('Could not set speed to %s' % self.speedLimit)
            driverhud.showAlert('Drive Train is not configured')
            #robot.drivetrain.enableSimpleDriving()

        self.lastY = None
        self.slowed = False

    def execute(self):
        # Avoid quick changes in direction
        y = logicalaxes.driveY.get()
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

        #print(str('X ' + str(logicalaxes.driveX.get()) + '\nY ' + str(y) + '\nRotate ' + str(logicalaxes.driveRotate.get())))

        if not abs(robot.drivetrain.getTilt() / 20) < 0.2: # simple, anti-roll thingy.
            y -= robot.drivetrain.getTilt() / 20

        robot.drivetrain.move(
            logicalaxes.driveX.get(),
            y,
            logicalaxes.driveRotate.get() * 0.6
        )

