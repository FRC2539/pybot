from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for pneumatics')

        self.requires(robot.ledsystem)
        self.requires(robot.pneumatics)

    def execute(self):
        if robot.pneumatics.isPressureLow():
            robot.ledsystem.setRed()

        elif robot.shooter.shooting and robot.pneumatics.isLowered() and robot.balllauncher.isMoving():
            robot.ledsystem.colorOneChase() # Should be shooting!

        elif robot.shooter.shooting or robot.pneumatics.isLowered() or robot.balllauncher.isMoving():
            robot.ledsystem.setWhite() # Something is not right!

        else:
            robot.ledsystem.rainbowLava() # All set!
