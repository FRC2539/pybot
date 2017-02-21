import subsystems

from wpilib.command.instantcommand import InstantCommand

class ToggleLightCommand(InstantCommand):

    def __init__(self):
        super().__init__('ToggleLight')
        self.requires(subsystems.gear)

    def initialize(self):
        if subsystems.gear.isLightOn():
            subsystems.gear.turnOffLight()
        else:
            subsystems.gear.turnOnLight()
