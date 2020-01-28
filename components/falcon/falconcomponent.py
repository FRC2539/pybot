import wpilib

from ctre import TalonFX, TalonFXControlMode

class FalconTest:
    falconTest: object

    def __init__(self):
        pass

    def run(self):
        self.falconTest.set(TalonFXControlMode.PercentOutput, 1.0)
        print('RPM?: '+ str((self.falconTest.getSelectedSensorVelocity(0) * 600) / 2048))

    def execute(self):
        self.run()
