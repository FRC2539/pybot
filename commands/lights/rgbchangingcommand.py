from wpilib.command.command import Command

import subsystems

class RGBChangingCommand(Command):

    def __init__(self):
        super().__init__('R G B Changing')

        self.requires(subsystems.lights)
        self.colorvalue = 0

    def initialize(self):
        pass

    def execute(self):
        if self.colorvalue <= 1:
            subsystems.lights.solidRed()
            self.colorvalue += 1

        elif self.colorvalue <= 2:
            subsystems.lights.solidGreen()
            self.colorvalue += 1

        elif self.colorvalue <= 3:
            subsystems.lights.solidBlue()
            self.colorvalue = 0

        else:
            self.colorvalue = 0
            print('Uh-oh')

    def end(self):
        subsystems.lights.off()
