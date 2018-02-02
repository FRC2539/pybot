from .skiddrive import SkidDrive
import ports
from custom.analogultrasonic import AnalogInput

class DriveTrain(SkidDrive):
    '''
    A custom drive train for the current year's game. Only add functionality
    here if it isn't likely to be used again in future seasons.
    '''

    def __init__(self):
        super().__init__('DriveTrain')
'''
        self.ultrasonic = AnalogInput(ports.drivetrain.ultrasonicPort)


    def getUltrasonic(self):
        return (self.ultrasonic.getDistance() * 1.008374 + .5762796)
'''
