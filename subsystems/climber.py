from .debuggablesubsystem import DebuggableSubsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX, FeedbackDevice
from wpilib import DigitalInput

import ports


class Climber(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Climber')

        self.rearRackMotor = WPI_TalonSRX(ports.climber.rearRackMotorID)
        self.rightRackMotor = WPI_TalonSRX(ports.climber.rightRackMotorID)
        self.leftRackMotor = WPI_TalonSRX(ports.climber.leftRackMotorID)

        self.leftRackMotor.setInverted(True)

        self.driveMotor = WPI_TalonSRX(ports.climber.driveMotorID)

        self.motors = [self.rearRackMotor, self.rightRackMotor, self.leftRackMotor, self.driveMotor]

        for motor in self.motors:
            motor.setSafetyEnabled(False)
            motor.setNeutralMode(NeutralMode.Brake)

        self.rearLimit = DigitalInput(ports.climber.rearRackLimit)
        self.rightLimit = DigitalInput(ports.climber.rightRackLimit)
        self.leftLimit = DigitalInput(ports.climber.leftRackLimit)

        self.rightRackMotor.setInverted(False)
        self.driveMotor.setInverted(True)

        self.rightRackMotor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)
        self.leftRackMotor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)
        self.rearRackMotor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)

        self.fPower = 0.95
        self.rPower = 1.0

        self.resetEncoders()

    def getRightLimit(self):
        return not self.rightLimit.get()


    def getLeftLimit(self):
        return not self.leftLimit.get()


    def getRearLimit(self):
        return not self.rearLimit.get()


    def resetEncoders(self):
        self.rightRackMotor.setSelectedSensorPosition(0, 0, 0)
        self.leftRackMotor.setSelectedSensorPosition(0, 0, 0)
        self.rearRackMotor.setSelectedSensorPosition(0, 0, 0)


    def getAvgPosition(self):
        return round((self.rightRackMotor.getSelectedSensorPosition(0) + self.leftRackMotor.getSelectedSensorPosition(0) + self.rearRackMotor.getSelectedSensorPosition(0)) / 3)


    def stopRacks(self):
        self.rightRackMotor.set(0)
        self.leftRackMotor.set(0)
        self.rearRackMotor.set(0)
        print(str(self.rightRackMotor.getQuadraturePosition()))
        print(str(self.leftRackMotor.getQuadraturePosition()))
        print(str(self.rearRackMotor.getQuadraturePosition()))


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


    def extendAllEnc(self):
        frontAvg = round((self.rightRackMotor.getSelectedSensorPosition(0) + self.leftRackMotor.getSelectedSensorPosition(0)) / 2)
        frontDiff = self.rightRackMotor.getSelectedSensorPosition(0) - self.leftRackMotor.getSelectedSensorPosition(0)
        diff = frontAvg - self.rearRackMotor.getSelectedSensorPosition(0)

        self.extendRightEnc(frontDiff - diff)
        self.extendLeftEnc(frontDiff - diff)
        self.extendRearEnc(diff)
        return self.getRightLimit() and self.getLeftLimit() and self.getRearLimit()


    def extendLeft(self):
        atLimit = self.getLeftLimit()
        if not atLimit:
            self.leftRackMotor.set(0.95)
        else:
            self.stopLeftRack()


    def extendRight(self):
        atLimit = self.getRightLimit()
        if not atLimit:
            self.rightRackMotor.set(0.95)
        else:
            self.stopRightRack()


    def extendRear(self):
        atLimit = self.getRearLimit()
        if not atLimit:
            self.rearRackMotor.set(0.9)
        else:
            self.stopRearRack()


    def extendLeftEnc(self, diff):
        atLimit = self.getLeftLimit()
        if not atLimit:
            if diff <= -2000:
                self.leftRackMotor.set(0)

            elif diff < -500:
                speed = self.fPower * ((2000 + diff) / 2000)

                if speed < 0:
                    speed *= -1
                if speed > 1.0:
                    speed = 1.0

                self.leftRackMotor.set(speed)

            else:
                self.leftRackMotor.set(self.fPower)

        else:
            self.stopLeftRack()


    def extendRightEnc(self, diff):
        atLimit = self.getRightLimit()
        if not atLimit:
            if diff >= 2000:
                self.rightRackMotor.set(0)

            elif diff > 500:
                speed = self.fPower * ((2000 - diff) / 2000)

                if speed < 0:
                    speed *= -1
                if speed > 1.0:
                    speed = 1.0

                self.rightRackMotor.set(speed)

            else:
                self.rightRackMotor.set(self.fPower)

        else:
            self.stopRightRack()


    def extendRearEnc(self, diff):
        atLimit = self.getRearLimit()
        if not atLimit:
            if diff <= -2000:
                self.rearRackMotor.set(0)

            elif diff < -500:
                speed = self.rPower * ((2000 + diff) / 2000)

                if speed < 0:
                    speed *= -1
                if speed > 1.0:
                    speed = 1.0

                self.rearRackMotor.set(speed)

            else:
                self.rearRackMotor.set(self.rPower)

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
