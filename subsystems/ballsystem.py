from .debuggablesubsystem import *

from networktables import NetworkTables

from wpilib import DigitalInput

from ctre import ControlMode, WPI_TalonSRX, NeutralMode

import ports


class BallSystem(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('BallSystem')
        self.lowerConveyorMotor = WPI_TalonSRX(ports.ballsystem.lowerConveyor)
        self.verticalConveyorMotor = WPI_TalonSRX(ports.ballsystem.verticalConveyor)

        self.lowerConveyorMotor.setNeutralMode(NeutralMode.Brake)
        self.verticalConveyorMotor.setNeutralMode(NeutralMode.Brake)

        self.shooting = False

        self.table = NetworkTables.getTable('BallSystem')

        self.shooterSensor = DigitalInput(ports.ballsystem.shooterSensor)
        self.queueingSensor = DigitalInput(ports.ballsystem.queueingSensor)

    def slowVerticalReverse(self):
        self.verticalConveyorMotor.set(-0.05)

    def runVerticalSlow(self):
        self.verticalConveyorMotor.set(0.4)

    def reverseVerticalSlow(self):
        self.verticalConveyorMotor.set(-0.4)

    def runLowerConveyor(self):
        self.lowerConveyorMotor.set(ControlMode.PercentOutput, 1)
        self.table.putString('LowerConveyorStatus', 'Forward')

    def runLowerConveyorSlow(self):
        self.lowerConveyorMotor.set(ControlMode.PercentOutput, 0.4) # experiment
        self.table.putString('LowerConveyorStatus', 'Slow')

    def reverseLowerConveyorSlow(self):
        self.lowerConveyorMotor.set(ControlMode.PercentOutput, -0.4) # experiment
        self.table.putString('LowerConveyorStatus', 'Reverse Slow')

    def runVerticalConveyor(self):
        self.verticalConveyorMotor.set(ControlMode.PercentOutput, 1)
        self.table.putString('UpperConveyorStatus', 'Forward')

    def reverseLowerConveyor(self):
        self.lowerConveyorMotor.set(ControlMode.PercentOutput, -1)
        self.table.putString('LowerConveyorStatus', 'Reversing')

    def reverseVerticalConveyor(self):
        self.verticalConveyorMotor.set(ControlMode.PercentOutput, -1)
        self.table.putString('UpperConveyorStatus', 'Reversing')

    def safeRunLower(self):
        self.lowerConveyorMotor.set(ControlMode.PercentOutput, 0.8)

    def safeRunVertical(self):
        self.verticalConveyorMotor.set(ControlMode.PercentOutput, 1)

    def safeRunAll(self):
        self.safeRunVertical()
        self.safeRunLower()

    def stopLowerConveyor(self):
        self.lowerConveyorMotor.stopMotor()

    def stopVerticalConveyor(self):
        self.verticalConveyorMotor.stopMotor()

    def runAll(self):
        #print("running all")
        self.runLowerConveyor()
        self.runVerticalConveyor()

    def runLowSlowAndVertical(self): # lol that rhymes
        self.lowerConveyorMotor.set(0.1)
        self.runVerticalConveyor()

    def runAllSlow(self):
        self.lowerConveyorMotor.set(0.69) # Nice
        self.verticalConveyorMotor.set(0.69)

    def reverseAll(self):
        self.reverseLowerConveyor()
        self.reverseVerticalConveyor()

    def stopAll(self):
        self.stopLowerConveyor()
        self.stopVerticalConveyor()

    def setHorizontalBrake(self):
        self.lowerConveyorMotor.setNeutralMode(NeutralMode.Brake)

    def setHorizontalCoast(self):
        self.lowerConveyorMotor.setNeutralMode(NeutralMode.Coast)

    #def enableSensor(self):
        #self.horizontalBeltSensor.setEnabled(True)

    #def disableSensor(self):
        #self.horizontalBeltSensor.setEnabled(False)

    def updateNetworktables(self):
        self.table.putNumber('BallInChamber', (not self.queueingSensor.get()))

    def isLowBallPrimed(self):
        self.updateNetworktables()
        return not self.queueingSensor.get() # may need to invert

    def needsToQueue(self):
        return not (self.queueingSensor.get())

    def isUpperBallPrimed(self):
        self.updateNetworktables()
        return not self.shooterSensor.get()

    def areTwoBallsPrimed(self):
        self.updateNetworktables()
        return (not self.queueingSensor.get()) and (not self.shooterSensor.get())

    def monitorBalls(self, startCount):

        #print("monitoring")
        if not self.shooterSensor.get() and not self.shooting: # is there something there that was not there last time?
            if startCount != 0:
                startCount -= 1
                self.table.putNumber('BallCount', self.ballCount)
            self.shooting = True
        elif self.shooterSensor.get(): # no ball present
            self.shooting = False # nothing there, spaced out.

        return startCount
