from ctre import CANCoderConfiguration, AbsoluteSensorRange


class Constants:
    pass


"""
Use this class to declare variables that may have to be 
adjusted a lot. This makes it more global and easier to find. 
Please note that this is not the ports.py. That should host 
IDs for the CANbus, sensors, PWM, and the liking. 
"""

drivetrain = Constants()

drivetrain.dPk = 0.01
drivetrain.dIk = 0
drivetrain.dDk = 0
drivetrain.dFFk = 0
drivetrain.dIZk = 0

drivetrain.tPk = 10
drivetrain.tIk = 0
drivetrain.tDk = 100
drivetrain.tFFk = 0
drivetrain.tIZk = 0

drivetrain.driveMotorGearRatio = 6.86
drivetrain.turnMotorGearRatio = 12.8

drivetrain.motionAcceleration = 10000
drivetrain.motionCruiseVelocity = 800

drivetrain.wheelDiameter = 4

drivetrain.wheelBase = 23.5
drivetrain.trackWidth = 23.5

drivetrain.speedLimit = (
    160.0  # in inches per second (if you have feet per second, multiply by 12!)
)

drivetrain.encoderConfig = CANCoderConfiguration()
drivetrain.encoderConfig.absoluteSensorRange = AbsoluteSensorRange.Signed_PlusMinus180
