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
        subsystems.shooter.setShooterSpeed(self.shootingSpeed)
        subsystems.shooter.startShooting()

    def execute(self):
        subsystems.shooter.getShooterSpeed()
        #if subsystems.shooter.getShooterSpeed() == self.shootingSpeed:
        #    subsystems.feeder.start()
        #else:
        #    subsystems.feeder.stop()

    #def isFinished(self):
    #    return subsystems.feeder.isEmpty()


    def end(self):
        subsystems.shooter.stop()
        subsystems.feeder.stop()
