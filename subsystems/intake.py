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
        self.intakeTable = NetworkTables.getTable('Intake')

        self.ballCount = 0
        self.table.putNumber('BallCount', self.ballCount)

        self.forward = False

        self.intaking = False

        self.intakeMotor.burnFlash()

    def intake(self, val=1):
        self.intakeMotor.set(val)
        self.intakeTable.putString('IntakeStatus', 'Intaking: ' + str(val))

    def outake(self):
        self.intakeMotor.set(-1.0)
        self.intakeTable.putString('IntakeStatus', 'Reversing')

    def stop(self):
        self.intakeMotor.stopMotor()
        self.intakeTable.putString('IntakeStatus', 'Halted')

    def monitorIntake(self): # Experimental
        # Gets output current, puts it in milliamperes. The free current (of a bag) at top speed is about 1.8 amps, will spike if more resistance (ball) - see motor chart.
        current = self.intakeMotor.getOutputCurrent()

        #print(current)

        if current * 1000 > 1800:
            self.ballCount += 1

    def slowIntake(self):
        self.intakeMotor.set(0.3)

    def slowOuttake(self):
        self.intakeMotor.set(-0.3)

    def intakeFreakOutNT(self):
        self.intakeTable.putString('Intakestatus', 'Freaking Out!')

    def fumbleForward(self):
        self.intakeMotor.set(1)

    def fumbleReverse(self):
        self.intakeMotor.set(-0.35)

    def changeFumble(self):
        if self.forward:
            self.fumbleReverse()
            self.forward = False
        else:
            self.fumbleForward()
            self.forward = True

        # lol rip intake motor

    def sensorCount(self):
        #print('hmm   ' + str(self.intakeSensor.get()))
        if not self.intakeSensor.get() and not self.intaking:
            self.ballCount += 1
            self.intaking = True
        elif self.intakeSensor.get():
            self.intaking = False
        self.table.putNumber('BallCount', self.ballCount)

