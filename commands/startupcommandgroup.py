from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

import subsystems

from .drivetrain.resettiltcommand import ResetTiltCommand
from .elevator.resetelevatorcommand import ResetElevatorCommand
from .network.alertcommand import AlertCommand

class StartUpCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Start Up')
        self.setRunWhenDisabled(True)

        self.addParallel(ResetTiltCommand())

        @fc.IF(lambda: subsystems.elevator.getHeight() > 1000)
        def resetElevator(self):
            self.addParallel(ResetElevatorCommand())
            self.addParallel(AlertCommand('Reset elevator position'))
