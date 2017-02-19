from wpilib.command import InstantCommand

from custom import driverhud

class AlertCommand(InstantCommand):

    def __init__(self, msg):
        '''Show an alert on the dashboard'''
        super().__init__('Alert: %s' % msg)

        self.msg = msg


    def initialize(self):
        driverhud.showAlert(self.msg)


    def setMessage(self, msg):
        self.msg = msg
