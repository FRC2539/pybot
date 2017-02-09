from wpilib.command import CommandGroup
from .movecommand import MoveCommand
from .turncommand import TurnCommand

class ShootCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('ShootCommandGroup')
        '''self.AddSequential(Shoot())'''
