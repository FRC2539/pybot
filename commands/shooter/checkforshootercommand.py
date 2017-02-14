from wpilib.command.conditionalcommand import ConditionalCommand
from commands.alertcommand import AlertCommand
from .shootcommandgroup import ShootCommandGroup

import subsystems

class CheckForShooterCommand(ConditionalCommand):
    def __init__(self):
        super().__init__("CheckForShooterCommand", ShootCommandGroup(), AlertCommand("Boiler not found."))

    def condition(self):
        print("running")
        return subsystems.shooter.isVisible()
