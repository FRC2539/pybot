import wpilib

from components.intake import Intake

from magicbot import StateMachine, state, timed_state, default_state

class IntakeBallsCommand(StateMachine): # Made in a state machine because it's easier to implement auto holds and stuff.

    intake: Intake
    intakeRunning: bool

    def intakeCommand(self):
        self.engage()

    @state(first=True)
    def runOrStopIntake(self):
        if not self.intakeRunning:
            self.intake.intake()
        else:
            self.intake.stop()

        self.intakeRunning = not self.intakeRunning

        self.done()
