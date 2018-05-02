from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

import robot

from .drivetrain.resettiltcommand import ResetTiltCommand
from .elevator.resetelevatorcommand import ResetElevatorCommand
from .network.alertcommand import AlertCommand

class StartUpCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Start Up')
        self.setRunWhenDisabled(True)

        self.addParallel(ResetTiltCommand())

        @fc.IF(lambda: abs(robot.elevator.getHeight()) > 1000)
        def resetElevator(self):
            self.addSequential(AlertCommand(
                'Code restarted when elevator is not at ground level')
            )
            self.addSequential(AlertCommand(
                'If elevator is at ground level, you must reset the elevator',
                'Info'
            ))
