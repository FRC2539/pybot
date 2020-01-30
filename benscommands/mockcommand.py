from components.colorsensor.colorwheel import ColorWheel

from generator import Generator

import robot

class AutoSpinWheel(Generator):
    def __init__(self):
        super(AutoSpinWheel, self).__init__()

    def initialize(self):
        robot.mockcommand.getColor()
