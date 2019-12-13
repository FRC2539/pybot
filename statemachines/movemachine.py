from magicbot import StateMachine, state

from components.drivebase.robotdrive import RobotDrive

class MoveStateMachine(StateMachine):
    robotdrive: RobotDrive

    tolerance: int

    def moveMachineStart(self, distance):
        # Call from the teleop to begin machine.
        self.distance = distance

        self.robotdrive.resetPosition()

        self.engage()

    @state(first=True)
    def prepareToMove(self):
        difference = self.robotdrive.inchesToTicks(self.distance)
        self.targetPositions = []

        swap = 1 # Swaps the value for each side.

        for position in self.robotdrive.getPosition():
            self.targetPositions.append(position + difference * swap)
            swap *= -1

        print('pos ' + str(self.robotdrive.getPosition()))
        print('going ' + str(self.targetPositions))


        self.robotdrive.setPositions(self.targetPositions)

        self.next_state(self.wait) # may want this to be next_state_now...

    @state
    def wait(self): #This will wait to end the state machine until the position has been set.
        if self.robotdrive.getAveragePosition(self.targetPositions) <= abs(self.tolerance):
            self.robotdrive.stop()
            self.done()


    print('moved')
