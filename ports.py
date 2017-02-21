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
drivetrain.frontLeftMotorID = 1
drivetrain.frontRightMotorID = 3
drivetrain.backLeftMotorID = 2
drivetrain.backRightMotorID = 4

# Analog Input
drivetrain.ultrasonicPort = 0


shooter = PortsList()

shooter.motorID = 5


pickup = PortsList()

pickup.motorID = 6


climber = PortsList()

climber.motorID = 7
climber.sensorID = 1


feeder = PortsList()

feeder.motorID = 8
feeder.sensorID = 2


gear = PortsList()

# Optical gear sensor in DIO
gear.sensorID = 3

# Relay for LED light ring
gear.lightRingPort = 0
