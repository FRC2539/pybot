from wpilib.command.command import Command
from subsystems.sparkmaxtemporary import SparkMaxTemporary
import robot
import subsystems

class SparkMaxTestCommand(Command):

    def __init__(self):
        super().__init__('Spark Max Test')

        self.requires(robot.sparkmaxtemporary)


    def initialize(self):
        robot.sparkmaxtemporary.set(1)


    def execute(self):
        enc1, enc2 = robot.sparkmaxtemporary.get()
        print(str(enc1) + '     ' + str(enc2))

    def end(self):
        robot.sparkmaxtemporary.stop()
