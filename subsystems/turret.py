from .debuggablesubsystem import DebuggableSubsystem

import wpilib

import ports
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
        self.max = 110
        self.min = -110

        self.motor.configSelectedFeedbackSensor(FeedbackDevice.PulseWidthEncodedPosition)

    def move(self, speed):
        #print(str(self.motor.getSelectedSensorPosition(0)))
        #if(self.motor.getSelectedSensorPosition(0)>self.max and self.motor.getSelectedSensorPosition(0)<self.min):
            #self.motor.set(ControlMode.PercentOutput, speed)
        #else:
            #print('hit turret limit')
            #self.motor.stopMotor()
        self.motor.set(ControlMode.PercentOutput, speed)

    def stop(self):
        self.motor.stopMotor()

    def returnZero(self):
        self.motor.set(ControlMode.Position, 0)

    def setPosition(self, position):
        if (position > self.min and position < self.max):
            self.motor.set(ControlMode.Position, position)
        else:
            print('param past turret max')
            self.motor.stopMotor()

    def initDefaultCommand(self):
        '''
        By default, unless another command is running that requires this
        subsystem, we will drive via joystick using the max speed stored in
        Config.
        '''
        from commands.turret.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())


