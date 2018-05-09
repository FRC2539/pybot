from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

import subsystems

from .network.alertcommand import AlertCommand

class StartUpCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Start Up')
        self.setRunWhenDisabled(True)
