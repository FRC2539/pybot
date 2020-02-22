from wpilib.command import Command

from wpilib import Timer

import robot

class WipeFastCommand(Command):

    def __init__(self):
        super().__init__('Wipe Fast')

        self.requires(robot.windshieldwiper)
        self.timer = Timer()

    def initialize(self):
        self.timer.start()
        robot.windshieldwiper.fastWipe()

    def execute(self):
        if robot.windshieldwiper.getAmperage() >= 5.1:
            robot.windshieldwiper.swapDirection()
            robot.windshieldwiper.fastWipe()

    def end(self):
        robot.windshieldwiper.stop()
        self.timer.stop()
