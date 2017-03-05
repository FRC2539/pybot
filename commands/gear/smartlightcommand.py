from wpilib.command.command import Command
from wpilib.timer import Timer
from networktables import NetworkTables

import subsystems

class SmartLightCommand(Command):
    '''Turns off the light when it gets too close to the target.'''

    _started = False

    def __init__(self):
        super().__init__('Smart LED Ring Control')

        self.requires(subsystems.gear)
        self.timer = Timer()
        self.on = False


    def initialize(self):
        if SmartLightCommand._started:
            return

        SmartLightCommand._started = True
        self.on = subsystems.gear.isLightOn()
        self.timer.start()


    def execute(self):
        distance = subsystems.gear.getLiftDistance()

        if distance is None:
            # Turn on the light if we haven't seen the target for two seconds
            if not self.on and self.timer.get() > 2:
                self.on = True
                subsystems.gear.turnOnLight()

            return

        if distance < 88:
            self.timer.reset()

            if self.on:
                self.on = False
                subsystems.gear.turnOffLight()

        elif not self.on and distance > 90:
            self.on = True
            subsystems.gear.turnOnLight()
