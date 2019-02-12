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
lights.lightControllerID = 0 #PWM

elevator = PortsList()
elevator.motorID = 5
elevator.lowerLimit = 1 #DIO

intake = PortsList()
intake.motorID = 10
intake.lightSensor = 0 #DIO

arm = PortsList()
arm.motorID = 6
arm.lowerLimit = 2 #DIO

climber = PortsList()
climber.backRackMotorID = 11
climber.leftRackMotorID = 9
climber.rightRackMotorID = 8
climber.driveMotorID = 7
