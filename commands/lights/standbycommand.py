from wpilib.command import Command

import subsystems

class StandbyCommand(Command):
    def __init__(self):
        super().__init__('Blinking Lights', 5)

        self.requires(subsystems.lights)


    def initialize(self):
        self.last = None


    def execute(self):
        if self.isTimedOut():
            if int(self.timeSinceInitialized()) != self.last:
                self.last = int(self.timeSinceInitialized())

                if self.last % 2 == 0:
                    subsystems.lights.off(0)
                    subsystems.lights.off(1)
                    subsystems.lights.off(2)
                else:
                    subsystems.lights.on(0)
                    subsystems.lights.on(1)
                    subsystems.lights.on(2)
