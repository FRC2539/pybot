




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

climbhook = PortsList()
climbhook.hookMotor = 9

winch = PortsList()
winch.mainmotor = 6

intake = PortsList()
intake.leftmainmotor = 8
intake.rightmainmotor = 7
intake.lightSensorID = 0

elevator = PortsList()
elevator.motorID = 5

pneumatics = PortsList()
