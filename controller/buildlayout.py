from .logitechdualshock import LogitechDualshock
from . import logicalaxes

from wpilib import XboxController
from wpilib.interfaces import GenericHID

class BuildLayout:
    def __init__(self, driver, operator, funcs):
        self.controllerUno = XboxController(driver) # LogitechDualshock(_id) Make sure the controller is in Xinput mode.
        self.controllerDos = XboxController(operator)

        self.buttonID = LogitechDualshock

        self.functions = funcs

        self.buttonsToXboxDriver = {'A' : self.controllerUno.getAButtonPressed}

    def getX(self):
        return self.controllerUno.getX(0) # 0 is left, 1 is right

    def getY(self):
        return self.controllerUno.getY(0)

    def getRotate(self):
        return self.controllerUno.getX(1)

    def checkDriver(self):
        for buttonName, funcStr in self.functions.items(): # Takes given functions, takes command from buttonsToXbox, and watches it.
            self.command = self.buttonsToXboxDriver[buttonName]
            if self.command():
                return funcStr
        return False

