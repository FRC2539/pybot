import wpilib

from ctre import TalonFX, TalonFXControlMode

class FalconTest:
    falconTest: object

    def __init__(self):
        pass

    def setup(self):
        self.falconTest.config_kP(0, 0.01, 0)
        self.falconTest.config_kI(0, 0, 0)
        self.falconTest.config_kD(0, 0.1, 0)
        self.falconTest.config_IntegralZone(0, 1, 0)
        self.falconTest.config_kF(0, 0.1, 0)

    def run(self):
        rpm = (4600 * 2048) / 600

        self.falconTest.set(TalonFXControlMode.Velocity, rpm)
        print('RPM?: '+ str((self.falconTest.getSelectedSensorVelocity(0) * 600) / 2048))

    def execute(self):
        self.run()
