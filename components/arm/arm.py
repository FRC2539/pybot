class Arm:
    arm_motor: object

    lowerLimit: object

    arm_encoder: object

    arm_pidcontroller: object

    def prepareArm(self):
        self.arm_motor.setClosedLoopRampRate(1)

        self.arm_motor.setInverted(True)

        self.upperLimit = 70.0
        self.startPos = 105.0

        self.arm_encoder.setPosition(self.startPos)

        self.finalPos = self.getPosition()

    def resetEncoder(self):
        self.arm_encoder.setPosition(0.0)
        self.arm_motor.setEncPosition(0.0)

    def getPosition(self):
        return self.arm_encoder.getPosition()

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
        self.stop()
