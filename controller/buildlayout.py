from .logitechdualshock import LogitechDualshock
from . import logicalaxes

class BuildLayout:
    def __init__(self, _id):
        self.controller = LogitechDualshock(_id)

        logicalaxes.driveX = self.controller.LeftX
        logicalaxes.driveY = self.controller.LeftY
        logicalaxes.driveRotate = self.controller.RightX

    def returnObj(self):
        return self.controller
          
    
