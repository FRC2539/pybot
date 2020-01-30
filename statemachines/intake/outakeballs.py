import wpilib

from components.intake.intake import Intake

from magicbot import StateMachine, state, timed_state, default_state

class OutakeBallsCommand(StateMachine): # Made in a state machine because it's easier to implement auto holds and stuff.

    intake: Intake
    intakeRunning: bool


    def outakeCommand(self):
        self.engage()

    @timed_state(first=True, duration=2.0, must_finish=True)
    def outake(self):
        self.intake.outake()

        self.next_state('killIt')

    @state
    def killIt(self):
        self.intake.stop()
        self.intakeRunning = False

        self.done()
