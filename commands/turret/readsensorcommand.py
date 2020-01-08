from wpilib.command.command import Command

import robot

class ReadSensorCommand(Command):

    def __init__(self):
        super().__init__('Read Sensor')

        self.requires(robot.turret)

    def inititalize(self):
        robot.turret.initSensor()

    def execute(self):
        print(robot.turret.readSensor())
