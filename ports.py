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

ColorWheelPorts = PortsList()

ColorWheelPorts.motorID = 5

hood = PortsList

hood.motorID = 6

IntakePorts = PortsList()

IntakePorts.motorID = 7

limelight = PortsList()

turret = PortsList()

turret.motorID = 8

shooter = PortsList()

shooter.motorID = 9

ballSystem = PortsList()

ballSystem.indexWheel = 10
ballSystem.lowerConveyor = 11
ballSystem.verticalConveyor = 12
