from wpilib.command.command import Command
import time
import robot

class BlinkLightsCommand(Command):

    def __init__(self, color, delay=0.01):
        super().__init__('Blink Lights')

        self.requires(robot.lights)
        self.color = color
        self.delay = delay


    def initialize(self):
        self.count = 0


    def execute(self):
        if self.count == 10:
            robot.lights.setSpecific(robot.lights.colors[self.color])
        elif self.count == 20:
            robot.lights.off()
            self.count = 0

        self.count += 1
        time.sleep(self.delay)


    def end(self):
        robot.lights.off()
