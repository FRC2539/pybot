from ctre import ControlMode

class Potentiometer:

    potentiometer: object
    potentiometerTalon: object

    potentiometerForward: object
    potentiometerReverse: object

    def __init__(self):
        self.speed = None

    def getReading(self):
        return self.potentiometer.get()

    def execute(self):
        if self.potentiometerForward.get() and self.potentiometerReverse.get():
            self.potentiometerTalon.stopMotor()
        elif not self.potentiometerReverse.get():
            self.potentiometerTalon.set(ControlMode.PercentOutput, float(self.getReading()))
        else:
            self.potentiometerTalon.set(ControlMode.PercentOutput, float(self.getReading()) * -1)
