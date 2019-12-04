import ctre
import ports

# NOTE: Remember to use the getSpeed() method!

class VelocityProducer:
    def __init__(self, speedMultiplier=1, rotateModifier=1):
        self.speedMultiplier = speedMultiplier
        self.rotateModifier = rotateModifier
                
        self.checkParameters()
        
        self.simple = True
        
    def checkParameters(self):
        if self.speedMultiplier <= 0 or self.rotateModifier <= 0:
            raise ValueError('Please give a float that is greater than zero for the multipliers and modifiers!')
        
    def checkSimpleDriving(self):
        # Checks for multipliers in order to disable unecessary calculations. NOTE: Should run at the beginning and init. 
        if self.speedMultiplier == 1 and self.rotateModifier == 1:
            self.simple = True
        else:
            self.simple = False

        return self.simple

class TankDrive(VelocityProducer):
    def __init__(self, speedMultiplier=1, rotateModifier=1):
        super().__init__(speedMultiplier, rotateModifier)
        
        self.speedMultiplier = speedMultiplier
        self.rotateModifier = rotateModifier
        
        self.getSpeedT = self.getSimpleTankSpeed
        
        if not self.checkSimpleDriving():   # Configures for quick calculations based off of presets
            self.getSpeed = self.getComplexTankSpeed
        
    def configureFourTank(self, motors):
        # Give list of 4 motors
        self.activeMotors = motors[0:2]
        
        if len(motors) != 4:
            raise 'Could not configure for four motor tank because there were not four given motors!' 
        else:
            motors[ports.DrivetrainPorts.BackLeftMotor].follow(motors[ports.DrivetrainPorts.FrontLeftMotor])
            motors[ports.DrivetrainPorts.BackRightMotor].follow(motors[ports.DrivetrainPorts.FrontRightMotor])
    
        return self.activeMotors

    def getSimpleTankSpeed(self, x, y, rotate):
        return [y + rotate, -y + rotate]
    
    def getComplexTankSpeed(self, x, y, rotate):
        return [(y + (rotate * self.rotateModifier)) * self.speedMultiplier, (-y + (rotate * self.rotateModifier)) * self.speedMultiplier]
        
class MecanumDrive(VelocityProducer):
    def __init__(self, speedMultiplier=1, rotateModifier=1):
        super().__init__(speedMultiplier, rotateModifier)
        
        self.speedMultiplier = speedMultiplier
        self.rotateModifier = rotateModifier
        
        self.getSpeedM = self.getSimpleMecanumSpeed
        
        if not self.checkSimpleDriving():
            self.getSpeed = self.getComplexMecanumSpeed
        
    def configureMecanum(self, motors):
        self.activeMotors = motors
        
    def getSimpleMecanumSpeed(self, x, y, rotate):
        return [
            x + y + rotate,
            x - y + rotate,
            -x + y + rotate,
            -x - y + rotate
            ] 

    # Really elaborate, and I imagine it will be slow; however we, the band of brothers, declared never to use mecanum again, so...
    def getComplexMecanumSpeed(self, x, y, rotate):
        return [
            (x + y + (rotate * self.rotateModifier)) * self.speedMultiplier,
            (x - y + (rotate * self.rotateModifier)) * self.speedMultiplier,
            (-x + y + (rotate * self.rotateModifier)) * self.speedMultiplier,
            (-x - y + (rotate * self.rotateModifier)) * self.speedMultiplier
            ] 
