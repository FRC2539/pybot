from wpilib.command import Command

import robot

class RunUntilLoadedCommand(Command):

    def __init__(self):
        super().__init__('Run Until Loaded')

        self.requires(robot.ballsystem)
        self.requires(robot.intake)

    def initialize(self):
        robot.intake.intake(0.95)
        if not robot.ballsystem.isBallPrimed():
            robot.ballsystem.setHorizontalCoast()
            robot.ballsystem.runLowerConveyorSlow()

    def execute(self):
        print('hmmm ' + str(robot.ballsystem.isBallPrimed()))
        print(robot.ballsystem.isBallPrimed())

        if robot.ballsystem.isBallPrimed():
            robot.ballsystem.stopLowerConveyor()
        else:
            robot.ballsystem.runLowerConveyorSlow()

    def end(self):
        robot.intake.stop()
        robot.ballsystem.stopLowerConveyor()
        robot.ballsystem.setHorizontalBrake()
