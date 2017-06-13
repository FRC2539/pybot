from wpilib.command import Command
from ctre import CANTalon
import subsystems
import ports

# Perform a general system check on the robot.
class SystemCheck(Command):

    def initialize(self):
        # Print information about connection to each system
        print("Firmware Version\n")
        # Drivetrain
        print("Front Left DriveTrain: Version %s" % (CANTalon(ports.drivetrain.frontLeftMotorID).getFirmwareVersion()))
        print("Front Right DriveTrain: Version %s" % (CANTalon(ports.drivetrain.frontRightMotorID).getFirmwareVersion()))
        print("Back Left DriveTrain: Version %s" % (CANTalon(ports.drivetrain.backLeftMotorID).getFirmwareVersion()))
        print("Back Right Drivetrain: Version %s\n" % (CANTalon(ports.drivetrain.backRightMotorID).getFirmwareVersion()))

        # Shooter
        print("Shooter: Version %s" % (CANTalon(ports.shooter.motorID).getFirmwareVersion()))
        print()
        # Pickup
        print("pickup: Version %s" % (CANTalon(ports.pickup.motorID).getFirmwareVersion()))
        print()
        # Climber
        print("Climber: Version %s" % (CANTalon(ports.climber.motorID).getFirmwareVersion()))

        print("Motor PIDs")
        leftDriveTrain = subsystems.drivetrain.activeMotors[0]
        rightDriveTrain = subsystems.drivetrain.activeMotors[1]
        print("Left DriveTrain: %s, %s, %s" % (leftDriveTrain.getP, leftDriveTrain.getI, leftDriveTrain.getD))
        print("Right DriveTrain: %s, %s, %s" % (rightDriveTrain.getP, rightDriveTrain.getI, rightDriveTrain.getD))
        # Print speed of shooter.
        # Print position of each encoder
        # Print velocity of each encoder.
        # Print speed of pickup.
        # Print speed of climber.
        # Print whether a gear in the holder.
        # Print state of the front light.
        # Print state of the back light.
        # Print state of the server.
