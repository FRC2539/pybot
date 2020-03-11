" Standard port classes "

class PortsList:
    pass

DrivetrainPorts = PortsList()

DrivetrainPorts.FrontLeftMotor = 1
DrivetrainPorts.FrontRightMotor = 3 # dummy
DrivetrainPorts.BackLeftMotor = 2
DrivetrainPorts.BackRightMotor = 4

FalconTest = PortsList()

FalconTest.motorID = 5 # dummy

ColorWheelPorts = PortsList()

ColorWheelPorts.motorID = 6 # dummy

IntakePorts = PortsList()
IntakePorts.motorID = 7

TurretPorts = PortsList()

TurretPorts.motorID = 8

HoodPorts = PortsList()

HoodPorts.motorID = 9

HoodPorts.throughBore = 9 # DI/O

ShooterPorts = PortsList()

ShooterPorts.motorID = 10

LoadSystemPorts = PortsList()

LoadSystemPorts.motorID = 11
