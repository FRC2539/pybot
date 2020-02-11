from .debuggablesubsystem import DebuggableSubsystem

import ports

from rev import CANSparkMax, ControlType, MotorType

from networktables import NetworkTables as nt

class Shooter(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')

        self.motor = CANSparkMax(ports.shooter.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.controller = self.motor.getPIDController()

        self.secondMotor = CANSparkMax(ports.shooter.motorTwoID, MotorType.kBrushless)
        self.secondEncoder = self.motor.getEncoder()
        self.secondController = self.motor.getPIDController()

        self.table = nt.getTable('Shooter')

        self.ballCount = 5 #Config('
        #self.rpm = 6000 # Make NT value

        self.motor.setInverted(True)

        self.controller.setFF(0.000162, 0)
        self.controller.setP(0.0015, 0)
        self.controller.setI(0, 0)
        self.controller.setD(0, 0)
        self.controller.setIZone(0, 0)

        self.secondController.setFF(0.000162, 0)
        self.secondController.setP(0.0015, 0)
        self.secondController.setI(0, 0)
        self.secondController.setD(0, 0)
        self.secondController.setIZone(0, 0)

        self.secondMotor.follow(self.motor, True) # inverts it

        self.zeroNetworkTables()

    def runAtSpeed(self, percent):
        self.motor.set(percent)
        #self.secondMotor.set(percent)

    def shootBall(self):
        self.motor.set(0.6)
        #self.secondMotor.set(0.6)

    def stop(self):
        self.motor.stopMotor()
        #self.secondMotor.stopMotor()

    def monitorBalls(self):
        current = self.motor.getOutputCurrent()
        print(current)
        if current * 1000 > 1800:
            self.ballCount -= 1

    def updateNetworkTables(self):
        avgVel = round(((self.encoder.getVelocity() + self.secondEncoder.getVelocity()) / 2), 2)
        self.table.putNumber('ShooterRPM', avgVel)

    def setGoalNetworkTables(self, rpm=3500):
        self.table.putNumber('DesiredShooterRPM', rpm)

    def zeroNetworkTables(self):
        self.table.putNumber('ShooterRPM', 0.00)
        self.table.putNumber('DesiredShooterRPM', 0.00)

    def getRPM(self):
        return ((self.encoder.getVelocity() + self.secondEncoder.getVelocity()) / 2)

    def setRPM(self, rpm=3500):
        self.controller.setReference(float(3500), ControlType.kVelocity, 0, 0)
        #self.secondController.setReference(float(rpm), ControlType.kVelocity, 0, 0)
