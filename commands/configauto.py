from networktables import NetworkTables

def init():
    table = NetworkTables.getTable('Autonomous')

    autoNames = ['Eat Beans', 'Nom Nom']
    autoString = ''

    for auto in autoNames:
        autoString += str(auto + '$')

    autoString = autoString[:-1]

    table.putString('autoModes', autoString)
