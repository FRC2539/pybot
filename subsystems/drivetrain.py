from .skiddrive import *

class DriveTrain(SkidDrive):
        '''
        A custom drive train for the current year's game. Only add functionality
        here if it isn't likely to be used again in future seasons.
        '''

        def __init__(self):
            super().__init__('DriveTrain')
            

def rebuildDT():

    parent = rebuild()

    print(parent.__bases__)

    class DriveTrain(parent):
        '''
        A custom drive train for the current year's game. Only add functionality
        here if it isn't likely to be used again in future seasons.
        '''

        def __init__(self):
            super().__init__('DriveTrain')
            
    return DriveTrain
