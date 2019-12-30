class CustomBuild:
    def __init__(self, controllerOne, controllerTwo):
        self.controllerUno = controllerOne
        self.controllerDos = controllerTwo

    ''' The following are for trigger bool statements '''
    def getRightTriggerDriver(self):
        if self.controllerUno.getTriggerAxis(1) > 0.05:
            return True
        else:
            return False

    def getLeftTriggerDriver(self):
        if self.controllerUno.getTriggerAxis(0) > 0.05:
            return True
        else:
            return False

    def getRightTriggerOp(self):
        if self.controllerDos.getTriggerAxis(1) > 0.05:
            return True
        else:
            return False

    def getLeftTriggerOp(self):
        if self.controllerDos.getTriggerAxis(0) > 0.05:
            return True
        else:
            return False
