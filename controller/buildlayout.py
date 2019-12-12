from .logitechdualshock import LogitechDualshock
from . import logicalaxes

from wpilib.interfaces import GenericHID

class BuildLayout:
    def __init__(self, _id, layout):
        self.controller = GenericHID(_id) # LogitechDualshock(_id)

        self.buttonID = LogitechDualshock

        self.layout = layout

    def getX(self):
        return self.controller.getRawAxis(0)

    def getY(self):
        return self.controller.getRawAxis(1)

    def getRotate(self):
        return self.controller.getRawAxis(2)


    def returnObj(self):
        return self.controller

    def check(self):
        for buttonName, action in self.layout.items():
        # Button name should be a string and action should be a method.
            #if self.controller.buttonName.when
            if self.controller.getRawButtonPressed(self.namedButtons[buttonName]):
                action()
    
