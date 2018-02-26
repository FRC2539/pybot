from .pivotcommand import PivotCommand

import subsystems

class PivotToCommand(PivotCommand):
    '''Pivot to a specified angle using the gyroscope.'''

    def __init__(self, targetDegrees, reverse=False):
        super().__init__(
            targetDegrees,
            reverse,
            'Pivot to %f degrees' % targetDegrees
        )

        self.targetDegrees = targetDegrees


    def initialize(self):
        self.distance = subsystems.drivetrain.getAngleTo(self.targetDegrees)

        super().initialize(self)
