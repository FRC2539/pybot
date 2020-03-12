from wpilib.command import Command

import robot

class ShooterLimelightCommand(Command):

    def __init__(self):
        super().__init__('Shooter Limelight')

        self.requires(robot.shooter)
        self.close = False

    def initialize(self):
        robot.limelight.setPipeline(1)
        robot.ledsystem.flashRed()


        robot.shooter.setRPM(4200)


        #if robot.limelight.getA() < 1.289:
            #robot.shooter.setRPM(4200)
            #self.close = False

        #else:
            #self.close = True
            #robot.shooter.setRPM(2500)

    def execute(self):


        robot.shooter.setRPM(4200)


        #if robot.limelight.getA() < 1.289:
            #robot.shooter.setRPM(4200)
            #self.close = False

        #elif robot.limelight.getA() < .75:
            #robot.shooter.setRPM(4600)

        #else:
            #self.close = True
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
