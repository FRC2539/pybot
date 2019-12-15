class Arm:
    arm_motor: object

    lowerLimit: object

    def prepareArm(self):
        self.encoder = self.arm_motor.getEncoder()
        self.PIDcont = self.arm_motor.getPIDController()

        self.arm_motor.setClosedLoopRampRate(1)

        self.arm_motor.setInverted(True)

        self.upperLimit = 70.0
        self.startPos = 105.0

        self.encoder.setPosition(self.startPos)

        self.finalPos = self.getPosition()


    def getPosition(self):
        return self.encoder.getPosition()

    def atBottom(self):
        return (not self.lowerLimit.get()) or (self.getPosition() <= 0)

    def atTop(self):
        return (self.getPosition() >= self.upperLimit)

    def armUp(self):
        if not self.atTop():
            self.arm_motor.set(0.8)
        else:
            self.stop()

        self.finalPos = self.getPosition()

    def armDown(self):
        if not self.atBottom():
            self.arm_motor.set(-0.8)
        else:
            self.resetEncoder()
            self.stop()

        self.finalPos = self.getPosition()

    def stop(self):
        self.arm_motor.stopMotor()

    def execute(self):
        pass
