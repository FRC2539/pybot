from wpilib.command import Command
from custom import driverhud
from custom.config import MissingConfigError
import robot


class MoveCommand(Command):
    def __init__(self, distance, angle=0, tolerance=3,  name=None):
        """
        Takes a distance in inches and stores it for later. We allow overriding
        name so that other autonomous driving commands can extend this class.
        """

        if name is None:
            name = "Move %f inches" % distance

        super().__init__(name, 0.2)

        self.distance = -distance
        self.angle = angle
        self.tol = tolerance # Angle tolerance in degrees.
        
        self.blocked = False
        self.requires(robot.drivetrain)

    def initialize(self):
        robot.drivetrain.setModuleProfiles(1, turn=False)

        self.count = 0
        self.startPos = robot.drivetrain.getPositions()
        
        robot.drivetrain.setModuleAngles(self.angle)

    def execute(self):
        self.count = 0
        if self.count != 4:
            for currentAngle in robot.drivetrain.getModuleAngles():
                if abs(currentAngle - self.angle) < self.tol or abs(currentAngle - self.angle - 360)< self.tol:
                    self.count += 1
                else:
                    continue
                    
                
        if self.count == 4: # All angles aligned.
            robot.drivetrain.setPositions([
                self.distance, 
                self.distance,
                self.distance,
                self.distance
                ])
            
            robot.drivetrain.setModuleAngles(self.angle)
        
    def isFinished(self):
        count = 0
        for position, start in zip(robot.drivetrain.getPositions(), self.startPos):
            if abs(position - (start + self.distance) ) < 1:
                count += 1
            else:
                return False
                
        if count == 4:
            return True
    
    def end(self):
        robot.drivetrain.stop()
        robot.drivetrain.setModuleProfiles(0, turn=False)
