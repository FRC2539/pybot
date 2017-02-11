from wpilib.command import InstantCommand

import custom.driverhud as driverhud

class AlertCommand(InstantCommand):

    def __init__(self, msg):
        '''Show an alert on the dashboard'''

        self.msg = msg


    def initialize(self):
        driverhud.showAlert(self.msg)
