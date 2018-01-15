from custom.config import Config

defaults = {
    '/DriveTrain/maxSpeed': 950,
    '/DriveTrain/normalSpeed': 600,
    '/DriveTrain/preciseSpeed': 150,
    '/DriveTrain/ticksPerInch': 750,
    '/Shooter/speed': 100,
    '/Autonomous/robotLocation': 0,
    '/Gear/HandOffDistance': 36
}

def fakeConfig(self):
    global defaults

    if self.key in defaults:
        return defaults[self.key]

    return self._getValue()

Config._getValue = Config.getValue
Config.getValue = fakeConfig
