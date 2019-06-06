from wpilib.command.instantcommand import InstantCommand

class ToggleLayoutCommand(InstantCommand):

    def __init__(self):
        import controller.layout

        super().__init__('Toggle Layout')

    def initialize(self):
        from custom import driverhud, config

        from networktables import NetworkTables as nt

        value = config.Config('/DriveTrain/Layout', 0)

        table = nt.getTable('DriveTrain')

        if int(value) == 0:
            value = 1
            driverhud.showAlert('Selected Secondary Layout! Restart Code to Take Action!')
        else:
            value = 0
            driverhud.showAlert('Selected Primary Layout! Restart Code to Take Action!')

        table.putNumber('Layout', value)
