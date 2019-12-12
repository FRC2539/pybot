from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton # Can't use this... for command based only :(

from .controlleraxis import ControllerAxis
from .povbutton import POVButton

class GenericController(Joystick):
    '''The base class for all controllers '''
    
    namedButtons = {}
    namedAxes = {}
    invertedAxes = []
    
    def __init__(self, port):
        super().__init__(port)
        
        for name, id in self.namedButtons.items():
            if id >= 20:
                angle = (id - 20) * 90
                self.__dict__[name] = POVButton(self, angle)
            else:
                self.__dict__[name] = JoystickButton(self, id)
                
        for name, id in self.namedAxes.items():
            isInverted = name in self.invertedAxes
            self.__dict__[name] = ControllerAxis(self, id, isInverted)
