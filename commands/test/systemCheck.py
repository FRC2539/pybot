from wpilib.command import Command
from ctre import CANTalon
import subsystems
import ports

# Perform a general system check on the robot.
class SystemCheck(Command):

    def initialize(self):
        # Print information about connection to each system
        print("Connection to system\n")
        # Drivetrain
        print("DriveTrain\n")
        print("Front Left: %s" % (CANTalon(ports.drivetrain.frontLeftMotorID).getFirmwareVersion()))
        print("Front Right: %s" % (CANTalon(ports.drivetrain.frontRightMotorID).getFirmwareVersion()))
        print("Back Left: %s" % (CANTalon(ports.drivetrain.backLeftMotorID).getFirmwareVersion()))
        print("Back Right: %s\n" % (CANTalon(ports.drivetrain.backRightMotorID).getFirmwareVersion()))
        # Shooter
        print("Shooter\n")
        print(CANTalon(ports.shooter.motorID).getFirmwareVersion())
        print()
        # Pickup
        print("Pickup\n")
        print(CANTalon(ports.pickup.motorID).getFirmwareVersion())
        print()
        # Climber
        print("Climber\n")
        print(CANTalon(ports.climber.motorID).getFirmwareVersion())

        # Print PID values of each motor.
        # Print speed of shooter.
        # Print position of each encoder
        # Print velocity of each encoder.
        # Print speed of pickup.
        # Print speed of climber.
        # Print whether a gear in the holder.
        # Print state of the front light.
        # Print state of the back light.
        # Print state of the server.
