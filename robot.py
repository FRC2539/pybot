import wpilib

import shutil, sys

class CleanRobot(wpilib.TimedRobot):
    
    def robotInit(self):
        '''Initializes robot code here'''
        pass
    
    def autonomousInit(self):
        pass
    
    def teleopInit(self):
        pass
    
    def handleCrash(self):
        super().handleCrash()
        ''' investigate '''
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)        
        
    wpilib.run(CleanRobot)
