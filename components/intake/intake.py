import wpilib

class Intake:

    intakeMotor: object

    def setup(self):
        self.intakeMotor.setInverted(False) # dummy value

    def intake(self):
        self.intakeMotor.set(1.0)

    def outake(self): # For some weird reason
        self.intakeMotor.set(-0.7)

    def maintainBalls(self):
        self.intakeMotor.set(0.4)

    def stop(self):
        self.intakeMotor.stopMotor()

    def execute(self):
        pass # might make the maintainBalls method
