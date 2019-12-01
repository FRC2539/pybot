from .genericcontroller import GenericController

class LogitechDualshock(GenericController):
    namedButtons = {
        'A':2,
        'B':3,
        'X':1,
        'Y':4,
        'LeftBumper':5,
        'RightBumper':6,
        'LeftTrigger':7,
        'RightTrigger':8,
        'Back':9,
        'Start':10,
        'LeftJoystick':11,
        'RightJoystick':12,
        'DPadUp':20,
        'DPadDown':22,
        'DPadLeft':23,
        'DPadRight':21
        }
    namedAxes = {
        'LeftX':0,
        'LeftY':1,
        'RightX':2,
        'RightY':3,
        'DPadX':4,
        'DpadY':5
        }
    
    invertedAxed = ['LeftY', 'RightY', 'DPadY']
