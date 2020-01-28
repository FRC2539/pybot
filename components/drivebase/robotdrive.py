import wpilib
import math

from controller import logicalaxes

from components.drivebase.drivevelocities import TankDrive

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

class RobotDrive:

    robotdrive_motors: list

    activeMotors: list

    velocityCalculator: object # Establishes drive

    build: object

    useActives: list

    rumble: bool

    def __init__(self):     # NOTE: Be careful with this new init, as I added it after running it on a robot. It passes tests though, so we should be "gucci". Also note that you cannot access VI stuff in __init__.
        pass

    def assignFuncs(self, bot):

        # Assigns functions that are motor controller specific

        if bot:
            self.move = self.falconMove

        else:
            self.move = self.neoMove

    def prepareToDrive(self, bot):
        self.assignFuncs(bot)

        print(str(self.velocityCalculator))
        for motor in self.robotdrive_motors:
            motor.setNeutralMode(NeutralMode.Brake)
            motor.setSafetyEnabled(False)
            motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)

            # Configures mm stuff.
            motor.configMotionAcceleration(300) # Dummy value
            motor.configMotionCruiseVelocity(500) # Dummy value

        self.resetPID()

        self.rumble = False

        self.build.setDualRumble() # TEMPORARY!!!

        self.useActives = self.velocityCalculator.configureFourTank(self.robotdrive_motors)

    def getPositions(self):
        # Temporary...probably
        pos = [
                float(self.useActives[0].getQuadraturePosition()),
                float(self.useActives[1].getQuadraturePosition()),
                ]
        print(pos)

    def calculateTankSpeed(self, y, rotate, x=0):
        return [y + rotate, -y + rotate]

    def stop(self):
        for motor in self.useActives:
            motor.stopMotor()

    def neoMove(self):
        y = self.build.getY() * -1
        if abs(y) < 0.01:
            y = 0.0 # added for stupid sensitivity issue.
        speeds = self.velocityCalculator.getSpeedT(
                                        y=float(y),
                                        rotate=float(self.build.getRotate())
                                            )


        ##print(str(y))
        #if (abs(speeds[0]) > 0.95 and abs(speeds[1])) and not self.rumble > 0.95: # Probably only temporary, as this will slow the process down.
            ##print('set rumble')
            #self.build.setDualRumble()
            #self.rumble = True
        #elif (abs(speeds[0]) < 0.95 or abs(speeds[1]) < 0.95) and self.rumble: # Runs if they're less than almost full and if rumble is engaged.
            ##print('disabled rumble')
            #self.build.disableRumble()
            #self.rumble = False

        for speed, motor in zip(speeds, self.useActives):
            motor.set(ControlMode.PercentOutput, speed)

    def falconMove(self):
        pass

    def getPosition(self):
        positions = []
        for motor in self.useActives:
            positions.append(motor.getSelectedSensorPosition())

        return positions

    def setPositions(self, positions):
        for motor, position in zip(self.useActives, positions):
            motor.set(ControlMode.MotionMagic, position) # motion magic works because of config above.

    def resetPosition(self):
        for motor in self.useActives:
            motor.setQuadraturePosition(0)

    def getAveragePosition(self, targets):
        error = 0
        for motor, target in zip(self.useActives, targets):
            error += abs(target - motor.getSelectedSensorPosition())

        return error

    def inchesToTicks(self, distance): #distance -> inches!
        # First does the wheel rotations necessary by dividing the distance by wheel the circumference. Takes this and multiplies by required ticks for one rotation (250)
        return (distance / (math.pi * 6)) * 250

    def resetPID(self):
        for motor in self.useActives:
            motor.configClosedLoopRamp(0, 0)
            for profile in range(2):
                motor.config_kP(profile, 1, 0)
                motor.config_kI(profile, 0.001, 0)
                motor.config_kD(profile, 31, 0)
                motor.config_kF(profile, 0.7, 0)
                motor.config_IntegralZone(profile, 30, 0)

    def execute(self):
        # Functions as a default for a low level (kinda)
        self.move()

    def default(self):
        pass
