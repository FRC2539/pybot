#!/usr/bin/env python3

import sys

from wpilib.command import Command

from wpilib import Joystick
from wpilib.buttons import JoystickButton

from wpilib.buttons import Button

from commandbased import CommandBasedRobot
from wpilib._impl.main import run
from wpilib import RobotBase



class FaultyCommand(Command):
    def __init__(self):
        super().__init__('Faulty')

    def initialize(self):
        print('Test statement')

class GenericController(Joystick):
    '''The base class for all controllers.'''

    namedButtons = {}
    namedAxes = {}
    invertedAxes = []

    def __init__(self, port):
        '''
        Creates attributes of this class for every button and axis defined in
        its dictionaries. Subclasses need only fill in those dictionaries
        correctly.
        '''

        super().__init__(port)

        for name, id  in self.namedButtons.items():
            if id >= 20:
                '''
                By convention, the DPad buttons are 20 through 23 and can be
                converted to POV angles by the formula below.
                '''

                angle = (id - 20) * 90
                self.__dict__[name] = POVButton(self, angle)
            else:
                self.__dict__[name] = JoystickButton(self, id)

        for name, id in self.namedAxes.items():
            isInverted = name in self.invertedAxes
            self.__dict__[name] = ControllerAxis(self, id, isInverted)

class POVButton(Button):
    '''
    Turns DPad readings into button presses, so they can be used like any other
    button.
    '''

    def __init__(self, controller, angle):
        '''
        Pressing up on the DPad returns 0, up/right returns 45, right return 90
        and so on. So, we can tell if a button is pressed if the reading is
        within 45 degrees of the passed angle.
        '''

        self.validAngles = [angle, angle - 45, angle + 45]
        self.validAngles = [x % 360 for x in self.validAngles]

        self.controller = controller


    def get(self):
        '''Whether the button is pressed or not.'''

        return self.controller.getPOV() in self.validAngles

class ControllerAxis:
    '''Represents an axis of a joystick.'''

    def __init__(self, controller, id, isInverted):
        '''
        An axis is considered inverted if pushing up gives a negative result.
        In that case, we multiply its value by -1 before returning it.
        '''

        if isInverted:
            self.get = lambda: -1 * controller.getRawAxis(id)
        else:
            self.get = lambda: controller.getRawAxis(id)

class LogitechDualShock(GenericController):
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
        'LeftX': 0,
        'LeftY': 1,
        'RightX': 2,
        'RightY': 3,
        'DPadX': 4,
        'DPadY': 5
    }

    invertedAxes = ['LeftY', 'RightY', 'DPadY']


class Robot(CommandBasedRobot):
    '''Implements a Command Based robot design'''

    def robotInit(self):
        '''Set up everything we need for a working robot.'''

        controller = LogitechDualShock(0)
        controller.DPadUp.toggleWhenPressed(FaultyCommand())

        '''
        If you make the above line any of the other directional pad directions, it will seg fault.
        However, 'A', for example, works fine.
        '''

    def autonomousInit(self):
        '''This function is called each time autonomous mode starts.'''

        pass

    def handleCrash(self, error):
        super().handleCrash()
        pass


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)

    run(Robot)
