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
                                    'A' : 'getAButtonPressed()',
                                    'X' : 'getXButtonPressed()',
                                    'Y' : 'getYButtonPressed()',
                                    'B' : 'getBButtonPressed()',
                                    'Back' : 'getBackButtonPressed()',
                                    'Start' : 'getStartButtonPressed()',
                                    'LeftTrigger' : 'self.getLeftTriggerDriver()',              # Use this for a shoot or something. Use axis elsewhere.
                                    'RightTrigger' : 'self.getRightTriggerDriver()',            # Same as above.
                                    'LeftBumper' : 'getBumperPressed(0)',
                                    'RightBumper' : 'getBumperPressed(1)',
                                    'LeftStick' : 'getStickButtonPressed(0)',
                                    'RightStick' : 'getStickButtonPressed(1)',
                                    'DPadLeft' : 'getDPadLeftDriver()',
                                    'DPadRight' : 'getDPadRightDriver()'
                                    }

        self.buttonsToXboxOp = {
                                'A' : 'getAButtonPressed()',
                                'X' : 'getXButtonPressed()',
                                'Y' : 'getYButtonPressed()',
                                'B' : 'getBButtonPressed()',
                                'Back' : 'getBackButtonPressed()',
                                'Start' : 'getStartButtonPressed()',
                                'LeftTrigger' : 'self.getLeftTriggerOp()',              # Use this for a shoot or something. Use axis elsewhere.
                                'RightTrigger' : 'self.getRightTriggerOp()',            # Same as above.
                                'LeftBumper' : 'getBumperPressed(0)',
                                'RightBumper' : 'getBumperPressed(1)',
                                'LeftStick' : 'getStickButtonPressed(0)',
                                'RightStick' : 'getStickButtonPressed(1)',
                                'DPadLeft' : 'getDPadLeftOp()',
                                'DPadRight' : 'getDPadRightOp()'
                                }

        self.buttonHoldStatusD = {
                                    'A' : False,
                                    'X' : False,
                                    'Y' : False,
                                    'B' : False,
                                    'Back' : False,
                                    'Start' : False,
                                    'LeftTrigger' : False,              # Use this for a shoot or something. Use axis elsewhere.
                                    'RightTrigger' : False,            # Same as above.
                                    'LeftBumper' : False,
                                    'RightBumper' : False,
                                    'LeftStick' : False,
                                    'RightStick' : False,
                                    'DPadLeft' : False,
                                    'DPadRight' : False
                                }

        self.buttonHoldStatusO = {
                                    'A' : False,
                                    'X' : False,
                                    'Y' : False,
                                    'B' : False,
                                    'Back' : False,
                                    'Start' : False,
                                    'LeftTrigger' : False,              # Use this for a shoot or something. Use axis elsewhere.
                                    'RightTrigger' : False,            # Same as above.
                                    'LeftBumper' : False,
                                    'RightBumper' : False,
                                    'LeftStick' : False,
                                    'RightStick' : False,
                                    'DPadLeft' : False,
                                    'DPadRight' : False
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

    ''' Following is for DPad horizontal (only horizontal has an axis), both scaling and bools. '''

    def getDPadHorizontalAxisDriver(self): # Curse these long method names.
        return self.controllerUno.getRawAxis(6) # NOTE: Accesses genericHID parent class. EXPERIMENT WITH THIS TO LEARN HOW TO ASSIGN BOOLS

    def getDPadHorizontalAxisOp(self): # Curse these long method names.
        return self.controllerDos.getRawAxis(6)

    def getDPadLeftDriver(self):
        if self.controllerUno.getRawAxis(6) <= -0.9:
            return True
        else:
            return False

    def getDPadRightDriver(self):
        if self.controllerUno.getRawAxis(6) >= 0.9:
            return True
        else:
            return False

    def getDPadLeftOp(self):
        if self.controllerDos.getRawAxis(6) <= -0.9:
            return True
        else:
            return False

    def getDPadRightOp(self):
        if self.controllerDos.getRawAxis(6) >= 0.9:
            return True
        else:
            return False



    def setDualRumble(self):
        self.controllerUno.setRumble(GenericHID.RumbleType.kLeftRumble, 1) # Sets rumble to full and left side
        self.controllerUno.setRumble(GenericHID.RumbleType.kRightRumble, 1) # Sets rumble to full and right side

    def disableRumble(self):
        self.controllerUno.setRumble(GenericHID.RumbleType.kLeftRumble, 0)
        self.controllerUno.setRumble(GenericHID.RumbleType.kRightRumble, 0)

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
            try:
                self.commandDr = eval('self.controllerUno.' + str(self.buttonsToXboxDriver[func[0]]))
            except(AttributeError): # if it is not an XboxController class (like a trigger bool), the following runs.
                print('ran this')
                self.commandDr = eval(str(self.buttonsToXboxDriver[func[0]])) # If this does not work, make a seperate controller file with the methods from above, import it, instantiate an object, and then call these functions on that sucker.

            if self.commandDr and not self.buttonHoldStatusD[func[0]]:
                # Checks to see if returns true. This will NOT work with scaling triggers!
                print('Got input')
                self.buttonHoldStatusD[func[0]] = True
                return func[1], func[2]

            elif not self.commandDr:
                print('set status to false (released?)')
                self.buttonHoldStatusD[func[0]] = False
                continue

        return False, False

    def checkOperator(self):
        ''' Checks for operator action '''
        for func in self.functionsO: # Takes given functions, takes command from buttonsToXbox, and watches it.
            try:
                self.commandOp = eval('self.controllerUno.' + str(self.buttonsToXboxOp[func[0]]))
            except(AttributeError): # if it is not an XboxController class (like a trigger bool), the following runs.
                self.commandOp = eval(str(self.buttonsToXboxOp[func[0]]))

            if self.commandOp and not self.buttonHoldStatusO[func[0]]: # Checks to see if returns true. This will NOT work with scaling triggers!
                print('Got input')
                self.buttonHoldStatusO[func[0]] = True
                return func[1], func[2]

            elif not self.commandOp:
                print('set status to false (released?)')
                self.buttonHoldStatusO[func[0]] = False
                continue

        return False, False
