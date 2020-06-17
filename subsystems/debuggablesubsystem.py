from wpilib.command import Subsystem
from wpilib import LiveWindow

class DebuggableSubsystem(Subsystem):
    '''
    Simplifies sending sensor and actuator data to the SmartDashboard. This
    should be used as the base class for any subsystem that has motors or
    sensors.
    '''

    def __init__(self):
        self.enablePrints = True

    def debugSensor(self, label, sensor):
        return
        sensor.SetName(self.getName(), label)

    def debugMotor(self, label, motor):
        return
        motor.SetName(self.getName(), label)

    def cp(self, output):
        if self.enablePrints:
            print(str(output))

    def disablePrint(self):
        self.enablePrints = False

    def enablePrint(self):
        self.enablePrints = True
