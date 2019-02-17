from wpilib.command.command import Command

import robot

class PanelEjectCommand(Command):

    def __init__(self):
        super().__init__('Panel Eject')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.panelEject()

    def end(self):
        robot.elevator.stop()
