from commands.drive.gotowallcommand import GoToWallCommand
import subsystems

class DriveToLiftCommand(GoToWallCommand):

    def isFinished(self):
        if not subsystems.gear.hasGear():
            return True

        return super().isFinished()
