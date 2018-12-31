from wpilib.command import CommandGroup

import commandbased.flowcontrol as fc
from custom.config import Config
from pathfinder.followers import EncoderFollower
#from navx.ahrs import AHRS

import subsystems
import wpilib

from wpilib.command.waitcommand import WaitCommand
from commands.network.alertcommand import AlertCommand
from commands.drivetrain.resetencodercommand import ResetEncoderCommand
from commands.drivetrain.followtrajectorycommand import FollowTrajectoryCommand

import pathfinder as pf
import math
import ports
from ctre import ControlMode, NeutralMode, WPI_TalonSRX, FeedbackDevice


class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        points = [
        (0, 0, 0),
        (0, 24, 0),
        ]

    #    self.addSequential(FollowTrajectoryCommand(points, pf.FIT_HERMITE_CUBIC, 1.7, 2.0, 60.0))


"""

        self.addSequential(FollowPathCommand([
            (x, y, z),
            (a, b, c)
        ])


        self.addSequential(ResetEncoderCommand())

        points = [
        (-4, -1, -45.0),
        (-2, -2, 0),
        (0, 0, 0),
        ]

        info, trajectory = pf.generate(points, pf.FIT_HERMITE_CUBIC, pf.SAMPLES_HIGH,
                                    dt=0.05, # 50ms
                                    max_velocity=1.7,
                                    max_acceleration=2.0,
                                    max_jerk=60.0)

        print('generated trajectory')
        self.addSequential(AlertCommand("generated trajectory"))
        # Wheelbase Width = 0.5m

        # Do something with the new Trajectories...
        #left = modifier.getLeftTrajectory()
        #right = modifier.getRightTrajectory()
        returnval = FrontLeftMotor.getSelectedSensorPosition(0)
        print(str(returnval) + 'is the current sensor position!')




        leftEncoderPosition = getEncPosition()

        leftFollower = EncoderFollower(modifier.getLeftTrajectory())
        #leftFollower = EncoderFollower(left)
        leftFollower.configureEncoder(getEncPosition, 232, 6)
        leftFollower.configurePIDVA(1.0, 0.0, 0.0, 1 / 1.7, 0)

        rightFollower = EncoderFollower(modifier.getRightTrajectory())
        rightFollower.configureEncoder(getQuadraturePosition, 232, 6)
        rightFollower.configurePIDVA(1.0, 0.0, 0.0, 1 / 1.7, 0)

#       Above should be working ...

        leftOutput = leftFollower.calculate(drivetrain.getPositions[0]); #Should be getSensorCollection, but this has not been working.

        encoder_position_left = 0

        gyro_heading = 0 #navx.getAngle()
        desired_heading = pf.r2d(leftFollower.getHeading())
        angleDifference = pf.boundHalfDegrees(desired_heading - gyro_heading)
        turn = 0.8 * (-1.0/80.0) * angleDifference

        #TODO Fix below, look into navX code.

        #setLeftMotors(1 + turn)

        l = leftFollower.calculate(encoder_position_left)

        self.leftFollower = leftFollower
        self.rightFollower = rightFollower

        self.addSequential(AlertCommand("auto done"))
        # This code renders the followed path on the field in simulation (requires pyfrc 2018.2.0+)
        if wpilib.RobotBase.isSimulation():
            from pyfrc.sim import get_user_renderer
            renderer = get_user_renderer()
            if renderer:
                renderer.draw_pathfinder_trajectory(left, color='#0000ff', offset=(-1,0))
                renderer.draw_pathfinder_trajectory(modifier.source, color='#00ff00', show_dt=1.0, dt_offset=0.0)
                renderer.draw_pathfinder_trajectory(right, color='#0000ff', offset=(1,0))

"""
