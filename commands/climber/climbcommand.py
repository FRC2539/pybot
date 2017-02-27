from wpilib.command import Command
from networktables import NetworkTables

import subsystems
from custom import driverhud

class ClimbCommand(Command):
    '''
    Signal the Jetson to draw a rope marker on the camera output and start
    spinning the winch.
    '''

    def __init__(self):
        super().__init__('Climb')

        self.requires(subsystems.climber)
        self.vision = NetworkTables.getTable('cameraTarget')


    def initialize(self):
        if not subsystems.climber.atTop():
            subsystems.climber.start()
            self.vision.putBoolean('climbing', True)
        else:
            driverhud.showAlert('Already at top')


    def isFinished(self):
        return subsystems.climber.atTop()


    def end(self):
        subsystems.climber.stop()
        self.vision.putBoolean('climbing', False)
