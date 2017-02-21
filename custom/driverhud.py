'''
The DriveHUD displays useful information on the driver dashboard, and can read
information from the dashboard and provide it to the program.
'''

from wpilib.sendablechooser import SendableChooser
from wpilib.smartdashboard import SmartDashboard
from wpilib.command import Scheduler

from wpilib.command import InstantCommand
from commands.drive.movecommand import MoveCommand
from commands.gear.startwithgearcommandgroup import StartWithGearCommandGroup

autonChooser = None

from wpilib.robotbase import RobotBase

def init():
    '''
    This function must be called from robotInit, but not before the subsystems
    have been created. Do not call it more than once.
    '''

    global autonChooser

    if autonChooser is not None and not RobotBase.isSimulation():
        raise RuntimeError('Driver HUD has already been initialized')

    '''
    Add commands to the autonChooser to make them available for selection by the
    driver. It is best to choose a command that will not break anything if run
    at the wrong time as the default command.
    '''
    autonChooser = SendableChooser()
    autonChooser.addDefault('Do Nothing', InstantCommand('Do Nothing'))
    autonChooser.addObject('Cross Baseline', MoveCommand(84))
    autonChooser.addObject('Hang Gear', StartWithGearCommandGroup())

    SmartDashboard.putData('Autonomous Program', autonChooser)

    '''Display all currently running commands.'''
    SmartDashboard.putData('Active Commands', Scheduler.getInstance())


def getAutonomousProgram():
    '''
    Return the autonomous program as selected on the dashboard. It is up to the
    calling scope to start and cancel the command as needed.
    '''

    global autonChooser

    if autonChooser is None:
        raise RuntimeError('Cannot select auton before HUD initializiation')

    return autonChooser.getSelected()


def showAlert(msg, type='Alerts'):
    '''Display a text notification on the dashboard.'''

    messages = SmartDashboard.getStringArray(type, [])
    messages.append(msg)
    SmartDashboard.putStringArray(
        type,
        messages
    )


def showInfo(msg):
    showAlert(msg, 'Info')
