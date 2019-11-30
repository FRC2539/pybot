import ctre
import ports

class VelocityProducer:
    def __init__(self, speedMultiplier=1, rotateModifier=1):
        self.speedMultiplier = speedMultiplier
        self.rotateModifier = rotateModifier
        
        self.fieldOriented = False
        
    def checkParameters(self):
        if self.speedMultiplier <= 0 or self.rotateModifier <= 0:
            raise ValueError('Please give a float that is greater than zero for the multipliers and modifiers!')

class TankDrive(VelocityProducer):
    def configureFourTank(self, motors):
        # Give list of 4 motors
        self.activeMotors = motors[0:2]
        
        if len(motors) != 4:
            raise 'Could not configure for four motor tank because there were not four given motors!' 
        else:
            motors[ports.DrivetrainPorts.BackLeftMotor].follow(motor[ports.DrivetrainPorts.FrontLeftMotor])
            motors[ports.DrivetrainPorts.BackRightMotor].follow(motor[ports.DrivetrainPorts.FrontRightMotor])
    
        return self.activeMotors
    
    def getTankSpeed(self, x, y, rotate):
        return [(y + (rotate * rotateModifier)) * speedMultiplier, (-y + (rotate * rotateModifier)) * speedMultiplier
        
class MecanumDrive(VelocityProducer):
    def configureMecanum(self, motors):
        self.activeMotors = motors
        
    def getMecanumSpeed(self, x, y, rotate):
        return [
            x + y + rotate,
            x - y + rotate,
            -x + y + rotate,
            -x - y + rotate
            ] 
