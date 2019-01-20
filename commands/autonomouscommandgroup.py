from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from custom.config import Config
from networktables import NetworkTables
from commands.network.alertcommand import AlertCommand
from commands.drivetrain.turntocommand import TurnToCommand
import commandbased.flowcontrol as fc

#from commands.drivetrain.turncommand import TurnCommand
#from commands.drivetrain.movecommand import MoveCommand
#from commands.drivetrain.setspeedcommand import setSpeedCommand

def noCargo():
    #NetworkTables.initialize(server='roborio-2539-frc.local')
    if Config('cameraInfo/cargoFound', False):
        return False
    else:
        return True


class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        print('auto on')
        #self.addSequential(TurnToCommand(5))

        NetworkTables.initialize(server='roborio-2539-frc.local')

        #hasCargo = Config('cameraInfo/cargoFound', False)
        #self.addSequential(AlertCommand('Cargo: %s' % str(hasCargo)))
        #print(str(hasCargo))

        @fc.WHILE(noCargo)
        def lookingforcargo(self):
            print('looking for cargo')

        print('after while')

        '''
        while hasCargo == False:
            #looking for cargo
            print('looking for cargo')

            while hasCargo:
                #found cargo
                print('found cargo')

                #self.addSequential(AlertCommand('Distance to cargo: %s' % float(distanceToCargo)))
                #self.addSequential(AlertCommand('X alert: %s' % float(Config('cameraInfo/cargoX', -1))))
                cargoX = Config('cameraInfo/cargoX', -1)
                if cargoX < 325:
                    #TurnCommand(-5)
                    self.addSequential(AlertCommand('Cargo Location Right: %s' % float(cargoX)))
                    #self.addSequential(TurnCommand(-1))
                    #print('')

                if cargoX > 325:
                    #TurnCommand(5)
                    self.addSequential(AlertCommand('Cargo Location Left: %s' % float(cargoX)))
                    #self.addSequential(TurnCommand(1))
                    #print('')

        #@fc.WHILE(noCargo)
        #def lookingforcargo(self):
        #    print('looking for cargo')
        '''


        '''
        distanceToCargo = Config('cameraInfo/distanceToCargo', None)
        cargoX = Config('cameraInfo/cargoX', -1)
        #self.addSequential(AlertCommand('Distance to cargo: %s' % float(distanceToCargo)))
        #self.addSequential(AlertCommand('Cargo:
        '''
        '''
        while hasCargo:
            #self.addSequential(AlertCommand('Distance to cargo: %s' % float(distanceToCargo)))
            #self.addSequential(AlertCommand('X alert: %s' % float(Config('cameraInfo/cargoX', -1))))
            cargoX = Config('cameraInfo/cargoX', -1)
            if cargoX < 325:
                #TurnCommand(-5)
                self.addSequential(AlertCommand('Cargo Location Right: %s' % float(cargoX)))
                #self.addSequential(TurnCommand(-1))
                print('')

            if cargoX > 325:
                #TurnCommand(5)
                self.addSequential(AlertCommand('Cargo Location Left: %s' % float(cargoX)))
                #self.addSequential(TurnCommand(1))
                print('')
         %s' % Config('cameraInfo/cargoX', -1)))

            print('cargoX-'+str(cargoX))

            if int(cargoX) < 325:
                #TurnCommand(-5)
                #self.addSequential(AlertCommand('Cargo Location Right: %s' % float(cargoX)))
                self.addSequential(TurnCommand(-1))


            if int(cargoX) > 325:
                #TurnCommand(5)
                #self.addSequential(AlertCommand('Cargo Location Left: %s' % float(cargoX)))
                self.addSequential(TurnCommand(1))
            '''

        #distanceToCargo = Config('cameraInfo/distanceToCargo', None)

        #cargoX = getCargoX

        #print(str(hasCargo))
        #if hasCargo:
            #self.addSequential(AlertCommand('Distance to cargo: %s' % float(distanceToCargo)))
            #self.addSequential(AlertCommand('X alert: %s' % float(cargoX)))

            #Turn robot according to cargo location.
            #i = 0
            #@fc.IF(lambda: i <1500)
            #def checkI(self):
            #    self.addSequential(AlertCommand('i: %s' % int(i))
            #    i += 1

        '''

            while i < 15000:
                self.addSequential(AlertCommand('i: %s' % int(i))
                if int(cargoX) < 325:
                    #TurnCommand(-5)
                    #self.addSequential(AlertCommand('Cargo Location Right: %s' % float(cargoX)))
                    self.addSequential(TurnCommand(-5))
                    i += 1

                if int(cargoX) > 325:
                    #TurnCommand(5)
                    #self.addSequential(AlertCommand('Cargo Location Left: %s' % float(cargoX)))
                    self.addSequential(TurnCommand(5))
                    i += 1
            '''
