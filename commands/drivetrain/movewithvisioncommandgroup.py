from wpilib.command import CommandGroup
from custom.config import Config
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.network.alertcommand import AlertCommand

import commandbased.flowcontrol as fc

import robot

class MoveWithVisionCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Move With Vision')

        self.requires(robot.drivetrain)

        def hasRocketTape():
            if Config('cameraInfo/tapeFound', False):
                return 1
            else:
                return 0

        def noRocketTape():
            if Config('cameraInfo/tapeFound', False):
                return 0
            else:
                return 1

        def distanceToTape():
            return Config('cameraInfo/distanceToTape', -1)

        def tapeX():
            return Config('cameraInfo/tapeX', -1)


        def turnRightTwenty():
            angle = 0
            while angle <= 20:
                if hasRocketTape():
                    print('ISEEEEEDA LIGHNTTTTT')
                    return 1
                else:
                    self.addSequential(TurnCommand(2))
                    #self.addSequential(AlertCommand('Looping in right'))
                    angle += 2
                    continue

            return 0

        def turnLeftTwenty():
            angle = 0
            while angle <= 20:
                if hasRocketTape():
                    return 1
                else:
                    self.addSequential(TurnCommand(-2))
                    print('looping in left')
                    angle += 2
                    continue
            return 0

        @fc.WHILE(hasRocketTape)
        def startWithTape(self):
            distance = distanceToTape()
            newDistance = distance - 8
            self.addSequential(MoveCommand(newDistance))

        @fc.WHILE(noRocketTape)
        def findRocketTape(self):
            print(' i dum robot y no see la tapeee')
            turnRightTwenty()
            foundR = turnRightTwenty()
            print('The robort has no idea what its doing')
            if foundR:
                pass

            elif not foundR:
                self.addSequential(TurnCommand(-20))
                foundL = turnLeftTwenty()
                print('OOOOOOOFFFFFFF')

            elif not foundL or not foundR:
                self.addSequential(TurnCommand(20))
                print('I did not find it!')

            @fc.WHILE(hasRocketTape)
            def moveToTape(self):
                distance = distanceToTape()
                newDistance = distance - 8
                self.addSequential(MoveCommand(newDistance))
                print('Done')
