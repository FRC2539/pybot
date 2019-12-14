from .logitechdualshock import LogitechDualshock
from . import logicalaxes

from wpilib import XboxController
from wpilib.interfaces import GenericHID

class BuildLayout:
    def __init__(self, driver, operator, funcsD, funcsO):
        self.controllerUno = XboxController(driver) # LogitechDualshock(_id) Make sure the controller is in Xinput mode.
        self.controllerDos = XboxController(operator)

        self.buttonID = LogitechDualshock

        self.functionsD = funcsD
        self.functionsO = funcsO

        self.buttonsToXboxDriver = {'A' : self.controllerUno.getAButtonPressed}

    def getX(self):
        return self.controllerUno.getX(0) # 0 is left, 1 is right

    def getY(self):
        return self.controllerUno.getY(0)

    def getRotate(self):
        return self.controllerUno.getX(1)

    def checkEarly(self):
        for func in self.functionsD:
            for var in func:
                if not type(var) is str:
                    raise TypeError('Check functions list for driver or operator in robot.py. They need to be valid strings; We got "' + str(var) + '" in "' + str(func) + '".')
        for func in self.functionsO:
            for var in func:
                if not type(var) is str:
                    raise TypeError('Check functions list for operator in robot.py. They need to be valid strings; We got "' + str(var) + '" in "' + str(func) + '".')

    def checkDriver(self):
        for func in self.functionsD: # Takes given functions, takes command from buttonsToXbox, and watches it.
            print(func)
            self.command = self.buttonsToXboxDriver[func[0]]
            if self.command():
                return func[1], func[2]
        return False, False

