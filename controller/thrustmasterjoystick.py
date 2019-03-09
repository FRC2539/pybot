from .genericcontroller import GenericController

class ThrustmasterJoystick(GenericController):

    #Please forgive me for these redundant button names. It goes: Side in reference to the stick, then position

    namedAxes = {
        'X': 0,
        'Y': 1,
        'Rotate': 2,
        'Slider': 3
        }

    namedButtons = {
        'trigger' : 1,
        'bottomThumb' : 2,
        'leftThumb' : 3,
        'rightThumb' : 4,
        'RightRightTop' : 5,
        'RightMiddleTop' : 6,
        'RightLeftTop' : 7,
        'RightLeftBottom' : 8,
        'RightMiddleBottom' : 9,
        'RightRightBottom' : 10,
        'LeftLeftTop' : 11,
        'LeftMiddleTop' : 12,
        'LeftRightTop' : 13,
        'LeftRightBottom' : 14,
        'LeftMiddleBottom' : 15,
        'LeftLeftBottom' : 16
        }

    invertedAxes = ['Y', 'Slider']
