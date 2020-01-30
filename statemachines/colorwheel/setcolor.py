from magicbot import StateMachine, state

from components.colorsensor.colorwheel import ColorWheel

class AutoSetColor(StateMachine):
    wheelactions: ColorWheel

    def __init__(self):
        self.colors = ['y', 'r', 'g', 'b']
        self.direction = True
        self.colorDistance = 37.56 # 11.8", 37.56 rotations (30:1 + 3" diameter)

    def autoSetColor(self):
        self.engage()

    @state(first=True)
    def getColorAndNeeded(self):
        self.myColor = self.wheelactions.getColor() # Make sure this provides the correct value, not an assumption
        self.desiredColor = 'r' # Make this come from FMS later. NOTE: If not a string, simply use a dictionary instead.

        # Forward?
        if self.colors[self.myColor] < self.colors[self.desiredColor]:
            self.direction = True
        elif self.colors[self.myColor] > self.colors[self.desiredColor]:
            self.direction = False
        else:
            self.direction = None

        self.next_state_now(spinWheel)

    def spinWheel(self):
