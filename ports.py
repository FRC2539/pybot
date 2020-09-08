

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
drivetrain.frontRightMotorID = 2
drivetrain.backLeftMotorID = 3
drivetrain.backRightMotorID = 4

revolver = PortsList()

revolver.motorID = 6
revolver.absoluteThroughbore = 6 # DI/O

intake = PortsList()

intake.motorID = 5

balllauncher = PortsList()

balllauncher.motorID = 7

shooter = PortsList()

shooter.shooterMotorOneID = 8
shooter.shooterMotorTwoID = 9

pneumatics = PortsList()

pneumatics.PCM = 17

ledsystem = PortsList()

ledsystem.controllerID = 0 # PWM

hood = PortsList()

hood.motorID = 11
hood.absoluteThroughbore = 9 # DI/O

turret = PortsList()

turret.motorID = 10
turret.limitSwitch = 7 # DI/O

climber = PortsList()

climber.motorID = 12

