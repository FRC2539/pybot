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

ColorWheelPorts.motorID = 12
ColorWheelPorts.wwMotorID = 15

hood = PortsList

hood.motorID = 7
hood.absoluteThroughbore = 9 # DI/O

IntakePorts = PortsList()

IntakePorts.motorID = 13

IntakePorts.sensorID = 4 # on DI/O; 5 for power

limelight = PortsList()

turret = PortsList()

turret.motorID = 8
turret.limitSwitch = 8 # on DI/O;

shooter = PortsList()

shooter.motorID = 5
shooter.motorTwoID = 6

ballsystem = PortsList()

ballsystem.lowerConveyor = 10
ballsystem.verticalConveyor = 9

ballsystem.shooterSensor = 2 # on DI/O; 3 for power
ballsystem.horizontalConveyorSensor = 0 # On DIO; 1 for power

climber = PortsList()

climber.motorID = 14

winch = PortsList()

winch.motorID = 12

windshieldwiper = PortsList()

windshieldwiper.motorID = 12

pneumaticSystem = PortsList()

pneumaticSystem.pcmID = 17

pneumaticSystem.climberSolenoidForward = 0 # On PCM
pneumaticSystem.climberSolenoidReverse = 1 # On PCM

pneumaticSystem.colorWheelSolenoidForward = 2 # On PCM
pneumaticSystem.colorWheelSolenoidReverse = 3 # On PCM

trolley = PortsList()
