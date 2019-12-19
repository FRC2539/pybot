from ctre import NeutralMode

class Cargo:
    cargo_motor: object

    def prepareCargoIntake(self):
        self.cargo_motor.setNeutralMode(NeutralMode.Brake)
        self.cargo_motor.setSafetyEnabled(False)

    def intakeBall(self):
        self.cargo_motor.set(0.6)

    def outakeBall(self):
        self.cargo_motor.set(-0.8)

    def stop(self):
        self.cargo_motor.set(0)

    def slowCargoOutake(self):
        self.cargo_motor.set(-0.5)

    def holdCargo(self):
        self.cargo_motor.set(0.2)

    def execute(self):
        pass
