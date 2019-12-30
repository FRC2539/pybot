from magicbot import StateMachine, timed_state, default_state

from components.intakes.cargo import Cargo

class CargoOutake(StateMachine):
    cargo: Cargo

    shot: bool

    def runOutake(self):
        self.engage()

    @timed_state(first=True, duration=1.0)
    def run(self):
        self.cargo.outakeBall()
        self.shot = True

    def default(self):
        pass
