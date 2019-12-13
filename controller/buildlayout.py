from .logitechdualshock import LogitechDualshock
from . import logicalaxes

from wpilib import XboxController
from wpilib.interfaces import GenericHID

class BuildLayout:
    def __init__(self, _id, layout):
        self.controller = XboxController(_id) # LogitechDualshock(_id) Make sure the controller is in Xinput mode.

        self.buttonID = LogitechDualshock

        self.layout = layout

    def getX(self):
        return self.controller.getX(0) # 0 is left, 1 is right

    def getY(self):
        return self.controller.getY(0)

    def getRotate(self):
        return self.controller.getX(1)

    def returnObj(self):
        return self.controller

    def check(self):
        pass
