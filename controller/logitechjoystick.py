from .genericcontroller import GenericController

class LogitechJoystick(GenericController):
    '''
    Represents a Logitech Joystick.
    '''

    namedButtons = {
        'trigger': 1,
        'topThumb': 2,
        'bottomThumb': 3,
        'leftThumb': 4,
        'rightThumb': 5,
        'Button6': 6,
        'Button7': 7,
        'Button8': 8,
        'Button9': 9,
        'Button10': 10,
        'Button11': 11
        }

    namedAxes = {
        'X': 0,
        'Y': 1,
        'bottomThing': 2
    }

    invertedAxes = ['Y']
