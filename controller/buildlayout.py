from logitechdualshock import LogitechDualshock
from . import logicalaxes

class BuildLayout:
    def __init__(self, _id):
        self.controller = LogitechDualshock(_id)
        
        return self.controller
    
    def checkForAction(self):
        
