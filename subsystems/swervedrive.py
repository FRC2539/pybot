from .basedrive import BaseDrive
from .swervemodule import SwerveModule

import math

class SwerveDrive(BaseDrive):
    
    def __init__(self, name):
        super().__init__(name)
        
        self.isFieldOriented = True
    
        self.wheelBase = 0 # These are distances across the robot; horizontal, vertical, diagonal.
        self.trackWidth = 0
        self.radius = 0
    
    def _configureMotors(self):
        pass
    
    def _calculateSpeeds(self, x, y, rotate):
        '''
        Gonna take thsi nice and slow. Declaring variables to be simple,
        should try to walk through while coding. Reference the Ether whitepaper on
        Chief Delphi for the explanation for the calculations.
        '''
        
        angle = math.atan(y / x)
        
        if self.isFieldOriented:
            angle = angle - math.radians(self.normalizeGyro(self.getAngle()))
            
        A = x - angle * (self.wheelBase / self.radius)
        B = x + angle * (self.wheelBase / self.radius)
        C = y - angle * (self.trackWidth / self.radius)
        D = y + angle * (self.trackWidth / self.radius)
        
        ws1 = math.sqrt(B**2 + D**2) # Front left speed
        ws2 = math.sqrt(B**2 + C**2) # Front right speed
        ws3 = math.sqrt(A**2 + D**2) # Back left speed
        ws4 = math.sqrt(A**2 + C**2) # Back right speed
        
        wa1 = math.atan2(B, D) * 180 / math.pi # Front left angle
        wa2 = math.atan2(B, C) * 180 / math.pi # Front right angle
        wa3 = math.atan2(A, D) * 180 / math.pi # Back left angle
        wa4 = math.atan2(A, C) * 180 / math.pi # Back right angle
        
        speeds = [ws1, ws2, ws3, ws4]
        angles = [wa1, wa2, wa3, wa4]
        
        maxSpeed = max(speeds) # Find the largest speed.
        minSpeed = min(speeds)
        
        if maxSpeed > 1: # Normalize speeds if greater than 1, but keep then consistent with each other.
            for speed in speeds:
                speed /= maxSpeed
        
        if minSpeed < -1:
            for speed in speeds:
                speed /= minSpeed *-1

        magnitude = math.sqrt((x**2) + (y**2))
        if magnitude > 1:
            magnitude = 1
            
        for speed in speeds:
            speed *= magnitude
            
        return speeds, angles
                
    def normalizeGyro(self, a):
        return (a - (math.floor(a / 360) * 360))
