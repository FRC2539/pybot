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
        'RightRightTop' : 11,
        'RightMiddleTop' : 12,
        'RightLeftTop' : 13,
        'ClimbL2' : 14,
        'RightMiddleBottom' : 15,
        'Layout' : 16,
        'Misc' : 5,
        'LeftMiddleTop' : 6,
        'LeftRightTop' : 7,
        'ClimbL3' : 8,
        'LeftMiddleBottom' : 9,
        'LeftLeftBottom' : 10
        }

    invertedAxes = ['Y', 'Slider']
