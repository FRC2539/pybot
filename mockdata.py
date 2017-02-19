from custom.config import Config

defaults = {
    '/DriveTrain/maxSpeed': 950,
    '/DriveTrain/manualMaxSpeed': 100,
    '/DriveTrain/preciseSpeed': 150,
    '/Shooter/speed': 100,
    '/Autonomous/robotLocation': 0
}

def fakeConfig(self):
    global defaults

    if self.key in defaults:
        return defaults[self.key]

    return self._getValue()

Config._getValue = Config.getValue
Config.getValue = fakeConfig
