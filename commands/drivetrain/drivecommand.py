from wpilib.command import Command

import robot
from controller import logicalaxes
from custom.config import Config
import math

logicalaxes.registerAxis('driveX')
logicalaxes.registerAxis('driveY')
logicalaxes.registerAxis('driveRotate')

class DriveCommand(Command):
    def __init__(self, speedLimit):
        super().__init__('DriveCommand %s' % speedLimit)

        self.requires(robot.drivetrain)
        self.speedLimit = speedLimit

        self.preciseSpeed = Config('DriveTrain/preciseSpeed')
        if self.speedLimit < self.preciseSpeed:
            self.preciseSpeed = self.speedLimit

        self.unsafeHeight = Config('Elevator/switch') + 1000


    def initialize(self):
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)
        try:
            robot.drivetrain.setSpeedLimit(self.speedLimit)
        except (ZeroDivisionError, TypeError):
            print('Could not set speed to %f' % self.speedLimit)
            robot.drivetrain.setUseEncoders(False)

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

        tilt = robot.drivetrain.getTilt()
        correction = tilt / 20
        if abs(correction) < 0.2:
            correction = 0

        # Slow down when elevator is up
        if not self.slowed:
            if robot.elevator.getHeight() >= self.unsafeHeight:
                robot.drivetrain.setSpeedLimit(self.preciseSpeed)

        else:
            if robot.elevator.getHeight() < self.unsafeHeight:
                robot.drivetrain.setSpeedLimit(self.speedLimit)

        robot.drivetrain.move(
            logicalaxes.driveX.get(),
            y - correction,
            logicalaxes.driveRotate.get()
        )
