from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from commands.lights.bluelightscommand import BlueLightsCommand
from commands.lights.redlightscommand import RedLightsCommand

class PoliceChaseCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Police Chase')

        @fc.WHILE(lambda: True)
        def lights(self):
            self.addSequential(BlueLightsCommand(), 0.5)
            self.addSequential(RedLightsCommand(), 0.5)
