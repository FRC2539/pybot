from .debuggablesubsystem import DebuggableSubsystem

import ports

import wpilib

class PneumaticSystems(DebuggableSubsystem):
    ''' Controls the pneumatic functions of the robot, including the color wheel and climber. '''

    def __init__(self):
        super().__init__('PneumaticSystems')
        self.compressor = wpilib.Compressor(ports.pneumaticSystem.pcmID) # Not much to implement.

        self.climberSolenoid = wpilib.Solenoid(ports.pneumaticSystem.pcmID, ports.pneumaticSystem.climberSolenoid)
        self.colorWheelSolenoid = wpilib.Solenoid(ports.pneumaticSystem.pcmID, ports.pneumaticSystem.colorWheelSolenoid)

    def enableCompressor(self):
        self.compressor.setClosedLoopControl(True) # Runs the compressor, use in pits.

    def isFull(self):
        return not self.compressor.getPressureSwitchValve() # Returns true when full, false when low.

    def disableCompressor(self):
        self.compressor.setClosedLoopControl(False)

    def extendClimberPiston(self):
        self.climberSolenoid.set(True)

    def extendColorWheelPiston(self):
        self.colorWheelSolenoid.set(True)

    def retractClimberPiston(self):
        self.climberSolenoid.set(False)

    def retractColorWheelPiston(self):
        self.colorWheelSolenoid.set(False)

    def toggleClimberPiston(self):
        if self.climberSolenoid.get():
            self.climberSolenoid.set(False)
        else:
            self.climberSolenoid.set(True)

    def toggleColorWheelPiston(self):
        if self.colorWheelSolenoid.get():
            self.colorWheelSolenoid.set(False)
        else:
            self.colorWheelSolenoid.set(True)
