from .debuggablesubsystem import DebuggableSubsystem
from rev import CANSparkMax, MotorType, ControlType, ConfigParameter
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
        
        for slot in range(2):
            self.PIDController.setFF(0.5, slot)
            self.PIDController.setP(0.1, slot)
            self.PIDController.setI(0.001, slot)
            self.PIDController.setD(20, slot)
            self.PIDController.setIZone(3, slot)

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
            self.setPosition(float(self.upperLimit), 'down')
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
        return (value / 2.638) * 50
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
        self.PIDController.setReference(self.getPosition() + rotations, ControlType.kPosition, 0, 0)
        
        
    def decreaseHeight(self, value): # Give value in inches!
        rotations = self.inchesToRotations(value)
        self.PIDController.setReference(self.getPosition() - rotations, ControlType.kPosition, 0, 0)
        

    def goToFloor(self):
        self.goToLevel('floor')


    #def panelEject(self):
        #if not (self.getPosition() < 0.1):
            #self.setPosition(float(self.getPosition()) - 0.1)
