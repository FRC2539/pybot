from wpilib.command import Command

import robot


class AimTurretDrivebaseCommand(Command):

    def __init__(self):
        super().__init__('Aim Turret Drivebase')

        self.requires(robot.drivetrain)
        self.requires(robot.turret)


    def initialize(self):
        robot.limelight.setPipeline(1)


    def execute(self):
        #print("aiming")
        if (robot.turret.isZeroed() or robot.turret.isMax()):
            self.UseDriveTrain = True
        else:
            self.UseDriveTrain = False

        self.rotate = robot.limelight.getX() * .035
        if (abs(self.rotate) > .3):
            self.rotate = math.copysign(.3, self.rotate)

        if self.UseDriveTrain:
            robot.drivetrain.move(0,0,self.rotate)
        else:
            robot.turret.move(self.rotate)


    def end(self):
        robot.limelight.setPipeline(0)
        robot.drivetrain.stop()
        robot.turret.stop()
