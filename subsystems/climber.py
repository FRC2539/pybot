from .debuggablesubsystem import DebuggableSubsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX
from wpilib import DigitalInput

import ports


class Climber(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Climber')

        self.rearRackMotor = WPI_TalonSRX(ports.climber.rearRackMotorID)
        self.rightRackMotor = WPI_TalonSRX(ports.climber.rightRackMotorID)
        self.leftRackMotor = WPI_TalonSRX(ports.climber.leftRackMotorID)
        self.driveMotor = WPI_TalonSRX(ports.climber.driveMotorID)

        self.rearLimit = DigitalInput(ports.climber.rearRackLimit)
        self.rightLimit = DigitalInput(ports.climber.rightRackLimit)
        self.leftLimit = DigitalInput(ports.climber.leftRackLimit)

        self.rearRackMotor.setNeutralMode(NeutralMode.Brake)
        self.rightRackMotor.setNeutralMode(NeutralMode.Brake)
        self.leftRackMotor.setNeutralMode(NeutralMode.Brake)
        self.driveMotor.setNeutralMode(NeutralMode.Brake)

        self.rearRackMotor.setInverted(True)
        self.rightRackMotor.setInverted(True)


    def getRightLimit(self):
        return self.rightLimit.get()


    def getLeftLimit(self):
        return self.leftLimit.get()


    def getRearLimit(self):
        return self.rearLimit.get()


    def stopRacks(self):
        self.rightRackMotor.set(0)
        self.leftRackMotor.set(0)
        self.rearRackMotor.set(0)


    def stopRightRack(self):
        self.rightRackMotor.set(0)


    def stopLeftRack(self):
        self.leftRackMotor.set(0)


    def stopRearRack(self):
        self.rearRackMotor.set(0)


    def extendAll(self):
        self.extendFront()
        self.extendRear()
        return self.getRightLimit() and self.getLeftLimit() and self.getRearLimit()


    def extendFront(self):
        if not self.getRightLimit():
            self.rightRackMotor.set(1)
        else:
            self.stopRightRack()

        if not self.getLeftLimit():
            self.leftRackMotor.set(1)
        else:
            self.stopLeftRack()


    def extendRear(self):
        if not self.getRearLimit():
            self.rearRackMotor.set(1)
        else:
            self.stopRightRack()


    def retractAll(self):
        self.retractFront()
        self.retractRear()


    def retractFront(self):
        self.rightRackMotor.set(-1)
        self.leftRackMotor.set(-1)


    def retractRear(self):
        self.rearRackMotor.set(-1)


    def stopDrive(self):
        self.driveMotor.set(0)


    def driveForward(self):
        self.driveMotor.set(1)


    def driveBackward(self):
        self.driveMotor.set(-1)
