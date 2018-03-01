from custom.config import Config

defaults = {
    'DriveTrain/maxSpeed': 950,
    'DriveTrain/normalSpeed': 600,
    'DriveTrain/preciseSpeed': 150,
    'DriveTrain/ticksPerInch': 750,
    'DriveTrain/width': 29.5,
    'Autonomous/robotLocation': 'L',
    'Autonomous/switch': 'easy',
    'Autonomous/scale': 'easy',
    'Elevator/ground': 0,
    'Elevator/switch': 3000,
    'Elevator/portal': 2000,
    'Elevator/scale': 5000,
    'Elevator/exchange': 500
}

def fakeConfig(self):
    global defaults

    if self.key in defaults:
        return defaults[self.key]

    return self._getValue()

Config._getValue = Config.getValue
Config.getValue = fakeConfig
Config.__pos__ = fakeConfig

from wpilib.driverstation import DriverStation
DriverStation.getGameSpecificMessage = lambda x=0: 'LRL'
