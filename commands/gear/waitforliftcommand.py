from wpilib.command.timedcommand import TimedCommand

import subsystems

class WaitForLiftCommand(TimedCommand):
    '''
    Pauses until the lift is visible in the camera. If the lift does not appear
    by the timeout, the command finished anyhow.
    '''

    def __init__(self, timeout=2):
        super().__init__('Wait Until Lift Is Visible', timeout)


    def isFinished(self):
        return subsystems.gear.isLiftVisible() or super().isFinished()
