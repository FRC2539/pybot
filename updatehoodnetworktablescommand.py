from wpilib.command import Command

import robot

class UpdateHoodNetworkTablesCommand(Command):

    def __init__(self):
        super().__init__('Update Hood Network Tables')

        self.requires(robot.hood)

    def initialize(self):
        robot.hood.updateNetworkTables()
