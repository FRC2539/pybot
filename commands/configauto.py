from networktables import NetworkTables

def init():
    table = NetworkTables.getTable('Autonomous')


    autoNames = ['Move Test',
                 'Move Test 2',
                ]

    autoString = ''

    for auto in autoNames:
        autoString += str(auto + '$')

    autoString = autoString[:-1]

    table.putString('autoModes', autoString)
