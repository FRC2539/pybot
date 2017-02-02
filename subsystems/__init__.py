'''
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
'''

from wpilib.robotbase import RobotBase

from .drivetrain import DriveTrain
from .monitor import Monitor
from .shooter import Shooter
from .pickup import Pickup
from .climber import Climber

drivetrain = None
monitor = None
shooter = None
pickup = None
climber = None

def init():
    '''
    Creates all subsystems. You must run this before any commands are
    instantiated. Do not run it more than once.
    '''
    global drivetrain, monitor, shooter, pickup, climber

    '''
    The default tests that are run before deploy call startCompetition multiple
    times, breaking the normal flow, so we test to see if we're running in a
    test by checking isSimulation.
    '''
    if drivetrain is not None and not RobotBase.isSimulation():
        raise RuntimeError('Subsystems have already been initialized')

    drivetrain = DriveTrain()
    monitor = Monitor()
    shooter = Shooter()
    pickup = Pickup()
    climber = Climber()
