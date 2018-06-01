from wpilib.command import Command

import subsystems

class FireCommand(Command):

    def __init__(self, shootingSpeed, maxFuel=None):
        super().__init__('ShootingCommand %s' % (shootingSpeed))

        self.requires(subsystems.shooter)
        self.requires(subsystems.feeder)

        self.shootingSpeed = shootingSpeed
        self.maxFuel = maxFuel


    def initialize(self):
        subsystems.shooter.startShooting(11000)
        self.open = False
        self.ticksWithoutFuel = 0
        self.fuelLaunched = 0


    def execute(self):
        if self.open:
            if subsystems.shooter.isReadyToFire():
                subsystems.feeder.startAgitator()
                self.ticksWithoutFuel += 1

            else:
                self.open = False
                self.fuelLaunched += 1

        elif subsystems.shooter.isReadyToFire():
            self.open = True
            subsystems.feeder.open()
            self.ticksWithoutFuel = 0


    def isFinished(self):
        return self.maxFuel and self.maxFuel <= self.fuelLaunched


    def end(self):
        subsystems.feeder.close()
        subsystems.feeder.stopAgitator()
        subsystems.shooter.stop()
