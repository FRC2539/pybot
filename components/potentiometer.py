from ctre import ControlMode, FeedbackDevice

class Potentiometer:

    potentiometer: object
    potentiometerTalon: object

    potentiometerForward: object
    potentiometerReverse: object

    potentiometerOne: object
    potentiometerTwo: object
    potentiometerThree: object
    potentiometerFour: object

    def setup(self):
        #self.potentiometerTalon.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Absolute, 0, 0)
        self.enc = self.potentiometerTalon.getEncoder()

    def getReading(self):
        return self.potentiometer.get()

    def getEncoderReadings(self):
        print('port six ' + str(self.potentiometerOne.get()))
        print('port seven ' + str(self.potentiometerTwo.get()))
        print('port eight ' + str(self.potentiometerThree.get()))
        print('port nine ' + str(self.potentiometerFour.get()))

    def execute(self):
        print('position ' + str(self.enc.getPosition()))
        if self.potentiometerForward.get() and self.potentiometerReverse.get():
            self.potentiometerTalon.stopMotor()
        elif not self.potentiometerReverse.get():
            self.potentiometerTalon.set(float(self.getReading()))
        else:
            self.potentiometerTalon.set(float(self.getReading()) * -1)
