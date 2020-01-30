class Generator:

    def __init__(self):
        self.initialize()
        while not self.isFinished():
            self.execute()
            yield
        self.end()

        self.__del__()

    def initialize(self):
        print('No i ran')
        pass

    def execute(self):
        pass

    def isFinished(self):
        return True # change as needed

    def interrupted(self):
        pass # probably will never use

    def end(self):
        pass
