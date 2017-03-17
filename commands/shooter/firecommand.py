from wpilib.command import Command

import subsystems

class FireCommand(Command):
    # Initialize the named command.
    def __init__(self, shootingSpeed):
        super().__init__('ShootingCommand %s' % (shootingSpeed))

        self.requires(subsystems.shooter)
        self.requires(subsystems.feeder)

        self.shootingSpeed = shootingSpeed


    def initialize(self):
        subsystems.shooter.startShooting(self.shootingSpeed)
        subsystems.feeder.close()
        self.open = False


    def execute(self):
        if self.open:
            if not subsystems.shooter.isReadyToFire():
                self.open = False
                subsystems.feeder.close()
        else:
            if subsystems.shooter.isReadyToFire():
                self.open = True
                subsystems.feeder.open()


    def end(self):
        subsystems.shooter.stop()
        subsystems.feeder.close()
