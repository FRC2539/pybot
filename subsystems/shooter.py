from .cougarsystem import *

from ctre import WPI_TalonFX, FeedbackDevice, ControlMode, NeutralMode

from networktables import NetworkTables as nt

import ports


class Shooter(CougarSystem):
    """Controls the robot's shooter."""

    def __init__(self):
        super().__init__("Shooter")

        self.table = nt.getTable("Shooter")

        # Initialize the first motor.
        self.shooterMotorOne = WPI_TalonFX(ports.shooter.shooterMotorOneID)
        self.shooterMotorOne.configSelectedFeedbackSensor(
            FeedbackDevice.IntegratedSensor, 0, 0
        )

        # Initialize the second motor.
        self.shooterMotorTwo = WPI_TalonFX(ports.shooter.shooterMotorTwoID)
        self.shooterMotorTwo.configSelectedFeedbackSensor(
            FeedbackDevice.IntegratedSensor, 0, 0
        )

        # Set the behavior for when both motors are in "neutral", or are not being moved.
        self.shooterMotorOne.setNeutralMode(NeutralMode.Coast)
        self.shooterMotorTwo.setNeutralMode(NeutralMode.Coast)

        # Set the PID configuration.
        self.shooterMotorOne.config_kF(0, 0.055, 0)
        self.shooterMotorOne.config_kP(0, 0.165, 0)
        self.shooterMotorOne.config_kI(0, 0, 0)
        self.shooterMotorOne.config_kD(0, 0.0001, 0)
        self.shooterMotorOne.config_IntegralZone(0, 0, 0)

        self.shooterMotorOne.setInverted(False)
        self.shooterMotorTwo.setInverted(True)

        # Tell the second motor to follow the behavior of the first motor.
        self.shooterMotorTwo.follow(self.shooterMotorOne)

        # Create state variables.
        self.shooting = False
        self.atGoal = False

        # Set the range of velocities.
        self.maxVel = 5800
        self.minVel = 2800

        def setRPM(self, rpm):
            # Update the state of the subsytem.
            self.shooting = True
            # Update the current speed of the motor.
            # With the second motor following the first, no command is needed for the second motor.
            self.shooterMotorOne.set(ControlMode.Velocity, self.rpmToSensor(rpm))

        def setPercent(self, val):
            self.shooting = True
            self.shooterMotorOne.set(ControlMode.PercentOutput, val)

        def reverseShooter(self):
            self.shooting = True
            # Tell the motor to go in reverse (negative percent).
            self.shooterMotorOne.set(ControlMode.PercentOutput, -0.4)

        def stopShooter(self):
            self.shooting = False
            self.shooterMotorOne.stopMotor()

        def updateNetworkTables(self):
            # Send the current average RPM to network tables.
            self.table.putNumber("ShooterRPM", round(self.getRPM(), 0))

        def zeroNetworkTables(self):
            self.table.putNumber("ShooterRPM", 0)

        def rpmToSensor(self, rpm):
            return (rpm * 2048) / 600

        def sensorToRPM(self, units):
            return (units * 600) / 2048

        def isShooting(self):
            return self.shooting

        def getRPM(self):
            # Return the current average RPM of the motor.
            return self.sensorToRPM(self.shooterMotorOne.getSelectedSensorVelocity())
