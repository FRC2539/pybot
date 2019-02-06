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
drivetrain.frontLeftMotorID = 1
drivetrain.frontRightMotorID = 3
drivetrain.backLeftMotorID = 2
drivetrain.backRightMotorID = 4

lights = PortsList()
'''PWM'''
lights.lightControllerID = 0

elevator = PortsList()
elevator.motorID = 5
elevator.limit = 0

intake = PortsList()
intake.motorID = 10

arm = PortsList()
arm.motorID = 6

climber = PortsList()
climber.backRackMotorID = 11
climber.leftRackMotorID = 9
climber.rightRackMotorID = 8
climber.driveMotorID = 7
