import wpilib
import ports

from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

from .drivevelocities import TankDrive, MecanumDrive

from controller import logicalaxes

class RobotDrive:
    # This class acts as a subsystem (component)
    frontLeftMotor = WPI_TalonSRX
    frontRightMotor = WPI_TalonSRX
    backLeftMotor = WPI_TalonSRX
    backRightMotor = WPI_TalonSRX
    def __init__(self, _type='tank'):
        self.fallbackDrive = 'tank' # Configure this here only! (maybe nt value later)

        self.motors = [
                       self.frontLeftMotor,
                       self.frontRightMotor,
                       self.backLeftMotor,
                       self.backRightMotor
                       ]
        print(frontLeftMotor)
        for motor in self.motors:
            motor.setNeutralMode(2)
            motor.setSafetyEnabled(False)
            motor.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)
            # Add in motor specifications here               

        '''
        Deciding configuration is set up below. Add, edit, and remove
        carefully!
        '''

        unselected = True # Forces the lower while loop
        
        while unselected:

            if str(_type).lower() == 'tank':
                self.drivetrain = TankDrive(rotateModifier=0.8) # Add desired modifiers here!
                self.activeMotors = self.drivetrain.configureFourTank(self.motors)
                self.driveRobot = self.driveRobotTank # Configures function for a tank robot

                print('\nTANK Drive successfully set!\n')
                
                unselected = False # probably don't need unselected and break statements... investigate!
                break 

            elif str(_type).lower() == 'mecanum':
                self.drivetrain = MecanumDrive(rotateModifier=0.8) # Add desired modifiers here!
                self.activeMotors = self.drivetrain.configureMecanum(self.motors)
                self.driveRobot = self.driveRobotMecanum # Configures function for a mecanum robot

                print('\nMECANUM Drive successfully set!\n')

                unselected = False
                break

            else:
                raise Exception('\nUNKNOWN CONFIGURATION!\n\nPLEASE ENTER \'tank\' OR \'mecanum\'!')
                print('\n...Returning to preset fallback drive: ' + self.fallbackDrive + '...')
                _type = self.fallbackDrive
                continue
                


        #NOTE: Add NT value for configured dt!

        self.drivetrain.checkParameters()

    def stop(self):
        for motor in self.motors:
            motor.set(0.0)

    def registerAxes(self): # Called before drive method
        logicalaxes.registerAxis('driveX')
        logicalaxes.registerAxis('driveY')
        logicalaxes.registerAxis('driveRotate')
        
    def driveRobotTank(self):
        self.moveTank(
                      logicalaxes.driveX.get(),
                      logicalaxes.driveY.get(),
                      logicalaxes.driveRotate.get()
                      )
        
    def moveTank(self, x, y, rotate):
        # Given axises
        speeds = self.drivetrain.getSpeedT(x, y, rotate)

        print(speeds)
        print(self.activeMotors)
        print(ports.DrivetrainPorts.FrontLeftMotor)
        
        for motor, velocity in zip(self.activeMotors, speeds):
            motor.set(ControlMode.PercentOutput, float(velocity))

    def driveRobotMecanum(self):
        self.moveMecanum(
                      logicalaxes.driveX.get(),
                      logicalaxes.driveY.get(),
                      logicalaxes.driveRotate.get()
                      )
        
    def moveMecanum(self, x, y, rotate):
        speeds = self.drivetrain.getSpeedM(x, y, rotate)
    
        for motor, velocity in zip(self.activeMotors, speeds):
            motor.set(ControlMode.PercentOutput, velocity)
