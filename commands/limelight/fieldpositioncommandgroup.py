import commandbased.flowcontrol as fc

from commands.turret.setturretcommand import SetTurretCommand

class FieldPositionCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Field Position')

        # Add commands here with self.addSequential() and self.addParallel()

        self.addSequential(SetTurretCommand(850), 1.5)
        self.addSequential()
