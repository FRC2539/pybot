from .skiddrive import SkidDrive

import ports
from custom.analogultrasonic import AnalogUltrasonic

class DriveTrain(SkidDrive):
    '''
    A custom drive train for the current year's game. Only add functionality
    here if it isn't likely to be used again in future seasons.
    '''

    def __init__(self):
        super().__init__('DriveTrain')

        self.ultrasonic = AnalogUltrasonic(ports.drivetrain.ultrasonicPort)


    def getFrontClearance(self):
        return self.ultrasonic.getDistance() - 8
