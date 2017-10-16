from wpilib.command.command import Command

import subsystems

class WaitForLiftCommand(Command):
    '''Pauses until the lift is visible in the camera'''

    def __init__(self):
        super().__init__('Wait Until Lift Is Visible')


    def isFinished(self):
        return subsystems.gear.isLiftVisible()
