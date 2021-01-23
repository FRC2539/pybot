from .genericcontroller import GenericController


class ThrustmasterJoystick(GenericController):
    """
    Thrustmaster joystick
    """

    namedButtons = {
        "Trigger": 1,
        "BottomThumb": 2,
        "LeftThumb": 3,
        "RightThumb": 4,
        "LeftTopLeft": 5,
        "LeftTopMiddle": 6,
        "LeftTopRight": 7,
        "LeftBottomRight": 8,
        "LeftBottomMiddle": 9,
        "LeftBottomLeft": 10,
        "RightTopRight": 11,
        "RightTopMiddle": 12,
        "RightTopLeft": 13,
        "RightBottomLeft": 14,
        "RightBottomMiddle": 15,
        "RightBottomRight": 16,
    }

    namedAxes = {"X": 0, "Y": 1, "Z": 2, "Slider": 3}

    invertedAxes = ["Y", "Slider"]
