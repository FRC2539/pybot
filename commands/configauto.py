from networktables import NetworkTables

def init():
    table = NetworkTables.getTable('Autonomous')

    autoNames = ['Simple Shoot', '', 'Shoot, Trench, Collect 5','Shoot, Trench, Collect 3, Shoot', 'REEEEEEEEEE','shootie trench' ]
    autoString = ''

    for auto in autoNames:
        autoString += str(auto + '$')

    autoString = autoString[:-1]

    table.putString('autoModes', autoString)
