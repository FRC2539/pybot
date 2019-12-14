from .logitechdualshock import LogitechDualshock
from . import logicalaxes

from wpilib import XboxController
from wpilib.interfaces import GenericHID

class BuildLayout:
    def __init__(self, driver, operator, funcsD, funcsO):
        self.controllerUno = XboxController(driver) # LogitechDualshock(_id) Make sure the controller is in Xinput mode. Also, 0 is left, and 1 is right
        self.controllerDos = XboxController(operator)

        self.buttonID = LogitechDualshock

        self.functionsD = funcsD
        self.functionsO = funcsO

        self.commandDr = None
        self.commandOp = None

        self.buttonsToXboxDriver = {
                                    'A' : self.controllerUno.getAButtonPressed,
                                    'X' : self.controllerUno.getXButtonPressed,
                                    'Y' : self.controllerUno.getYButtonPressed,
                                    'B' : self.controllerUno.getBButtonPressed,
                                    'Back' : self.controllerUno.getBackButtonPressed,
                                    'Start' : self.controllerUno.getStartButtonPressed,
                                    'LeftTrigger' : self.getLeftTriggerDriver,              # Use this for a shoot or something. Use axis elsewhere.
                                    'RightTrigger' : self.getRightTriggerDriver,            # Same as above.
                                    'LeftBumper' : self.controllerUno.getBumperPressed(0),
                                    'RightBumper' : self.controllerUno.getBumperPressed(1),
                                    'LeftStick' : self.controllerUno.getStickButtonPressed(0),
                                    'RightStick' : self.controllerUno.getStickButtonPressed(1)
                                    }

        self.buttonsToXboxOp = {
                                'A' : self.controllerDos.getAButtonPressed,
                                'X' : self.controllerDos.getXButtonPressed,
                                'Y' : self.controllerDos.getYButtonPressed,
                                'B' : self.controllerDos.getBButtonPressed,
                                'Back' : self.controllerDos.getBackButtonPressed,
                                'Start' : self.controllerDos.getStartButtonPressed,
                                'LeftTrigger' : self.getLeftTriggerOp,              # Use this for a shoot or something. Use axis elsewhere.
                                'RightTrigger' : self.getRightTriggerOp,            # Same as above.
                                'LeftBumper' : self.controllerDos.getBumperPressed(0),
                                'RightBumper' : self.controllerDos.getBumperPressed(1),
                                'LeftStick' : self.controllerDos.getStickButtonPressed(0),
                                'RightStick' : self.controllerDos.getStickButtonPressed(1)
                                }

        # TODO incorporate the dpad.

    ''' The following are for trigger bool statements '''
    def getRightTriggerDriver(self):
        if self.controllerUno.getTriggerAxis(1) > 0.05:
            return True
        else:
            return False

    def getLeftTriggerDriver(self):
        if self.controllerUno.getTriggerAxis(0) > 0.05:
            return True
        else:
            return False
    def getRightTriggerOp(self):
        if self.controllerDos.getTriggerAxis(1) > 0.05:
            return True
        else:
            return False
    def getLeftTriggerOp(self):
        if self.controllerDos.getTriggerAxis(0) > 0.05:
            return True
        else:
            return False


    ''' The following are for trigger scaling statements. '''

    def getRightTriggerAxisDriver(self):
        return self.controllerUno.getTriggerAxis(1)

    def getLeftTriggerAxisDriver(self):
        return self.controllerUno.getTriggerAxis(0)

    def getRightTriggerAxisOp(self):
        return self.controllerDos.getTriggerAxis(1)

    def getLeftTriggerAxisOp(self):
        return self.controllerDos.getTriggerAxis(0)


    def getX(self):
        return self.controllerUno.getX(0)

    def getY(self):
        return self.controllerUno.getY(0)

    def getRotate(self):
        return self.controllerUno.getX(1)

    def checkEarly(self):
        ''' Checks for valid inputs '''
        for func in self.functionsD:
            for var in func:
                if not type(var) is str:
                    raise TypeError('Check functions list for driver or operator in robot.py. They need to be valid strings; We got "' + str(var) + '" in "' + str(func) + '".')
        for func in self.functionsO:
            for var in func:
                if not type(var) is str:
                    raise TypeError('Check functions list for operator in robot.py. They need to be valid strings; We got "' + str(var) + '" in "' + str(func) + '".')

    def checkDriver(self):
        ''' Checks for driver action '''
        for func in self.functionsD: # Takes given functions, takes command from buttonsToXbox, and watches it.
            self.commandDr = self.buttonsToXboxDriver[func[0]]
            if self.commandDr(): # Checks to see if returns true. This will NOT work with scaling triggers!
                return func[1], func[2]
        return False, False

    def checkOperator(self):
        ''' Checks for operator action '''
        for func in self.functionsO: # Takes given functions, takes command from buttonsToXbox, and watches it.
            self.commandOp = self.buttonsToXboxOp[func[0]]
            if self.commandOp(): # Checks to see if returns true. This will NOT work with scaling triggers!
                return func[1], func[2]
        return False, False
