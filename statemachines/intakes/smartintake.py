from magicbot import StateMachine, timed_state, default_state

from components.intakes.cargo import Cargo

class SmartIntake(StateMachine):
    cargo: Cargo

    isRunning: bool
    shot: bool

    def runSmartIntake(self):
        self.engage()

    @timed_state(first=True, duration=5.0, must_finish=True)
    def check(self):
        if self.isRunning:
            self.cargo.holdCargo()
            self.isRunning = False
            self.shot = False
            self.done()

        else:
            self.cargo.intakeBall()
            self.isRunning = True
            self.shot = False
            self.next_state(self.slowAfterTime)

    @default_state
    def slowAfterTime(self):
        if not self.shot:
            self.cargo.holdCargo() # Used if an op forgets to slow intake or for an auto hold.
        else:
            self.cargo.stop()
