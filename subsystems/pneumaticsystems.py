from .debuggablesubsystem import DebuggableSubsystem

import ports

import wpilib

class PneumaticSystems(DebuggableSubsystem):
    ''' Controls the pneumatic functions of the robot, including the color wheel and climber. '''

    def __init__(self):
        super().__init__('PneumaticSystems')
        self.compressor = wpilib.Compressor(ports.pneumaticSystem.pcmID) # Not much to implement.

        self.climberSolenoid = wpilib.DoubleSolenoid(ports.pneumaticSystem.pcmID, ports.pneumaticSystem.climberSolenoidForward, ports.pneumaticSystem.climberSolenoidReverse)
        self.colorWheelSolenoid = wpilib.DoubleSolenoid(ports.pneumaticSystem.pcmID, ports.pneumaticSystem.colorWheelSolenoidForward, ports.pneumaticSystem.colorWheelSolenoidReverse)

        self.disableCompressor()

    def enableCompressor(self):
        self.compressor.setClosedLoopControl(True) # Runs the compressor, use in pits.
        self.compressor.start()

    def isFull(self):
        return self.compressor.getPressureSwitchValue() # Returns true when full, false when low.

    def disableCompressor(self):
        self.compressor.setClosedLoopControl(False)

    def extendClimberPiston(self):
        self.climberSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)

    def extendColorWheelPiston(self):
        self.colorWheelSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)

    def retractClimberPiston(self):
        self.climberSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)

    def retractColorWheelPiston(self):
        self.colorWheelSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)

    def stopClimberPiston(self):
        self.climberSolenoid.set(wpilib.DoubleSolenoid.Value.kOff)

    def stopColorWheelPiston(self):
        self.colorWheelSolenoid.set(wpilib.DoubleSolenoid.Value.kOff)
    #def toggleClimberPiston(self):
        #if self.climberSolenoid.get():
            #self.climberSolenoid.set(False)
        #else:
            #self.climberSolenoid.set(True)

    #def toggleColorWheelPiston(self):
        #if self.colorWheelSolenoid.get():
            #self.colorWheelSolenoid.set(False)
        #else:
            #self.colorWheelSolenoid.set(True)
