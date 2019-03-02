from wpilib.command.command import Command
import time
import robot

class IntakeCommand(Command):

    def __init__(self):
        super().__init__('Intake')

        self.requires(robot.intake)
        self._finished = False
        self.cargoCount = 0
        self.hasCargo = False


    def initialize(self):
        '''
        self.hasCargo = robot.intake.hasCargo()

        if self.hasCargo:
            robot.lights.solidGreen()
        else:
            robot.lights.solidWhite()
        '''
        robot.lights.solidGreen()
        robot.intake.intake()


    def execute(self):
        pass
        '''
        self.hasCargo = not robot.intake.hasCargo()

        if self.cargoCount >= 3 and self.hasCargo:
            self.cargoCount = 0
            self._finished = True
        elif self.hasCargo:
            self.cargoCount += 1
        else:
            self.cargoCount = 0



    def isFinished(self):
        return self._finished
        '''

    def end(self):
        '''
        self.cargoCount = 0
        self._finished = False
        if self.hasCargo:
            robot.lights.solidGreen()
        else:
            robot.lights.off()
        '''
        robot.lights.off()

        time.sleep(0.25)

        robot.intake.stop()
