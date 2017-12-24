'''
This is the place where we store port numbers for all subsystems. It is based on
the RobotMap concept from WPILib. Each subsystem should have its own ports list.
Values other than port numbers should be stored in Config.
'''

class PortsList:
    '''Dummy class used to store variables on an object.'''
    pass

drivetrain = PortsList()

# CAN IDs for motors
drivetrain.leftMotorID = 1
drivetrain.rightMotorID = 2

# Relay for LED light ring
lights = PortsList()
lights = [0, 1, 2]
