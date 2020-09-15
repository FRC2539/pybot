from wpilib import Timer

from wpilib.controller import PIDController, RamseteController, SimpleMotorFeedforward, SimpleMotorFeedforwardMeters
from wpilib.kinematics import ChassisSpeeds, DifferentialDriveKinematics, DifferentialDriveWheelSpeeds
from wpilib.trajectory import Trajectory

from wpilib.command import Command

from trajectoryconstants import DriveConstants, AutoConstants

from crapthatwillneverwork.kougarkoursegenerator import KougarKourseGenerator

import robot

class KougarKourse(Command):

    '''
    No touchy, touchy, my stuffy, stuffy!
    '''

    def __init__(self,
                 trajectory,
                 pose=robot.drivetrain.getPoseMeters,
                 controller=RamseteController(AutoConstants.kRamseteB, AutoConstants.kRamseteZeta),
                 feedforward=SimpleMotorFeedforwardMeters(DriveConstants.ksVolts,
                                DriveConstants.kvVoltsSecondPerMeter,
                                DriveConstants.kaVoltSecondsSquaredPerMeter),
                 kinematics=DifferentialDriveKinematics(DriveConstants.kTrackWidthMeters),
                 wheelSpeeds=robot.drivetrain.getWheelSpeeds,
                 leftController=PIDController(DriveConstants.kPDriveVel, 0, 0),
                 rightController=PIDController(DriveConstants.kPDriveVel, 0, 0),
                 outputVolts=robot.drivetrain.setVolts,
                 requirements=robot.drivetrain
                ):
                     
        if type(trajectory) == int: # Checks for an ID number to make trajectory now.
            trajectory = KougarKourseGenerator(trajectory)
                    
        elif isinstance(trajectory, KougarKourseGenerator): # Checks to see if it is given the KougarKourse object.
            trajectory = trajectory.trajectory # lol
        
        super().__init__()
        
        self.timer = Timer()
        self.trajectory = trajectory
        self.pose = pose
        self.follower = controller
        self.feedforward = feedforward
        self.kinematics = kinematics
        self.speeds = wheelSpeeds
        self.leftController = leftController
        self.rightController = rightController
        self.output = outputVolts
        self.requirements = requirements

        self.usePID = True

        self.requires(requirements)

    def initialize(self):
        self.prevTime = 0
        initialState = self.trajectory.sample(0)
        self.prevSpeeds = self.kinematics.toWheelSpeeds(
            ChassisSpeeds(initialState.velocity,
                          0,
                          initialState.curvature
                           * initialState.velocity))

        self.timer.reset()
        self.timer.start()

        if self.usePID:
            self.leftController.reset()
            self.rightController.reset()

    def execute(self):
        curTime = self.timer.get()
        dt = curTime - self.prevTime # Delta T.

        targetWheelSpeeds = self.kinematics.toWheelSpeeds(
            self.follower.calculate(self.pose(), self.trajectory.sample(curTime)))

        leftSpeedSetpoint = targetWheelSpeeds.left
        rightSpeedSetpoint = targetWheelSpeeds.right

        if self.usePID:
            leftFeedforward = self.feedforward.calculate(leftSpeedSetpoint,
                                                        (leftSpeedSetpoint - self.prevSpeeds.left) / dt)

            rightFeedforward = self.feedforward.calculate(rightSpeedSetpoint,
                                                         (rightSpeedSetpoint - self.prevSpeeds.right) / dt)

            leftOutput = leftFeedforward + self.leftController.calculate(self.speeds().left,
                                                                         leftSpeedSetpoint)

            rightOutput = rightFeedforward + self.rightController.calculate(self.speeds().right,
                                                                            rightSpeedSetpoint)

        else:
            leftOutput = leftSpeedSetpoint
            rightOutput = rightSpeedSetpoint

        self.output(leftOutput, rightOutput)

        self.prevTime = curTime
        self.prevSpeeds = targetWheelSpeeds

    def isFinished(self):
        return self.timer.hasElapsed(self.trajectory.totalTime())

    def end(self):
        self.timer.stop()
