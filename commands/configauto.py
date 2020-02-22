from networktables import NetworkTables

def init():
    table = NetworkTables.getTable('Autonomous')

    autoNames = [
        'Eat Beans', 'Inner Power Port :)',
        'Inner Power Port But More 8D',' SkSkSkirt off the init line',
        'REEEEEEEEEE','shootie trench'
                 ]
    autoString = ''

    for auto in autoNames:
        autoString += str(auto + '$')

    autoString = autoString[:-1]

    table.putString('autoModes', autoString)
