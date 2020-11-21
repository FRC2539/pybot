from .cougarsystem import *

from wpilib.command import Subsystem

from wpilib import Compressor, DoubleSolenoid, Watchdog, AnalogInput

from networktables import NetworkTables as nt

import ports

class Pneumatics(CougarSystem):
    '''Controls all pneumatic functions on the robot. Reference these in commands for other systems, as there are no general pneumatic commands.'''

    def __init__(self):
        super().__init__('Pheumatics')
        
        disablePrints()
        
        self.table = nt.getTable('Pneumatics')

        self.pneumaticCompressor = Compressor(ports.pneumatics.PCM)

        self.pneumaticCompressor.setClosedLoopControl(False) # Enables and ensures automatic compressor activity.

        self.ballLauncherSolenoid = DoubleSolenoid(ports.pneumatics.PCM, 0, 1) # Forward (0), extends it.
        self.intakeSolenoid = DoubleSolenoid(ports.pneumatics.PCM, 2, 3)
                
        self.pressureSensor = AnalogInput(ports.pneumatics.pressureSensor)

        self.maxPressure = 120 # It will only go to 110 if you use the RIGHT method.
        self.supplyVolt = 4.942

        disablePrints()

    def isPressureLow(self):
        return not self.isReasonable()#self.pneumaticCompressor.getPressureSwitchValue()

    def isCompressorRunning(self):
        return self.pneumaticCompressor.enabled()
    
    def extendIntakeSolenoid(self):
        self.intakeSolenoid.set(DoubleSolenoid.Value.kForward)
        
    def retractIntakeSolenoid(self):
        self.intakeSolenoid.set(DoubleSolenoid.Value.kReverse)

    def isIntakeLowered(self):
        return not (self.intakeSolenoid.get() == DoubleSolenoid.Value.kForward)

    def extendBallLauncherSolenoid(self):
        self.ballLauncherSolenoid.set(DoubleSolenoid.Value.kForward)

    def retractBallLauncherSolenoid(self):
        self.ballLauncherSolenoid.set(DoubleSolenoid.Value.kReverse)

    def isLowered(self):
        return (self.ballLauncherSolenoid.get() == DoubleSolenoid.Value.kForward)

    def enableCLC(self):
        self.pneumaticCompressor.setClosedLoopControl(True)

    def disableCLC(self):
        self.pneumaticCompressor.setClosedLoopControl(False)

    def startCompressor(self):
        self.pneumaticCompressor.start()

    def stopCompressor(self):
        self.pneumaticCompressor.stop()

    def getAnalogPressureSensor(self):
        return 250 * (self.pressureSensor.getVoltage() / self.supplyVolt) - 25
    
    def isReasonable(self):
        return int(self.getAnalogPressureSensor()) >= self.maxPressure - 30
    
    def isFull(self):
        return int(self.getAnalogPressureSensor()) >= self.maxPressure - 15
    
    def updatePressure(self):
        self.table.putNumber('Pressure', int(self.getAnalogPressureSensor()))

    def initDefaultCommand(self):
        from commands.pneumatics.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
