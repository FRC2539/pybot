class Elevator:

    elevator_motor: object

    lowerlimit: object

    elevator_encoder: object

    elevator_pidcontroller: object

    def prepareElevator(self):
        self.elevator_motor.setClosedLoopRampRate(0.5)

        self.upperLimit = 145.0

    def stop(self):
        self.elevator_motor.stopMotor()

    def getPosition(self):
        return self.elevator_encoder.getPosition()

    def elevatorUp(self):
        if not self.getPosition() >= self.upperLimit:
            self.elevator_motor.set(1.0)

        else:
            self.stop()
            self.elevator_encoder.setPosition(self.upperLimit)

    def elevatorDown(self):
        if (not self.lowerlimit.get()) or self.getPosition() <= 0.0:
            self.stop()
            self.elevator_encoder.setPosition(0.0)
        else:
            self.elevator_motor.set(-1.0)

    def hold(self):
        if not (not self.lowerlimit.get()) or (self.getPosition() <= 0.0): # Checks to see if position is at zero.
            self.elevator_encoder.setPosition(self.getPosition())
        else:
            self.stop()

    def default(self):
        # ADD THIS TO EVERYONE
        self.stop()

    def execute(self):
        pass
        #self.hold() # Hopefully this will maintain a strong position when not at zero. Otherwise it will stop it.
