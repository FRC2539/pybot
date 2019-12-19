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
        #self.robotdrive.prepareToDrive()

    @default_state
    def drive(self):
        pass
        #self.robotdrive.move()
