from wpilib import Timer

from wpilib.controller import PIDController, RamseteController, SimpleMotorFeedforward

from wpilib.kinematics import ChassisSpeeds, DifferentialDriveKinematics, DifferentialDriveWheelSpeeds

from wpilib.trajectory import Trajectory

from wpilib.geometry import Pose2D

from wpilib.command import Command

class RamseteCommand(Command):

    def __init__(self,
                 trajectory,
                 pose,
                 controller,
                 feedforward,
                 kinematics,
                 wheelSpeeds,
                 leftController,
                 rightController,
                 outputVolts,
                 requirements
                ):

        self.timer = Timer()
        self.trajectory = trajectory
        self.pose = pose
        self.controller = controller
        self.feedforward = feedforward
        self.kinematics = kinematics
        self.wheelSpeeds = wheelSpeeds
        self.leftController = leftController
        self.rightController = rightController
        self.outputVolts = outputVolts
        self.requirements = requirements

        self.usePID = True

        self.requires(requirements)

    def initialize(self):
        self.prevTime = 0
        initialState = self.trajectory.sample(0)
        self.prevSpeeds = self.kinematics.toWheelSpeeds(
            ChassisSpeeds(initialState.velocityMetersPerSecond,
                          0,
                          initialState.curvatureRadPerMeter
                           * initialState.velocityMetersPerSecond))

        self.timer.reset()
        self.timer.start()

        if self.usePID:
            self.leftController.reset()
            self.rightController.reset()

    def execute(self):
        curTime = self.timer.get()
        dt = curTime - self.prevTime # Delta T.

        # At this point, we encountered an error. Look at the github.
