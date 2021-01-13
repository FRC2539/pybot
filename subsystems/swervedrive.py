from .basedrive import BaseDrive
from .swervemodule import SwerveModule

import ports

import math

class SwerveDrive(BaseDrive):
    
    def __init__(self, name):
        super().__init__(name)
        
        self.isFieldOriented = True
    
        self.wheelBase = 23.5 # These are distances across the robot; horizontal, vertical, diagonal.
        self.trackWidth = 23.5
        self.r = math.sqrt(self.wheelBase ** 2 + self.trackWidth ** 2)
        
        self.modules = [
            SwerveModule(ports.drivetrain.frontLeftDriveID, ports.drivetrain.frontLeftTurnID, # Front left module.
                         ports.drivetrain.frontLeftCANCoder, self.speedLimit),
            
            SwerveModule(ports.drivetrain.frontRightDriveID, ports.drivetrain.frontRightTurnID, # Front right module.
                         ports.drivetrain.frontRightCANCoder, self.speedLimit),
            
            SwerveModule(ports.drivetrain.backLeftDriveID, ports.drivetrain.backLeftTurnID, # Back left module.
                         ports.drivetrain.backLeftCANCoder, self.speedLimit),
            
            SwerveModule(ports.drivetrain.backRightDriveID, ports.drivetrain.backRightTurnID, # Back right module.
                         ports.drivetrain.backRightCANCoder, self.speedLimit)
                        ]
    
    def _configureMotors(self):
        '''
        Configures the motors. Shouldn't need this. 
        '''
        
        self.activeMotors = self.motors[0:2] # Don't actually need these, this just keeps basedrive happy. 
    
    def _calculateSpeeds(self, x, y, rotate):
        '''
        Gonna take this nice and slow. Declaring variables to be simple,
        should try to walk through while coding. 
        '''
        x = 1
        y = 1
        rotate = 1
        
        theta = self.getAngle() * (math.pi / 180)
            
        if self.isFieldOriented:
            
            temp = y * math.cos(theta) + x * math.sin(theta) # just the new y value being temporarily stored.
            x = -y * math.sin(theta) + x * math.cos(theta)
            y = temp
            
        A = x - rotate * (self.wheelBase / self.r)
        B = x + rotate * (self.wheelBase / self.r)
        C = y - rotate * (self.trackWidth / self.r)
        D = y + rotate * (self.trackWidth / self.r)
        
        ws1 = math.sqrt(B**2 + D**2) # Front left speed
        ws2 = math.sqrt(B**2 + C**2) # Front right speed
        ws3 = math.sqrt(A**2 + D**2) # Back left speed
        ws4 = math.sqrt(A**2 + C**2) # Back right speed
        
        wa1 = math.atan2(B, D) * 180 / math.pi # Front left angle (degrees)
        wa2 = math.atan2(B, C) * 180 / math.pi # Front right angle
        wa3 = math.atan2(A, D) * 180 / math.pi # Back left angle
        wa4 = math.atan2(A, C) * 180 / math.pi # Back right angle
        
        speeds = [ws1, ws2, ws3, ws4] # It is in order.
        angles = [wa1, wa2, wa3, wa4] # It is in order.
        
        newSpeeds = speeds # Do NOT delete! This IS used!
        newAngles = [] # Do NOT delete! This IS
        
        maxSpeed = max(speeds) # Find the largest speed.
        minSpeed = min(speeds) # Find the smallest speed.
        
        if maxSpeed > 1: # Normalize speeds if greater than 1, but keep then consistent with each other.
            speeds[:] = [speed / maxSpeed for speed in speeds]
        
        if minSpeed < -1: # Normalize speeds if less than -1, but keep then consitent with each other.
            speeds[:] = [speed / minSpeed * -1 for speed in speeds]

        magnitude = math.sqrt((x**2) + (y**2))
        if magnitude > 1:
            magnitude = 1
        
        speeds[:] = [speed * magnitude for speed in speeds]
        
        for angle in angles:
            if angle < 0:
                newAngles.append(angle + 360)
            else:
                newAngles.append(angle)
            
        return newSpeeds, newAngles
                    
    def move(self, x, y, rotate):
        '''
        Turns coordinate arguments into motor outputs.
        Short-circuits the rather expensive movement calculations if the
        coordinates have not changed.
        '''
                
        if [x, y, rotate] == self.lastInputs:
            return
        
        self.lastInputs = [x, y, rotate]

        '''Prevent drift caused by small input values'''
        x = math.copysign(max(abs(x) - self.deadband, 0), x)
        y = math.copysign(max(abs(y) - self.deadband, 0), y)
        rotate = math.copysign(max(abs(rotate) - self.deadband, 0), rotate)

        speeds, angles = self._calculateSpeeds(x, y, rotate)

        for module, speed, angle in zip(self.modules, speeds, angles): # You're going to need encoders, so only focus here.
            module.setWheelAngle(angle)
            module.setWheelSpeed(speed)

    def normalizeGyro(self, a):
        return (a - (math.floor(a / 360) * 360))
    
    def stop(self):
        for module in self.modules:
            module.stopModule()
            
    def setProfile(self, profile):
        for module in self.modules:
            module.setModuleProfile(profile)

    def setFieldOriented(self, fieldCentric=True):
        self.isFieldOriented = fieldCentric