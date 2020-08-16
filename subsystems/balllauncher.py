from wpilib.command import Subsystem

from .cougarsystem import *

from ctre import WPI_TalonSRX, ControlMode, NeutralMode

import ports

class BallLauncher(CougarSystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('BallLauncher')

        self.launcherMotors = WPI_TalonSRX(ports.balllauncher.motorID)

        self.launcherMotors.setNeutralMode(NeutralMode.Brake)
        self.launcherMotors.setInverted(True)

        self.launching = False

    def launchBalls(self):
        self.launching = True
        self.launcherMotors.set(ControlMode.PercentOutput, 1.0)

    def reverseBalls(self):
        self.launching = False
        self.launcherMotors.set(ControlMode.PercentOutput, -0.4)

    def stopLauncher(self):
        self.launching = False
        self.launcherMotors.stopMotor()

    def isMoving(self):
        return self.launching
