import wpilib
import ports

from .debuggablesubsystem import DebuggableSubsystem

from rev import ControlType, CANSparkMax, MotorType

from rev.color import ColorSensorV3, ColorMatch

from networktables import NetworkTables as nt

class ColorWheel(DebuggableSubsystem):

    def __init__(self):
        super().__init__('Color Wheel')

        self.colorMatcher = ColorMatch()

        self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)
        self.colorWheelMotor = CANSparkMax(ports.ColorWheelPorts.motorID, MotorType.kBrushed)# WPI_TalonSRX(ports.ColorWheelPorts.motorID)

        self.wwMotor = CANSparkMax(ports.ColorWheelPorts.wwMotorID, MotorType.kBrushed)

        self.upPosition = 135 # real physical max is 180
        self.startPosition = 0

        self.colorSensor.configureColorSensor(
            ColorSensorV3.ColorResolution.k18bit,
            ColorSensorV3.ColorMeasurementRate.k50ms
        ) # Tune these values as needed.

        self.colorWheelMotor.setInverted(False) # might need to change

        #self.colorWheelController.setP(0.01, 0) # Dummy values from the falcon tester
        #self.colorWheelController.setI(0, 0)
        #self.colorWheelController.setD(0.1, 0)
        #self.colorWheelController.setIZone(1, 0)
        #self.colorWheelController.setFF(0.1, 0)

        self.colorWheelMotor.burnFlash()

    def getColor(self):
        self.color = self.colorSensor.getColor()
        print('r: ' + str(self.color.red))
        print('g: ' + str(self.color.green))
        print('b: ' + str(self.color.blue))
        print('ny: ' + str(self.color.red / self.color.green))

        if self.color.blue > (self.color.green - .18) and self.color.blue > self.color.red: # subtracts because there is more green in blue than blue lol.
            return 'b'
        #elif self.color.red > self.color.green and self.color.red > self.color.blue:
         #   return 'r'
        elif self.color.green - 0.25 > self.color.red and self.color.green > self.color.blue:
            return 'g'
        elif self.color.red / self.color.green < 0.65: # checks a highly-tuned ratio for current color since yellow isn't RGB and if you think it is you're an idiot.
            return 'y' #cough cough people who deleted Bens winch code cough cough
        else:
            return 'r'

    def reset(self):
        pass
        #self.colorWheelMotor.setEncPosition(0.0)
        #self.colorWheelEncoder.setPosition(0.0)

    def autoSpinWheel(self, val=9630): # This val is for the number of rotations; pass an argument for the set
        ''' Should be about 3.25 rotations of the color wheel '''
        # Need to add the offset based on direction to set the extra distance to get to the sensor.
        self.reset()
        #self.colorWheelController.setReference(val, ControlType.kPosition, 0, 0) # Look at photos for calc, Ben.

    def stop(self):
        self.colorWheelMotor.stopMotor()

    def spinToSensor(self, val):
        # only use if already on that color.
        self.reset()
        ##self.colorWheelController.setReference(val, ControlType.kPosition, 0, 0) # DUMMY VALUE



    def spinClockwise(self):
        self.colorWheelMotor.set(1)

    def spinCClockwise(self):
        self.colorWheelMotor.set(-1)

    def startSpin(self):
        self.wwMotor.set(0.8)

    def reverseSpin(self):
        self.wwMotor.set(-0.8)

    def stopRaise(self):
        self.wwMotor.stopMotor()

    def getAmp(self):
        return (self.wwMotor.getOutputCurrent())

    def stopOnImpact(self):
        return (self.wwMotor.getOutputCurrent() >= 13.0)
