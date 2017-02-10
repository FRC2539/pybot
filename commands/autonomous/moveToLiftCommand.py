from wpilib.command import Command
from .turncommand import TurnCommand
from .movecommand import MoveCommand
import subsystems

class moveToLiftCommand(Command):

    def __init__(self):
        super().__init__('MoveToLiftCommand')


    def initialize(self):
        if subsystems.gear.isTargetVisible():
            TurnCommand(subsystems.gear.offsetFromTarget())
            MoveCommand(subsystems.gear.distanceToTarget() - 12)


    def isFinished(self):
        if subsystems.gear.offsetFromTarget() < 5 and subsystems.gear.distanceToTarget() < 12:
            return True
        return False
