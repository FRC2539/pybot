" Standard port classes "

class PortsList:
    pass

DrivetrainPorts = PortsList()

DrivetrainPorts.FrontLeftMotor = 1
DrivetrainPorts.FrontRightMotor = 3
DrivetrainPorts.BackLeftMotor = 2
DrivetrainPorts.BackRightMotor = 4

Arm = PortsList()

Arm.ArmMotorID = 6
Arm.lowerLimit = 2 # DI/O
