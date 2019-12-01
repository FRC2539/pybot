from wpilib.buttons.button import Button

class POVButton(Button):
    def __init__(self, controller, angle):
        self.validAngles = [angle, angle - 45, angle + 45]
        self.validAngles = [x % 360 for x in self.validAngles]
        
        self.controller = controller
        
    def get(self):
        return self.controller.getPOV() in self.validAngles
