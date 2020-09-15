from wpilib import Timer

from wpilib.controller import PIDController, RamseteController, SimpleMotorFeedforward

from wpilib.kinematics import ChassisSpeeds, DifferentialDriveKinematics, DifferentialDriveWheelSpeeds

from wpilib.trajectory import Trajectory

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
