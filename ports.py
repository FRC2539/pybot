
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
drivetrain.frontLeftMotorID = 9
drivetrain.frontRightMotorID = 4

elevator = PortsList() # CHECK THE ID'S; PROBABLY ARE WRONG

elevator.elevatorWheelMotorID = 3
elevator.elevatorBeltMotorID  = 0
### Connected to Spark

indexwheel = PortsList() # CHECK THE ID'S; PROBABLY ARE WRONG

indexwheel.indexWheelMotorID = 7

shooter = PortsList()

shooter.shooterMotorID = 8
