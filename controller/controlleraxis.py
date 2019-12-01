class ControllerAxis:
    def __init__(self, controller, id, isInverted):
        if isInverted:
            self.get = lambda: -1 * controller.getRawAxis(id)
            
        else:
            self.get = lambda: controller.getRawAxis(id)
