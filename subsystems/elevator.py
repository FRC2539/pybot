from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX, ControlMode, FeedbackDevice
import ports
from custom.config import Config
import threading

class Elevator(Subsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Elevator')

        self.motor = WPI_TalonSRX(ports.elevator.motorID)
        self.motor.setSafetyEnabled(False)
        self.motor.configSelectedFeedbackSensor(
            FeedbackDevice.PulseWidthEncodedPosition,
            0,
            0
        )

        self.lowerLimit = 0
        self.upperLimit = 24000
        self.motor.configReverseSoftLimitEnable(True, 0)
        self.motor.configForwardSoftLimitEnable(True, 0)
        self.motor.configReverseSoftLimitThreshold(self.lowerLimit, 0)
        self.motor.configForwardSoftLimitThreshold(self.upperLimit, 0)
        self.motor.configMotionCruiseVelocity(3740, 0)
        self.motor.configMotionAcceleration(7480, 0)

        self.floors = [
            Config('Elevator/ground'),
            Config('Elevator/exchange'),
            Config('Elevator/portal'),
            Config('Elevator/switch'),
            Config('Elevator/scale'),
            Config('Elevator/hang')
        ]
        self.floorNames = []
        for floor in self.floors:
            name = floor.getKey().split('/')[-1].capitalize()
            self.floorNames.append(name)

        self.level = 0
        self.mutex = threading.RLock()


    def initDefaultCommand(self):
        from commands.elevator.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())


    def set(self, speed):
        self.motor.set(ControlMode.PercentOutput, speed)


    def up(self):
        self.set(1)


    def down(self):
        self.set(-0.5)


    def getHeight(self):
        return self.motor.getSelectedSensorPosition(0)


    def getSpeed(self):
        return abs(self.motor.getQuadratureVelocity())


    def getLevelName(self):
        height = self.getHeight()
        level = self.floors[self.level]
        if level - 500 < height < level + 500:
            return self.floorNames[self.level]

        below = None
        above = None
        for level, floor in enumerate(self.floors):
            above = level
            if height <= floor:
                break

            below = level

        if below == above:
            if height < self.floors[above] + 500:
                return self.floorNames[above]

            return 'Above %s' % self.floorNames[above]

        if below is None:
            if height > self.floors[0] - 500:
                return self.floorNames[0]

            return 'Below %s' % self.floorNames[0]

        if height - self.floors[below] < self.floors[above] - height:
            if height < self.floors[below] + 500:
                return self.floorNames[below]
            return 'Above %s' % self.floorNames[below]

        else:
            if height > self.floors[above] - 500:
                return self.floorNames[above]
            return 'Below %s' % self.floorNames[above]


    def guessLevel(self):
        height = self.getHeight()
        for level, floor in enumerate(self.floors):
            if floor - 500 < height < floor + 500:
                self.level = level
                return


    def stop(self):
        height = self.getHeight()
        if height < self.lowerLimit:
            height = self.lowerLimit
        elif height > self.upperLimit:
            height = self.upperLimit

        self.guessLevel()

        self.motor.set(ControlMode.MotionMagic, height)


    def reset(self):
        self.motor.setSelectedSensorPosition(0, 0, 0)
        self.setLevel('ground')


    def goTo(self, height):
        self.motor.set(ControlMode.MotionMagic, int(height))


    def changeLevel(self, amount=1):
        with self.mutex:
            self.level += amount
            if self.level < 0:
                self.level = 0

            if self.level >= len(self.floors):
                self.level = len(self.floors) - 1

        self.goTo(self.floors[self.level])


    def setLevel(self, floor):
        key = 'Elevator/%s' % floor

        with self.mutex:
            for level, floor in enumerate(self.floors):
                if (str(floor) == key):
                    self.level = level
                    break

        self.goTo(self.floors[self.level])
