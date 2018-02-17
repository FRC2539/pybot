'''
This is the place where we store port numbers for all subsystems. It is based on
the RobotMap concept from WPILib. Each subsystem should have its own ports list.
Values other than port numbers should be stored in Config.
'''

class PortsList:
    '''Dummy class used to store variables on an object.'''
    pass

drivetrain = PortsList()

'''CAN IDs for motors'''
drivetrain.frontLeftMotorID = 2
drivetrain.frontRightMotorID = 4
drivetrain.backLeftMotorID = 1
drivetrain.backRightMotorID = 3

drivetrain.ultrasonicPort = 0

intake = PortsList()

intake.leftMotorID = 8
intake.rightMotorID = 7

intake.lightSensorID = 0

elevator = PortsList()

elevator.motorID = 5

climber = PortsList()

climber.hookMotorID = 9
climber.winchMotorID = 6
