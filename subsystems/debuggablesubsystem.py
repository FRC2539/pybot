from wpilib.command import Subsystem
from wpilib import LiveWindow

import robot

class DebuggableSubsystem(Subsystem):
    '''
    Simplifies sending sensor and actuator data to the SmartDashboard. This
    should be used as the base class for any subsystem that has motors or
    sensors.
    '''

    def debugSensor(self, label, sensor):
        return
        sensor.SetName(self.getName(), label)

    def debugMotor(self, label, motor):
        return
        motor.SetName(self.getName(), label)

    def print(self, output):
        print('custom')
        if robot.enablePrints:
            print(str(output))

    def disablePrint(self):
        robot.enablePrints = False

    def enablePrint(self):
        robot.enablePrints = True

