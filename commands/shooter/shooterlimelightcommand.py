from wpilib.command import Command

from wpilib import Timer

import robot

class ShooterLimelightCommand(Command):

    def __init__(self):
        super().__init__('Shooter Limelight')

        self.requires(robot.shooter)
        self.close = False

        self.timer = Timer()

    def initialize(self):
        robot.limelight.setPipeline(1)
        robot.ledsystem.flashRed()

        #robot.shooter.setRPM(4200)
        #robot.shooter.setGoalNetworkTables(4200)

        self.timer.start()
        self.secondCounter = 0

        #if robot.limelight.getA() < 1.289:
            #robot.shooter.setRPM(4200)
            #self.close = False

        #else:
            #self.close = True
            #robot.shooter.setRPM(2500)

    def execute(self):

        self.speed = 5000 - 850 * robot.limelight.getA()
        if self.speed > 4900:
            self.speed = 4900
        if self.timer.hasElapsed(self.secondCounter):
            robot.shooter.updateNetworkTables(robot.shooter.getRPM())
            self.secondCounter += 1.5
            robot.shooter.setGoalNetworkTables(self.speed)


        robot.shooter.setRPM(self.speed)
        #if robot.limelight.getA() < 1.289:
            #robot.shooter.setRPM(4200)
            ##self.close = False

        #elif robot.limelight.getA() < .75:
            #robot.shooter.setRPM(4600)

        #else:
            ##self.close = True
            #robot.shooter.setRPM(3000)





        #if not self.close:
            #if robot.shooter.getRPM() >= 3900 and robot.ledsystem.onTarget:
                #robot.ledsystem.setGold()

            #elif robot.shooter.getRPM() >= 3900 and not robot.ledsystem.onTarget:
                #robot.ledsystem.setRed()

            #else:
                #robot.ledsystem.flashRed()
        #else:
            #if robot.shooter.getRPM() >= 2900 and robot.ledsystem.onTarget:
                #robot.ledsystem.setGold()

            #elif robot.shooter.getRPM() >= 2900 and not robot.ledsystem.onTarget:
                #robot.ledsystem.setRed()

            #else:
                #robot.ledsystem.flashRed()

    def end(self):
        robot.ledsystem.turnOff()
        robot.limelight.setPipeline(0)
        robot.shooter.stop()

        self.timer.stop()
        self.timer.reset()

        robot.shooter.zeroNetworkTables()
