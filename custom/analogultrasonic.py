from wpilib.analoginput import AnalogInput

class AnalogUltrasonic(AnalogInput):
    '''Simple wrapper to treat an analog signal like a distance sensor.'''

    def __init__(self, channel):
        super().__init(channel)

        self.scalingFactor = 102.40655401945725


    def getDistance(self):
        return self.getAverageVoltage() * self.scalingFactor
