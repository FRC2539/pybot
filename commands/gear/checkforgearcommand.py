from wpilib.command.conditionalcommand import ConditionalCommand
from commands.alertcommand import AlertCommand
from .hanggearcommandgroup import HangGearCommandGroup

import subsystems

class CheckForGearCommand(ConditionalCommand):
    def __init__(self):
        super().__init__(HangGearCommandGroup(), AlertCommand("Lift not found."))

    def condition(self):
        return subsystems.gear.isVisible()
