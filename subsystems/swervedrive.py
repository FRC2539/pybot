from .cougarsystem import *
from .basedrive import BaseDrive
from .swervemodule import SwerveModule

import ports
import constants

import math


class SwerveDrive(BaseDrive):
    def __init__(self, name):
        super().__init__(name)

        """
        "Rollers? Where we're going, we don't need 'rollers'." - Ben Bistline, 2021
        
        The constructor for the class. When returning lists, it should follow like:
        [front left, front right, back left, back right]
        """

        self.isFieldOriented = True

        self.wheelBase = (
            constants.drivetrain.wheelBase
        )  # These are distances across the robot; horizontal, vertical, diagonal.
        self.trackWidth = constants.drivetrain.trackWidth
        self.r = math.sqrt(self.wheelBase ** 2 + self.trackWidth ** 2)

        self.speedLimit = (
            constants.drivetrain.speedLimit
        )  # Override the basedrive without editing the file.

        self.modules = [
            SwerveModule(  # Front left module.
                ports.drivetrain.frontLeftDriveID,
                ports.drivetrain.frontLeftTurnID,
                ports.drivetrain.frontLeftCANCoder,
                self.speedLimit,
                -251.37,
            ),
            SwerveModule(  # Front right module.
                ports.drivetrain.frontRightDriveID,
                ports.drivetrain.frontRightTurnID,
                ports.drivetrain.frontRightCANCoder,
                self.speedLimit,
                -271.9,
                invertedDrive=True,  # Invert for some reason?
            ),
            SwerveModule(  # Back left module.
                ports.drivetrain.backLeftDriveID,
                ports.drivetrain.backLeftTurnID,
                ports.drivetrain.backLeftCANCoder,
                self.speedLimit,
                -38.8,
            ),
            SwerveModule(  # Back right module.
                ports.drivetrain.backRightDriveID,
                ports.drivetrain.backRightTurnID,
                ports.drivetrain.backRightCANCoder,
                self.speedLimit,
                -130.6,
                invertedDrive=True,  # Invert for some reason. Ezra's going nuts lol.
            ),
        ]

    def _configureMotors(self):
        """
        Configures the motors. Shouldn't need this.
        """

        self.activeMotors = self.motors[
            0:2
        ]  # Don't actually need these, this just keeps basedrive happy.

    def _calculateSpeeds(self, x, y, rotate):
        """
        Gonna take this nice and slow. Declaring variables to be simple,
        should try to walk through while coding.
        """

        """
        'self.getAngle()' is the robot's heading, 
        multiply it by pi over 180 to convert to radians.
        """
        #rotate = -rotate
        
        theta = self.getAngleTo(0) * (
            math.pi / 180
        )  # Gets the offset to zero, -180 to 180.

        if (
            self.isFieldOriented
        ):  # Are we field-centric, as opposed to robot-centric. A tank drive is robot-centric, for example.

            temp = y * math.cos(theta) + x * math.sin(theta)  # just the new y value being temporarily stored.
            x = -y * math.sin(theta) + x * math.cos(theta)
            y = temp

        """
        The bottom part is the most confusing part, but it basically uses ratios and vectors with the
        pythagorean theorem to calculate the velocities.
        """
        print(str(rotate))
        A = x - rotate * (self.wheelBase / self.r)  # Use variables to simplify it.
        B = x + rotate * (self.wheelBase / self.r)
        C = y - rotate * (self.trackWidth / self.r)
        D = y + rotate * (self.trackWidth / self.r)

        ws1 = math.sqrt(B ** 2 + D ** 2)  # Front left speed
        ws2 = math.sqrt(B ** 2 + C ** 2)  # Front right speed
        ws3 = math.sqrt(A ** 2 + D ** 2)  # Back left speed
        ws4 = math.sqrt(A ** 2 + C ** 2)  # Back right speed

        wa1 = math.atan2(B, D) * 180 / math.pi   # Front left angle (degrees)
        wa2 = math.atan2(B, C) * 180 / math.pi # Front right angle
        wa3 = math.atan2(A, D) * 180 / math.pi  # Back left angle
        wa4 = math.atan2(A, C) * 180 / math.pi  # Back right angle

        speeds = [ws2, ws1, ws4, ws3]  # It is in order (FL, FR, BL, BR).
        angles = [wa2, wa1, wa4, wa3]  # It is in order (FL, FR, BL, BR).

        newSpeeds = speeds  # Do NOT delete! This IS used!
        newAngles = angles

        print("a " + str(newAngles))

        maxSpeed = max(speeds)  # Find the largest speed.
        minSpeed = min(speeds)  # Find the smallest speed.

        if (
            maxSpeed > 1
        ):  # Normalize speeds if greater than 1, but keep then consistent with each other.
            speeds[:] = [
                speed / maxSpeed for speed in speeds
            ]  # We can do this by dividing ALL by the largest value.

        if (
            minSpeed < -1
        ):  # Normalize speeds if less than -1, but keep then consitent with each other.
            speeds[:] = [
                speed / minSpeed * -1 for speed in speeds
            ]  # We can do this by dividing ALL by the smallest value. The negative maintains the signs.

        magnitude = math.sqrt(
            (x ** 2) + (y ** 2)
        )  # Pythagorean theorem, vector of joystick.
        if magnitude > 1:
            magnitude = 1

        speeds[:] = [
            speed * magnitude for speed in speeds
        ]  # Ensures that the speeds of the motors are relevant to the joystick input.

        return newSpeeds, angles  # Return the calculated speed and angles.

    def move(self, x, y, rotate):
        """
        Turns coordinate arguments into motor outputs.
        Short-circuits the rather expensive movement calculations if the
        coordinates have not changed.
        """
        if [x, y, rotate] == self.lastInputs or [x, y, rotate] == [0, 0, 0]:
            return

        self.lastInputs = [x, y, rotate]
        #print(str(rotate))

        """Prevent drift caused by small input values"""
        x = math.copysign(max(abs(x) - self.deadband, 0), x)
        y = math.copysign(max(abs(y) - self.deadband, 0), y)
        rotate = math.copysign(max(abs(rotate) - (self.deadband + 0.05), 0), rotate)
        #print('modified'+str(rotate))
        speeds, angles = self._calculateSpeeds(x, y, rotate)

        if (
        x == 0 and y == 0 and rotate != 0
        ):  # The robot won't apply power if it's just rotate (fsr?!)
            for module, angle in zip(
            self.modules, angles
        ):  # You're going to need encoders, so only focus here.
                module.setWheelAngle(angle)
                module.setWheelSpeed(abs(rotate))

        else:
            for module, speed, angle in zip(
        self.modules, speeds, angles
        ):  # You're going to need encoders, so only focus here.
                module.setWheelAngle(angle)
                module.setWheelSpeed(abs(math.sqrt(speed**2+rotate**2)))

    def stop(self):
        for module in self.modules:
            module.stopModule()

    def setProfile(self, profile):
        for module in self.modules:
            module.setModuleProfile(profile)

    def setFieldOriented(self, fieldCentric=True):
        self.isFieldOriented = fieldCentric

    def getSpeeds(self, inIPS=True):  # Defaults to giving in inches per second.
        return [module.getWheelSpeed(inIPS) for module in self.modules]

    def setSpeeds(self, speeds: list):  # Set a speed in inches per second.
        for module, speed in zip(self.modules, speeds):
            module.setWheelSpeed(speed)

    def updateCANCoders(self, positions: list):
        for module, position in zip(self.modules, positions):
            module.updateCANCoder(position)

    def getModuleAngles(self):
        # Add module in front, not to be confused with gyro! Returns degrees.
        return [module.getWheelAngle() for module in self.modules]

    def setModuleAngles(self, angles: list):  # Set a list of different angles.
        for module, angle in zip(self.modules, angles):
            module.setWheelAngle(angle)

    def setModuleAngles(
        self, angle: int
    ):  # This sets a uniform angle. Overrides the method above.
        for module in self.modules:
            module.setWheelAngle(angle)

    def getPositions(self, inInches=True):  # Defaults to giving in inches.
        return [module.getModulePosition(inInches) for module in self.modules]

    def setPositions(
        self, positions: list
    ):  # Remember, provide these in inches. It will go forward/back x many inches.
        for module, position in zip(self.modules, positions):
            module.setModulePosition(position)

    def setModuleProfiles(self, id_=0):
        for module in self.modules:
            module.setModuleProfile(id_)
