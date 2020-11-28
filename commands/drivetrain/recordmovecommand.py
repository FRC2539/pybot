from wpilib.command import Command

import robot


class RecordMoveCommand(Command):

    def __init__(self):
        super().__init__('Record Move')
        
        self.requires(robot.drivetrain)

        self.speedLimit = robot.drivetrain.speedLimit

        robot.drivetrain.resetPID()

    def initialize(self):
        robot.drivetrain.capturedPoints = [robot.drivetrain.getPositions()]
        
        robot.drivetrain.updateOdometry()
        robot.drivetrain.stop()
        try:
            robot.drivetrain.setSpeedLimit(self.speedLimit)
        except (ValueError, MissingConfigError):
            print('Could not set speed to %s' % self.speedLimit)
            driverhud.showAlert('Drive Train is not configured')
            robot.drivetrain.enableSimpleDriving()

        self.lastY = None
        self.slowed = False
        
        robot.drivetrain.setProfile(0)

    def execute(self):

        robot.drivetrain.updateOdometry()
        # Avoid quick changes in direction
        y = logicalaxes.driveY.get() * 0.8
        if self.lastY is None:
            self.lastY = y
        else:
            cooldown = 0.05
            self.lastY -= math.copysign(cooldown, self.lastY)

            # If the sign has changed, don't move
            if self.lastY * y < 0:
                y = 0

            if abs(y) > abs(self.lastY):
                self.lastY = y

        robot.drivetrain.move(
            0,
            y,
            logicalaxes.driveX.get() * 0.4
        )
        
    def end(self):
        robot.drivetrain.stop()
        self.outputResults()
        robot.drivetrain.capturedPoints = []
        
    def outputResults(self):
        count = 1
        last = robot.drivetrain.capturedPoints[0]
        
        for pos in robot.drivetrain.capturedPoints:
            if not count == 1:
        
                leftUnits = robot.drivetrain.getPositions()[0] - last[0]
                rightUnits = robot.drivetraion.getPositions()[1] - last[1]
                leftInches = robot.drivetrain.unitsToInches(leftUnits)
                rightInches = robot.drivetrain.unitsToInches(rightUnits)
                
                print('Segment ' + str(count) + ': Left: ' + str(leftUnits) + ' specific units / ' + str(leftInches) + ' inches ' + ' Right: ' + str(rightUnits) + ' specific units / ' +  str(rightInches) + ' inches') 
            
            count += 1
            last = pos
            
