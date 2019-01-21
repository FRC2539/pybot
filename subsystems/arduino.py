from .debuggablesubsystem import DebuggableSubsystem
from wpilib import SerialPort
from time import sleep


class Arduino(DebuggableSubsystem):
    '''Hopefully talks to the arduino and makes a friend.'''

    def __init__(self):
        super().__init__('Arduino')
        '''
        self.arduino = SerialPort(9600, SerialPort.Port.kUSB)
        sleep(3)
        self.string = ''
        self.count = 1
        self.string = self.arduino.readString()
        print(self.string + '     ' + str(self.count))
        sleep(3)
        self.count = 2
        self.string = self.arduino.readString()
        print(self.string + '     ' + str(self.count))
        '''
