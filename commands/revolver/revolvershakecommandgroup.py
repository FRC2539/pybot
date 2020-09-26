import commandbased.flowcontrol as fc


class RevolverShakeCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Revolver Shake')

        # Add commands here with self.addSequential() and self.addParallel()
        
