import wpilib
import ports

from .debuggablesubsystem import DebuggableSubsystem

from rev import ControlType, CANSparkMax, MotorType

from rev.color import ColorSensorV3, ColorMatch

from networktables import NetworkTables as nt

class ColorWheel(DebuggableSubsystem):

    def __init__(self):
        super().__init__('Color Wheel')

        driverStation = nt.getTable("SmartDashboard")

        self.colorMatcher = ColorMatch()

        self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)
        self.colorWheelMotor = CANSparkMax(ports.ColorWheelPorts.motorID, MotorType.kBrushless)# WPI_TalonSRX(ports.ColorWheelPorts.motorID)
        self.colorWheelEncoder = self.colorWheelMotor.getEncoder()
        self.colorWheelController = self.colorWheelMotor.getPIDController()

        self.colorSensor.configureColorSensor(
            ColorSensorV3.ColorResolution.k18bit,
            ColorSensorV3.ColorMeasurementRate.k50ms
        ) # Tune these values as needed.

        self.colorWheelMotor.setInverted(False) # might need to change

        self.colorWheelController.setP(0.01, 0) # Dummy values from the falcon tester
        self.colorWheelController.setI(0, 0)
        self.colorWheelController.setD(0.1, 0)
        self.colorWheelController.setIZone(1, 0)
        self.colorWheelController.setFF(0.1, 0)

    def getColor(self):
        self.color = self.colorSensor.getColor()

        #print(self.color.red / self.color.green)

        #print('r ' + str(self.color.red))
        #print('b ' + str(self.color.blue))
        #print('g ' + str(self.color.green))

        if self.color.blue > self.color.green and self.color.blue > self.color.red:
            return 'b'
        elif self.color.red > self.color.green and self.color.red > self.color.blue:
            return 'r'
        elif self.color.red / self.color.green > 0.52:
            return 'y'
        else: #self.color.green > self.color.red and self.color.green > self.color.blue:
            return 'g'
        #self.firstStrength = max(self.colorCheck.keys())
        #self.secondStrength = max(self.colorCheck.remove(self.firstStrength))



    def reset(self):
        self.colorWheelMotor.setEncPosition(0.0)
        self.colorWheelEncoder.setPosition(0.0)

    def autoSpinWheel(self, val=9630): # This val is for the number of rotations; pass an argument for the set
        ''' Should be about 3.25 rotations of the color wheel '''
        # Need to add the offset based on direction to set the extra distance to get to the sensor.
        self.reset()
        self.colorWheelController.setReference(val, ControlType.kPosition, 0, 0) # Look at photos for calc, Ben.

    def stop(self):
        self.colorWheelMotor.stopMotor()

    def spinToSensor(self, val):
        # only use if already on that color.
        self.reset()
        self.colorWheelController.setReference(val, ControlType.kPosition, 0, 0) # DUMMY VALUE

    def spinClockwise(self):
        self.colorWheelMotor.set(0.9)

    def spinCClockwise(self):
        self.colorWheelMotor.set(-0.9)
