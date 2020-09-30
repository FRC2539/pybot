from .skiddrive import SkidDrive
import robotselection

class DriveTrain(SkidDrive):
    '''
    A custom drive train for the current year's game. Only add functionality
    here if it isn't likely to be used again in future seasons.
    '''

    def __init__(self):
        super().__init__('DriveTrain')

        if self.motors[0].getFirmwareString() == 'v0.0' and not robotselection.competitionrobot.checking: # If it's a NEO
            robotselection.competitionrobot.status = True

        robotselection.competitionrobot.checking = False
