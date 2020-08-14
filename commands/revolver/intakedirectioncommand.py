from wpilib.command import Command

import robot

class IntakeDirectionCommand(Command):

    def __init__(self):
        super().__init__('Intake Direction')

        self.requires(robot.revolver)

    def initialize(self):
        robot.revolver.setVariableSpeed(-0.25)


#    def isFinished(self):

        #revPos = robot.revolver.getPosition()
        #if revPos >= 283 and revPos <= 285:
            #print("idc locked rev pos: " + str(robot.revolver.getPosition()))
            #return True
        #else:
            #print("idc rev pos: " + str(robot.revolver.getPosition()))

    def end(self):
        robot.revolver.stopRevolver()
