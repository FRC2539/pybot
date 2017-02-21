from wpilib.command import Command
from networktables import NetworkTables

import subsystems

class ClimbCommand(Command):
    # Initialize the named command.
    def __init__(self):
        super().__init__('Climb')

        self.requires(subsystems.climber)
        self.vision = NetworkTables.getTable('cameraTarget')

    def initialize(self):
        subsystems.climber.start()
        self.vision.putBoolean('climbing', True)

    def isFinished(self):
        return subsystems.climber.atTop()

    def end(self):
        subsystems.climber.stop()
        self.vision.putBoolean('climbing', False)
