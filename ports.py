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

Elevator = PortsList()

Elevator.ElevatorMotorID = 5
Elevator.lowerLimit = 1 # DI/O

CargoIntake = PortsList()

CargoIntake.CargoMotorID = 10

HatchIntake = PortsList()

HatchIntake.HatchMotorID = 12
HatchIntake.rightLimitSwitch = 0 # DI/O
HatchIntake.leftLimitSwitch = 6 # DI/O
