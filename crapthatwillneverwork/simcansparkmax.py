from rev import CANSparkMax # Base off of the original CANSparkMax, rewrite what needs written.

import rev

#from hal import *

class SimCANSparkMax(CANSparkMax):

    def __init__(self, devID, motorType):

        super().__init__(devID, motorType)

        self.mySimDevice = SimDevice('BenCANSparkMax', devID)

        self.devID = devID
        self.motorType = motorType

        self.simIsInverted = self.mySimDevice.createBoolean('Inverted', False, False)
        self.simVoltageCompensationEnabled = self.mySimDevice.createBoolean('Voltage Compensation Enabled', False, False)
        self.simSoftLimitFwdEnabled = self.mySimDevice.createBoolean('Fwd Soft Limit Enabled', False, False)
        self.simSoftLimitRevEnabled = self.mySimDevice.createBoolean('Rev Soft Limit Enabled', False, False)

        self.simOpenLoopRampRate = self.mySimDevice.createDouble('Open Loop Ramp Rate', True, 1.0)
        self.simClosedLoopRampRate = self.mySimDevice.createDouble('Closed Loop Ramp Rate', True, 1.0)
        self.simSoftLimitFwd = self.mySimDevice.createDouble('Fwd Soft Limit', False, 0.0)
        self.simSoftLimitRev = self.mySimDevice.createDouble('Rev Soft Limit', False, 0.0)
        self.simSpeed = self.mySimDevice.createDouble('Speed', True, 0.0)

        self.simIdleMode = self.mySimDevice.createEnum('Idle Mode', False, ['Coast', 'Brake'], 0)
        self.simMotorType = self.mySimDevice.createEnum('Motor Type', True, ['Brushed', 'Brushless'], motorType)

    def setInverted(self, isInverted):
        if self.mySimDevice != None:
            self.simIsInverted.set(isInverted)
        else:
            super().setInverted(isInverted)

    def set(self, percent):
        if self.mySimDevice != None:
            self.simSpeed.set(percent)
        else:
            super().set(percent)

    def stopMotor(self):
        super().stopMotor()
        self.set(0.0)
