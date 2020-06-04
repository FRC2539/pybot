from .genericcontroller import GenericController

class LogitechG920(GenericController):
    '''
    Represents a Logitech Xbox controller with the underside switch set to "D"
    and mode turned off. If mode is one, the DPad and right joystick axes are
    swapped.
    '''

    namedButtons = {
        'A': 2,
        'B': 3,
        'X': 1,
        'Y': 4,
        'LeftBumper': 5,
        'RightBumper': 6,
        'LeftTrigger': 7,
        'RightTrigger': 8,
        'Back': 9,
        'Start': 10,
        'LeftJoystick': 11,
        'RightJoystick': 12,
        'DPadUp': 20,
        'DPadRight': 21,
        'DPadDown': 22,
        'DPadLeft': 23
    }

    namedAxes = {
        'RightX': 2,
        'RightY': 3,
        'DPadX': 4,
        'DPadY': 5,
        'Wheel': 0,
        'Accel': 1,
        'Brake': 2
    }

    invertedAxes = ['LeftY', 'RightY', 'DPadY']
