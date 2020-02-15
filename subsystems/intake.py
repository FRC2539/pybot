import ports

from .debuggablesubsystem import DebuggableSubsystem

from networktables import NetworkTables

from wpilib import DigitalInput

from rev import CANSparkMax, MotorType

class Intake(DebuggableSubsystem):
    def __init__(self):
        super().__init__('Intake')

        self.intakeMotor = CANSparkMax(ports.IntakePorts.motorID, MotorType.kBrushless)

        self.intakeMotor.setInverted(True)

        self.intakeSensor = DigitalInput(ports.IntakePorts.sensorID)

        self.table = NetworkTables.getTable('Shooter')

        self.ballCount = 0
        self.table.putNumber('BallCount', self.ballCount)

        self.forward = False

        self.intaking = False

    def intake(self, val=1):
        self.intakeMotor.set(val)

    def outake(self):
        self.intakeMotor.set(-1.0)

    def stop(self):
        self.intakeMotor.stopMotor()

    def monitorIntake(self): # Experimental
        # Gets output current, puts it in milliamperes. The free current (of a bag) at top speed is about 1.8 amps, will spike if more resistance (ball) - see motor chart.
        current = self.intakeMotor.getOutputCurrent()
        print(current)
        if current * 1000 > 1800:
            self.ballCount += 1

    def fumbleForward(self):
        self.intakeMotor.set(1)

    def fumbleReverse(self):
        self.intakeMotor.set(-0.3)

    def changeFumble(self):
        if self.forward:
            self.fumbleReverse()
        else:
            self.fumbleForward()

        self.forward = not self.forward

        # lol rip intake motor

    def sensorCount(self):
        print('hmm   ' + str(self.intakeSensor.get()))
        if not self.intakeSensor.get() and not self.intaking:
            self.ballCount += 1
            self.intaking = True
        elif self.intakeSensor.get():
            self.intaking = False
        self.table.putNumber('BallCount', self.ballCount)

