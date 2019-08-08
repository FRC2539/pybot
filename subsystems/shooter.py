from .debuggablesubsystem import DebuggableSubsystem
from wpilib.command.subsystem import Subsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX
from wpilib.digitalinput import DigitalInput
from wpilib import PWMSpeedController
from custom.driverhud import showAlert
from custom import driverhud

import ports


class Shooter(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')
        self.shooter = WPI_TalonSRX(ports.shooter.shooterMotorID)
        self.shooter.setSafetyEnabled(False)
        self.shooter.setInverted(True)
        self.vspeed = 0.6


        # setInverted might need to be False

    def set(self, speed):
        self.shooter.set(ControlMode.PercentOutput, speed)

# The following two methods were created to simplify dashboard speed alerts.

    def displayDecreaseSpeed(self):
        self.pvspeed = str(self.vspeed)
        if len(str(self.pvspeed)) > 5:
            if self.pvspeed[2:4] == '79':
                self.pvspeed = '0.8'
                driverhud.showAlert('Shooter Speed Decreased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '89':
                self.pvspeed = '0.9'
                driverhud.showAlert('Shooter Speed Decreased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '99':
                self.pvspeed = '1.0'
                driverhud.showAlert('Shooter Speed Decreased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '30':
                self.pvspeed = '0.3'
                driverhud.showAlert('Shooter Speed Decreased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '20':
                self.pvspeed = '0.2'
                driverhud.showAlert('Shooter Speed Decreased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '10':
                self.pvspeed = '0.1'
                driverhud.showAlert('Shooter Speed Decreased! Speed:\n' + str(self.pvspeed))
        else:
            driverhud.showAlert('Shooter Speed Decreased! Speed:\n' + str(self.vspeed))

    def displayIncreaseSpeed(self):
        self.pvspeed = str(self.vspeed)
        if len(str(self.pvspeed)) > 5:
            if self.pvspeed[2:4] == '79':
                self.pvspeed = '0.8'
                driverhud.showAlert('Shooter Speed Increased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '89':
                self.pvspeed = '0.9'
                driverhud.showAlert('Shooter Speed Increased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '99':
                self.pvspeed = '1.0'
                driverhud.showAlert('Shooter Speed Increased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '30':
                self.pvspeed = '0.3'
                driverhud.showAlert('Shooter Speed Increased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '20':
                self.pvspeed = '0.2'
                driverhud.showAlert('Shooter Speed Increased! Speed:\n' + str(self.pvspeed))
            elif self.pvspeed[2:4] == '10':
                self.pvspeed = '0.1'
                driverhud.showAlert('Shooter Speed Increased! Speed:\n' + str(self.pvspeed))
        else:
            driverhud.showAlert('Shooter Speed Increased! Speed:\n' + str(self.vspeed))

    def shoot(self):
        self.set(1)

    def slowShoot(self):
        self.set(0.75)

    def increaseSpeed(self):
        if self.vspeed + 0.1 <= 1:
            self.vspeed += 0.1
            self.displayIncreaseSpeed()
            print(str(self.vspeed))
        else:
            driverhud.showAlert('Unable to increase speed')

    def decreaseSpeed(self):
        if self.vspeed - 0.1 >= .1:
            self.vspeed -= 0.1
            self.displayDecreaseSpeed()
            print(str(self.vspeed))
        else:
            driverhud.showAlert('Unable to decrease speed')

    def variedShoot(self):
        self.set(self.vspeed)

    def stop(self):
        self.set(0)
