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

        self.rightRackMotor.setInverted(True)
        self.driveMotor.setInverted(True)

        self.rearRackMotor.setSafetyEnabled(False)
        self.rightRackMotor.setSafetyEnabled(False)
        self.leftRackMotor.setSafetyEnabled(False)
        self.driveMotor.setSafetyEnabled(False)


    def getRightLimit(self):
        return not self.rightLimit.get()


    def getLeftLimit(self):
        return not self.leftLimit.get()


    def getRearLimit(self):
        return not self.rearLimit.get()


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
        self.extendRight()
        self.extendLeft()
        self.extendRear()
        return self.getRightLimit() and self.getLeftLimit() and self.getRearLimit()


    def extendLeft(self):
        atLimit = self.getLeftLimit()
        if not atLimit:
            self.leftRackMotor.set(0.75)
        else:
            self.stopLeftRack()


    def extendRight(self):
        atLimit = self.getRightLimit()
        if not atLimit:
            self.rightRackMotor.set(0.75)
        else:
            self.stopRightRack()


    def extendRear(self):
        atLimit = self.getRearLimit()
        if not atLimit:
            self.rearRackMotor.set(0.8)
        else:
            self.stopRearRack()


    def retractAll(self):
        self.retractFront()
        self.retractRear()


    def retractFront(self):
        self.retractRight()
        self.retractLeft()


    def retractRight(self):
        self.rightRackMotor.set(-1)


    def retractLeft(self):
        self.leftRackMotor.set(-1)


    def retractRear(self):
        self.rearRackMotor.set(-1)


    def stopDrive(self):
        self.driveMotor.set(0)


    def driveForward(self):
        self.driveMotor.set(1)


    def creepForward(self):
        self.driveMotor.set(0.3)


    def driveBackward(self):
        self.driveMotor.set(-0.8)
