from magicbot import StateMachine, state

from components.colorwheel import ColorWheel

# WARNING: This is actually gonna set the color to your position. Needs to go to the 'sensor' location.

class AutoSetColor(StateMachine):
    wheelactions: ColorWheel

    def __init__(self):
        self.colors = ['y', 'r', 'g', 'b']

        self.direction = 1 # Clockwise
        self.distance = 0 # color spaces away

        self.colorDistance = 37.56 # 11.8", 37.56 rotations (30:1 + 3" diameter)

    def autoSetColorCommand(self):
        self.engage()

    @state(first=True)
    def getColorAndNeeded(self):
        self.myColor = self.wheelactions.getColor() # Make sure this provides the correct value, not an assumption
        self.desiredColor = 'r' # Make this come from FMS later. NOTE: If not a string, simply use a dictionary instead.

        self.distance = abs(self.colors[self.myColor] - self.colors[self.desiredColor])

        # Forward?
        if self.colors[self.myColor] < self.colors[self.desiredColor]:
            self.direction = 1

        elif self.colors[self.myColor] > self.colors[self.desiredColor]:
            self.direction = -1

        else:
            self.done()

        self.next_state_now('spinWheel')

    @state
    def spinWheel(self):
        self.wheelactions.autoSpinWheel(self.colorDistance * self.colorDistance * self.direction)
