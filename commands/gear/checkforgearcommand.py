from wpilib.command.conditionalcommand import ConditionalCommand
from commands.alertcommand import AlertCommand
from .hanggearcommandgroup import HangGearCommandGroup

import subsystems

# Check whether the robot sees a lift.
class CheckForGearCommand(ConditionalCommand):
    def __init__(self):
        super().__init__("CheckForGearCommand", HangGearCommandGroup(), AlertCommand("Lift not found."))

    def condition(self):
        print("running")
        return subsystems.gear.isVisible()
