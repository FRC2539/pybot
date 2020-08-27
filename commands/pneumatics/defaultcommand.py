from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for pneumatics')

        self.requires(robot.ledsystem)
        self.requires(robot.pneumatics)

        self.modifierOne = False

    def execute(self):

        print(robot.revolver.getPosition())

        if robot.pneumatics.isPressureLow() and not robot.shooter.shooting: # Run the compressor if we don't need the current.

            robot.pneumatics.enableCLC()
            robot.pneumatics.startCompressor()

            robot.ledsystem.setRed() # Compressor is running

        elif robot.pneumatics.isPressureLow() and robot.shooter.shooting and \
            robot.pneumatics.isCompressorRunning():  # Third condition allows us to not repeat here.

            robot.pneumatics.disableCLC()
            robot.pneumatics.stopCompressor()

            self.modifierOne = True

        elif robot.shooter.shooting and robot.pneumatics.isLowered() and \
            robot.balllauncher.isMoving() and robot.revolver.isRevolving():

            if self.modifierOne:
                robot.ledsystem.colorOneHeartbeat() # Alerts that the compressor is low as well, and was halted.
            else:
                robot.ledsystem.colorOneChase() # Should be shooting!

        elif robot.shooter.shooting or robot.pneumatics.isLowered() or \
            robot.balllauncher.isMoving() or robot.revolver.isRevolving():

            if self.modifierOne:
                robot.ledsystem.whiteHeartbeat() # Alerts that the compressor is low as well, and was halted.
            else:
                robot.ledsystem.setWhite() # Something is not right!

        else:
            robot.ledsystem.rainbowLava() # All set!

        if not robot.pneumatics.isPressureLow():
            self.modifierOne = False

        else:
            self.modifierOne = True
