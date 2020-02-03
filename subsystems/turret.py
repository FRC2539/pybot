from .debuggablesubsystem import DebuggableSubsystem

import ports
import wpilib

from ctre import ControlMode, FeedbackDevice, WPI_TalonSRX

class Turret(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Turret')
        self.motor = WPI_TalonSRX(ports.turret.motorID)
        self.motor.config_kP(0, .0001, 0)
        self.motor.config_kI(0, 0, 0)
        self.motor.config_kD(0, .001, 0)
        self.motor.config_kF(0, .00019, 0)
        self.motor.config_IntegralZone(0, 0, 0)

        self.motor.configSelectedFeedbackSensor(FeedbackDevice.PulseWidthEncodedPosition)
        #self.encoder = wpilib.DutyCycleEncoder(1)

    def move(self, speed):
        self.motor.set(ControlMode.PercentOutput, speed)

    def stop(self):
        self.motor.stopMotor()

    def getAbsoluteReading(self):
        print('\n reading: ' + str(self.motor.getSelectedSensorPosition()) + '\n\n')

    def setAbsoluteReading(self, val):
        print('\n\n' + str(self.motor.setSelectedSensorPosition(val, 0, 0)) + '\n\n')


    def setPosition(self, position):
        self.motor.set(ControlMode.Position, position)


    def initDefaultCommand(self):
        from commands.turret.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
