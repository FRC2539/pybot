from wpilib.command.conditionalcommand import ConditionalCommand
from commands.alertcommand import AlertCommand
from commands.gear.hanggearcommandgroup import HangGearCommandGroup

import subsystems

class GearInBotCommand(ConditionalCommand):
    def __init__(self):
        super().__init__("GearInBotCommand", HangGearCommandGroup(), AlertCommand("No Gear in bot"))

    def condition(self):
        print("running")
        return subsystems.gear.hasGear()
