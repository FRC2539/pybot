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
        subsystems.feeder.close()
        subsystems.shooter.startShooting(self.shootingSpeed)
        self.open = False
        self.stayOpen = 0


    def execute(self):
        if self.open and self.stayOpen < 3:
            if not subsystems.shooter.isReadyToFire():
                self.open = False
                subsystems.feeder.close()
                subsystems.feeder.stopAgitator()
                self.stayOpen += 1
        else:
            if subsystems.shooter.isReadyToFire():
                self.open = True
                subsystems.feeder.open()
                if self.stayOpen > 3:
                    subsystems.feeder.startAgitator()
            elif self.open:
                self.open = False
                self.stayOpen += 1


    def end(self):
        subsystems.feeder.close()
        subsystems.feeder.stopAgitator()
        subsystems.shooter.stop()
