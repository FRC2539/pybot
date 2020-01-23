from .debuggablesubsystem import DebuggableSubsystem
from rev import CANSparkMax, MotorType, ControlType
from wpilib import DigitalInput

from custom.config import Config
from networktables import NetworkTables

import ports
import robot

class Elevator(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Elevator')

        NetworkTables.initialize(server='10.25.39.2')
        self.Elevator = NetworkTables.getTable('Elevator')

        self.motor = CANSparkMax(ports.elevator.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.PIDController = self.motor.getPIDController()
        self.FFk = Config('/Elevator/FFk', 0)
        self.Pk = Config('/Elevator/Pk', .045)
        self.Ik = Config('/Elevator/Ik', 0)
        self.Dk = Config('/Elevator/Dk', 1)
        self.IZk = Config('/Elevator/IZk', 0)

        print ('pk' + str(self.Pk.getValue()))

        
        for slot in range(2):
            self.PIDController.setFF(self.FFk.getValue(), slot) # was .5
            self.PIDController.setP(self.Pk.getValue(), slot)
            self.PIDController.setI(self.Ik.getValue(), slot)# was .001
            self.PIDController.setD(self.Dk.getValue(), slot)# was 20
            self.PIDController.setIZone(self.IZk.getValue(), slot)# was 3

        self.motor.setOpenLoopRampRate(0.6)
        self.motor.setClosedLoopRampRate(0.6)


        self.lowerLimit = DigitalInput(ports.elevator.lowerLimit)

        self.upperLimit = 145.0

        self.encoder.setPositionConversionFactor(1)

        #These are temporary and need to be finalized for competition. Make sure they are in inches!!! 
        self.levels = {
                        'floor' : 0.0,
                        'aboveFloor' : 10.0,
                        'lowHatches' : 0.0,
                        'midHatches' : 41.0,
                        'highHatches' : 69.0,
                        'cargoBalls' : 50.0,
                        'lowBalls' : 0.0,
                        'midBalls' : 44.0,
                        'highBalls' : 72.0,
                        'start' : 0.0
                        }


    def up(self):
        isTop = self.getPosition() >= self.upperLimit

        if isTop:
            self.setPosition(float(self.upperLimit))
            self.stop()
        else:
            self.set(1.0)

        return isTop


    def down(self):
        isZero = self.isAtZero()

        if isZero:
            self.stop()
            self.resetEncoder()

        else:
            self.set(-1.0)

        return isZero

    def stop(self):
        self.motor.set(0.0)


    def hold(self):
        self.setPosition(self.getPosition())


    def set(self, speed):
        self.motor.set(speed)


    def resetEncoder(self):
        self.encoder.setPosition(0.0)
        self.PIDController.setReference(0.0, ControlType.kPosition, 0, 0)

    def zeroEncoder(self):
        self.motor.setEncPosition(0)

    def inchesToRotations(self, value):
        return (value / (2*2.638 * 3.14159)) * 50
        # 2.638" is the distance in inches in which the chain moves from one rotation. Gear ratio is 50:1.

    def setPosition(self, target):
        rotations = self.inchesToRotations(target)
        self.PIDController.setReference(float(rotations), ControlType.kPosition, 0, 0)
        
        
    def getPosition(self):
        return self.encoder.getPosition()


    def isAtZero(self):
        return (self.getPosition() <= 0.0) or (not self.lowerLimit.get())


    def goToLevel(self, level):
        print('going to level')
        return self.encoder.setPosition(float(self.levels[level]))
    
    
    def increaseHeight(self, value): # Give value in inches!
        rotations = self.inchesToRotations(value)
        self.PIDController.setReference(self.getPosition() + rotations, ControlType.kPosition, 1, 0)
        
        
    def decreaseHeight(self, value): # Give value in inches!
        rotations = self.inchesToRotations(value)
        self.PIDController.setReference(self.getPosition() - rotations, ControlType.kPosition, 1, 0)
        

    def goToFloor(self):
        self.goToLevel('floor')

    def isMid(self):
        self.position = self.encoder.getPosition()
        self.dif0 = self.position - 0
        self.dif1 = self.position - 41
        self.dif2 = self.position - 69

        if self.dif0 < self.dif1 :
            if  self.dif0 < self.dif2:
                return False
        elif self.dif1 < self.dif0:
            if self.dif1 < self.dif2:
                return True
        elif self.dif2 < self.dif0:
            if self.dif2 < self.dif1:
                return False
        else:
            return False

    def isHigh(self):
        self.position = self.encoder.getPosition()
        self.dif0 = self.position - 0
        self.dif1 = self.position - 41
        self.dif2 = self.position - 69

        if self.dif0 < self.dif1 :
            if  self.dif0 < self.dif2:
                return False
        elif self.dif1 < self.dif0:
            if self.dif1 < self.dif2:
                return False
        elif self.dif2 < self.dif0:
            if self.dif2 < self.dif1:
                return True
        else:
            return False

    def isLow(self):
        self.position = self.encoder.getPosition()
        self.dif0 = self.position - 0
        self.dif1 = self.position - 41
        self.dif2 = self.position - 69

        if self.dif0 < self.dif1 :
            if  self.dif0 < self.dif2:
                return True
        elif self.dif1 < self.dif0:
            if self.dif1 < self.dif2:
                return False
        elif self.dif2 < self.dif0:
            if self.dif2 < self.dif1:
                return False
        else:
            return False



    #def panelEject(self):
        #if not (self.getPosition() < 0.1):
            #self.setPosition(float(self.getPosition()) - 0.1)
