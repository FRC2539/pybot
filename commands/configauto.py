from networktables import NetworkTables

def init():
    table = NetworkTables.getTable('Autonomous')

    autoNames = ['Eat Beans', 'Inner Power Port :)', 'SkSkSkirt off the init line']
    autoString = ''

    for auto in autoNames:
        autoString += str(auto + '$')

    autoString = autoString[:-1]

    table.putString('autoModes', autoString)
