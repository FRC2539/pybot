from magicbot import StateMachine, timed_state, default_state

from components.intakes.cargo import Cargo

class CargoOutake(StateMachine):
    cargo: Cargo

    shot: bool

    def runOutake(self):
        self.engage()

    @timed_state(first=True, duration=2.0, must_finish=True)
    def run(self):
        self.cargo.outakeBall()
        self.shot = True
