from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for pneumatics')

        self.requires(robot.ledsystem)
        self.requires(robot.pneumatics)

    def initalize(self):
        robot.ledsystem.rainbowLava()

    def execute(self):
        
        # Air
        
        if robot.pneumatics.isPressureLow() and not robot.shooter.shooting:
            robot.pneumatics.enableCLC()
            robot.pneumatics.startCompressor()
            
        elif (robot.pneumatics.isPressureLow() or robot.pneumatics.isCompressorRunning()) and robot.shooter.shooting:
            robot.pneumatics.stopCompressor()
            robot.pneumatics.disableCLC()
            
        # LEDs
        
        # Shooting should look like:
        # WHITE -> GREEN -> ORANGE
        # The heartbeat is determined by the air pressure. A hearbeat signal means LOW pressure (bad).
        # WHITE to let you know shooter isn't at speed yet, GREEN then to let you know at speed and ready,
        # just continue with the FireSequence command. Then, the ORANGE should be shooting balls.
        
        if robot.pneumatics.isPressureLow(): # Use heartbeat style.
            
            if robot.shooter.shooting and robot.shooter.atGoal: 
                if robot.revolver.sequenceEngaged: 
                    robot.ledsystem.colorOneHeartbeat() # Shooting!
                else:
                    robot.ledsystem.colorTwoHeartbeat() # Ready to shoot! (Green heartbeat)
            
            elif robot.shooter.shooting: # Not at the goal yet.
                robot.ledsystem.whiteHeartbeat()
                
            elif robot.intake.intaking: # 
                robot.ledsystem.blueHeartbeat()
                
            else:
                robot.ledsystem.redHeartbeat() # Compressor should be running, because we ain't shooting. Intake will mask the compressor running however.
                
        else:
            
            if robot.shooter.shooting and robot.shooter.atGoal:
                if robot.revolver.sequenceEngaged:
                    robot.ledsystem.colorOneStrobe() # Shooting!
                else:
                    robot.ledsystem.setGreen() # Ready to shoot!
            
            elif robot.shooter.shooting:
                robot.ledsystem.setWhite()
                
            elif robot.intake.intaking:
                robot.ledsystem.setBlue()
                
            else:
                robot.ledsystem.rainbowLava() # The default, good to go setting.
        
    def end(self):
        robot.ledsystem.off()
