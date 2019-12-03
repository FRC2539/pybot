import wpilib

from ctre import WPI_TalonSRX

from magicbot import StateMachine, state, timed_state, default_state

from components.drivebase.robotdrive import RobotDrive

class DriveRobot(StateMachine):
    #drivetrain = RobotDrive
    
    def beginDrive(self):
        self.engage()
        
    @default_state
    def drive(self):
        self.drivetrain.driveRobot()

    @state(first=True, must_finish=True)
    def prepareToDrive(self):
        self.drivetrain = RobotDrive('tank') # Make this a network table value!

        self.drivetrain.stop()
        self.drivetrain.registerAxes()
        self.next_state('drive')
