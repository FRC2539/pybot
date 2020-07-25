from wpilib.command import Subsystem

from .cougarsystem import *

from ctre import WPI_TalonSRX, ControlMode, NeutralMode

import ports

class BallLauncher(Subsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('BallLauncher')

        self.launcherMotors = WPI_TalonSRX(ports.balllauncher.motorID)

        self.launcherMotors.setNeutralMode(NeutralMode.kBrake)
        self.launcherMotors.setInverted(False)

    def launchBalls(self):
        self.launcherMotors.set(ControlMode.PercentOutput, 0.7)

    def reverseBalls(self):
        self.launcherMotors.set(ControlMode.PercentOutput, -0.5)

    def stopLauncher(self):
        self.launcherMotors.stopMotor()
