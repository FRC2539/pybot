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

        self.fPower = 1.0
        self.rPower = 0.7

        self.resetEncoders()

    def getLeftPos(self):
        return self.leftRackMotor.getSelectedSensorPosition(0)


    def getRightPos(self):
        return self.rightRackMotor.getSelectedSensorPosition(0)


    def getRearPos(self):
        return self.rearRackMotor.getSelectedSensorPosition(0)


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


    def popAll(self):
        self.popRight()
        self.popLeft()
        self.popRear()
        return self.getRightLimit() and self.getLeftLimit() and self.getRearLimit()


    def startRaise(self):
        self.extendRear()
        self.extendLeft()
        self.extendRight()

    def extendAllEnc(self):
        if self.rearRackMotor.getSelectedSensorPosition(0) - self.leftRackMotor.getSelectedSensorPosition(0) > 200 or \
            self.rearRackMotor.getSelectedSensorPosition(0) - self.rightRackMotor.getSelectedSensorPosition(0) > 200:
            self.stopRearRack()

        else:
            self.extendLeft()
            self.extendRight()

        if self.leftRackMotor.getSelectedSensorPosition(0) - self.rearRackMotor.getSelectedSensorPosition(0) > 200:
            self.stopLeftRack()

        else:
            self.extendRear()
            self.extendRight()

        if self.rightRackMotor.getSelectedSensorPosition(0) - self.rearRackMotor.getSelectedSensorPosition(0) > 200:
            self.stopRightRack()

        else:
            self.extendLeft()
            self.extendRear()

        #frontAvg = round((self.rightRackMotor.getSelectedSensorPosition(0) + self.leftRackMotor.getSelectedSensorPosition(0)) / 2)
        ##frontAvg = round(self.rightRackMotor.getSelectedSensorPosition(0))
        #frontDiff = self.rightRackMotor.getSelectedSensorPosition(0) - self.leftRackMotor.getSelectedSensorPosition(0)
        #diff = frontAvg - self.rearRackMotor.getSelectedSensorPosition(0)

        #print("LEFTRACK: "+str(self.leftRackMotor.getSelectedSensorPosition(0)))
        #print("rightRack: "+str(self.rightRackMotor.getSelectedSensorPosition(0)))
        #print('REAR RACK: ' + str(self.rearRackMotor.getSelectedSensorPosition(0)))
        #print("frontAvg: "+str(frontAvg))
        #print("frontDiff: "+str(frontDiff))
        #print("DIFF: "+str(diff))

        ##ORIGINAL COPY
        #self.extendRightEnc(frontDiff - diff)
        #self.extendLeftEnc(frontDiff - diff)
        #self.extendRearEnc(diff)

        return self.getRightLimit() and self.getLeftLimit() and self.getRearLimit()


    def extendLeft(self):
        atLimit = self.getLeftLimit()
        if not atLimit:
            self.leftRackMotor.set(0.8)
        else:
            self.stopLeftRack()


    def extendRight(self):
        atLimit = self.getRightLimit()
        if not atLimit:
            self.rightRackMotor.set(0.8)
        else:
            self.stopRightRack()


    def popLeft(self):
        atLimit = self.getLeftLimit()
        if not atLimit:
            self.leftRackMotor.set(1)
        else:
            self.stopLeftRack()

        print('left pos ' + str(self.leftRackMotor.getSelectedSensorPosition(0)))

        return atLimit

    def popRight(self):
        atLimit = self.getRightLimit()
        if not atLimit:
            self.rightRackMotor.set(1)
        else:
            self.stopRightRack()

        print('right pos ' + str(self.rightRackMotor.getSelectedSensorPosition(0)))

        return atLimit

    def popRear(self):
        atLimit = self.getRearLimit()
        if not atLimit:
            self.rearRackMotor.set(0.8)
        else:
            self.stopRearRack()

        print('rear pos ' + str(self.rearRackMotor.getSelectedSensorPosition(0)))

        return atLimit

    def checkLeft(self, stopPos):
        atLimit = self.getLeftLimit()
        if not atLimit:
            pos = self.leftRackMotor.getSelectedSensorPosition(0)
            if pos >= stopPos:
                return False
            else:
                print('NEED TO RUN LEFT')
                return True


    def checkRight(self, stopPos):
        atLimit = self.getRightLimit()
        if not atLimit:
            pos = self.rightRackMotor.getSelectedSensorPosition(0)
            if pos >= stopPos:
                return False
            else:
                return True


    def checkRear(self, stopPos):
        atLimit = self.getRearLimit()
        if not atLimit:
            pos = self.rearRackMotor.getSelectedSensorPosition(0)
            if pos >= stopPos:
                return False
            else:
                return True

    def extendRear(self):
        atLimit = self.getRearLimit()
        if not atLimit:
            self.rearRackMotor.set(0.85)
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


    def creepBackward(self):
        self.driveMotor.set(-0.3)


    def driveBackward(self):
        self.driveMotor.set(-0.8)
