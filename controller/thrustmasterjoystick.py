from .genericcontroller import GenericController

class ThrustmasterJoystick(GenericController):
    '''
    Thrustmaster joystick
    '''
    
    buttonNames = {
        
        'Trigger': 1,
        'BottomThumb': 2,
        'LeftThumb': 3,
        'RightThumb': 4,
        'LeftTopLeft': 5,
        'LeftTopMiddle': 6,
        'LeftTopRight': 7,
        'LeftBottomRight': 8,
        'LeftBottomMiddle': 9,
        'LeftBottomLeft': 10,
        'RightTopRight': 11,
        'RightTopMiddle': 12,
        'RightTopLeft': 13,
        'RightBottomLeft': 14,
        'RightBottomMiddle': 15,
        'RightBottomRight': 16
        }
    
    namedAxes = {
        'LeftX': 0,
        'LeftY': 1,
        'RightX': 2,
        'RightY': 3,
        'DPadX': 4,
        'DPadY': 5
        }
    
    invertedAxes = ['LeftY', 'RightY', 'DPadY']

