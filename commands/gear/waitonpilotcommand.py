from wpilib.command.timedcommand import Command

import subsystems

class WaitOnPilotCommand(Command):
    '''Keeps the robot in place while the gear is removed.'''

    def __init__(self):
        super().__init__('Wait on Pilot', 4)
        self.requires(subsystems.drivetrain)


    def initialize(self):
        self.setInterruptible(False)


    def isFinished(self):
        if not self.isInterruptible() and self.isTimedOut():
            self.setInterruptible(True)

        return not subsystems.gear.hasGear()
