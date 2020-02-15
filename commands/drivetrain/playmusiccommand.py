from wpilib.command import Command

import robot

class PlayMusicCommand(Command):

    def __init__(self):
        super().__init__('Play Music')

        self.requires(robot.drivetrain)


    def initialize(self):
        robot.drivetrain.neverPlayMusic()



    def execute(self):
        pass


    def end(self):
        robot.drivetrain.noStopMusicHere()
