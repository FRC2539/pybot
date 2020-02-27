from networktables import NetworkTables

def init():
    table = NetworkTables.getTable('Autonomous')


    autoNames = ['3 Ball Auto',
                 '3 Ball Move First',
                 '5 Ball Auto',
                 '6 Ball Auto',
                ]

    autoString = ''

    for auto in autoNames:
        autoString += str(auto + '$')

    autoString = autoString[:-1]

    table.putString('autoModes', autoString)
