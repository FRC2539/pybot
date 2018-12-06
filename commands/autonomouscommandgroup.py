from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from custom.config import Config

import subsystems
import wpilib

from wpilib.command.waitcommand import WaitCommand
from commands.network.alertcommand import AlertCommand
from commands.drivetrain.resetencodercommand import ResetEncoderCommand

import pathfinder as pf
import math
import ports

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')


        self.addSequential(ResetEncoderCommand())

        points = [
        pf.Waypoint(-4, -1, math.radians(-45.0)),
        pf.Waypoint(-2, -2, 0),
        pf.Waypoint(0, 0, 0),
        ]

        info, trajectory = pf.generate(points, pf.FIT_HERMITE_CUBIC, pf.SAMPLES_HIGH,
                                    dt=0.05, # 50ms
                                    max_velocity=1.7,
                                    max_acceleration=2.0,
                                    max_jerk=60.0)
        print('generated trajectory')
        self.addSequential(AlertCommand("generated trajectory"))
        # Wheelbase Width = 0.5m
        modifier = pf.modifiers.TankModifier(trajectory).modify(0.73)

        # Do something with the new Trajectories...
        left = modifier.getLeftTrajectory()
        right = modifier.getRightTrajectory()

        leftFollower = pf.followers.EncoderFollower(left)
        leftFollower.configureEncoder(0, 232, 6)
        leftFollower.configurePIDVA(1.0, 0.0, 0.0, 1 / 1.7, 0)

        rightFollower = pf.followers.EncoderFollower(right)
        rightFollower.configureEncoder(0, 232, 6)
        rightFollower.configurePIDVA(1.0, 0.0, 0.0, 1 / 1.7, 0)

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
