from wpilib.command import Subsystem

from .cougarsystem import *

from ctre import WPI_TalonSRX, ControlMode, NeutralMode

import ports

class BallLauncher(Subsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('BallLauncher')

        self.launcherMotors = WPI_TalonSRX(ports.balllauncher.motorID)

        self.launcherMotors.setNeutralMode(NeutralMode.Brake)
        self.launcherMotors.setInverted(True)

    def launchBalls(self):
        self.launcherMotors.set(ControlMode.PercentOutput, 0.9)

    def reverseBalls(self):
        self.launcherMotors.set(ControlMode.PercentOutput, -0.7)

    def stopLauncher(self):
        self.launcherMotors.stopMotor()
