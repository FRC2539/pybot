#!/usr/bin/env python3

import wpilib.command
wpilib.command.Command.isFinished = lambda x: False

from commandbased import CommandBasedRobot
from wpilib._impl.main import run
from wpilib import RobotBase

from custom import driverhud
import controller.layout
import subsystems
import shutil, sys

from subsystems.cougarsystem import CougarSystem
from wpilib.command import Subsystem

from subsystems.monitor import Monitor as monitor
from subsystems.drivetrain import DriveTrain as drivetrain
from subsystems.revolver import Revolver as revolver
from subsystems.balllauncher import BallLauncher as balllauncher
from subsystems.shooter import Shooter as shooter
from subsystems.intake import Intake as intake
from subsystems.pneumatics import Pneumatics as pneumatics
from subsystems.ledsystem import LEDSystem as ledsystem
from subsystems.hood import Hood as hood
from subsystems.turret import Turret as turret
from subsystems.limelight import Limelight as limelight
from subsystems.climber import Climber as climber

class KryptonBot(CommandBasedRobot):
    '''Implements a Command Based robot design'''

    def robotInit(self):
        '''Set up everything we need for a working robot.'''
        if RobotBase.isSimulation():
            import mockdata

        self.subsystems()
        controller.layout.init()
        driverhud.init()

        from commands.startupcommandgroup import StartUpCommandGroup
        StartUpCommandGroup().start()

    def autonomousInit(self):
        '''This function is called each time autonomous mode starts.'''

        # Send field data to the dashboard
        driverhud.showField()

        # Schedule the autonomous command
        auton = driverhud.getAutonomousProgram()
        auton.start()
                
        driverhud.showInfo("Starting %s" % auton)

    def disabledInit(self):
        self.captureDisbaleVars()

    def handleCrash(self, error):
        super().handleCrash()
        driverhud.showAlert('Fatal Error: %s' % error)

    def captureDisbaleVars(self):
        writeThese = []
        vars = globals()
        module = sys.modules['robot']

        for key, var in vars.items():
            try:
                if issubclass(var, CougarSystem) and var is not CougarSystem:
                    object_ = getattr(module, key)
                    for data in object_.writeOnDisable:
                        writeThese.append([data[0], data[1], eval('object_' + str(data[2]))])

            except(TypeError):
                continue

        try:
            with open('/home/lvuser/py/data.txt', 'w') as f:
                #print('len ' + str(writeThese))
                for listitem in writeThese:
                    f.write(str(listitem) + '\n')
        except(FileNotFoundError):
            pass

    def checkDrive(self):
        if robotselection.competitionrobot.status:

            robotselection.competitionrobot.checking = True

            print('\n\n\nAlsoGood\n\n\n')

            for key, var in globals().items():
                if var == drivetrain:
                    setattr(sys.modules['robot'], key, var())

    @classmethod
    def subsystems(cls):
        vars = globals()
        module = sys.modules['robot']

        for key, var in vars.items():
            try:
                if issubclass(var, Subsystem) and var is not Subsystem and var is not CougarSystem:
                    try:
                        setattr(module, key, var())
                    except TypeError as e:
                        raise ValueError(f'Could not instantiate {key}') from e
            except TypeError:
                pass

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)

    run(KryptonBot)
