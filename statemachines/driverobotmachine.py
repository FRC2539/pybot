import wpilib

from ctre import WPI_TalonSRX

from components.drivebase.robotdrive import RobotDrive

from magicbot import StateMachine, state, timed_state, default_state

class DriveRobotMachine(StateMachine):
    robotdrive = RobotDrive

    def beginDrive(self):
        self.engage()
        # Tells the state machine to beginDrive

    @state(first=True)
    def startMachine(self):
        pass

    @default_state
    def drive(self):
        self.robotdrive.move()
