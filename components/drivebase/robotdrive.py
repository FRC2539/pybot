import wpilib
import math

import csv
import os

from magicbot import tunable

from controller import logicalaxes

from components.drivebase.drivevelocities import TankDrive

from ctre import NeutralMode, FeedbackDevice, TalonFXControlMode
from rev import ControlType

class RobotDrive:

    robotdrive_motors: list

    velocityCalculator: object # Establishes drive

    build: object

    useActives: list

    rumble: bool

    bot: object

    #def __init__(self):     # NOTE: Be careful with this new init, as I added it after running it on a robot. It passes tests though, so we should be "gucci". Also note that you cannot access VI stuff in __init__.

    def assignFuncs(self):
        # Assigns functions that are motor controller specific

        if self.bot:
            self.move = self.falconMove
            self.resetPID = self.falconResetPID
            self.getPositions = self.falconGetPosition
            self.setPositions = self.falconSetPositions

        else:
            self.move = self.neoMove
            self.resetPID = self.neoResetPID
            self.getPositions = self.neoGetPosition
            self.setPositions = self.neoSetPositions

    def prepareToDrive(self):
        self.assignFuncs()

        self.resetPID()

        self.lastInputs = None

        self.rumble = False

        self.build.setDualRumble() # TEMPORARY!!!

        self.useActives = self.velocityCalculator.configureFourTank(self.robotdrive_motors)

        self.timer = wpilib.Timer()
        self.timer.start()

        self.firstSave = True

        self.folder = '/home/lvuser/py/components/drivebase'

    def stop(self): # Compatible for both drivebases

        for motor in self.useActives:
            motor.stopMotor()

    def recordDataToCSV(self):
        #for index, motor in enumerate(self.robotdrive_motors):
                #self.recordData[0].append(index)
                #self.recordData[1].append(motor.getEncoder().getVelocity())
                #self.recordData[2].append(motor.getOutputCurrent())
                #self.recordData[3].append(motor.getBusVoltage())
                #self.recordData[4].append(self.timer.get())
        #print(self.recordData)
        if self.firstSave:
            with open(self.folder +'/' + 'data.csv', 'w', newline='') as firstfile:
                print('first write')
                self.writer = csv.writer(firstfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_ALL, lineterminator='\n')
                for index, motor in enumerate(self.robotdrive_motors):
                    self.writer.writerow(['Motor: ' + str(index)] + ['RPM: ' + str((motor.getEncoder()).getVelocity())] + ['Amps: ' + str(motor.getOutputCurrent())] + ['Bus Volts: ' + str(motor.getBusVoltage())] + ['Time (s): ' + str(self.timer.get())])
                self.firstSave = False
        else:
            with open(self.folder +'/' + 'data.csv', 'a', newline='') as file:
                print('writing')
                self.writer = csv.writer(file, delimiter='\t', quotechar='|', quoting=csv.QUOTE_ALL, lineterminator='\n')

                for index, motor in enumerate(self.robotdrive_motors):
                    self.writer.writerow(['Motor: ' + str(index)] + ['RPM: ' + str((motor.getEncoder()).getVelocity())] + ['Amps: ' + str(motor.getOutputCurrent())] + ['Bus Volts: ' + str(motor.getBusVoltage())] + ['Time (s): ' + str(self.timer.get())])

            #for id_, vel, cur, volt, time in zip(self.recordData[0], self.recordData[1], self.recordData[2], self.recordData[3], self.recordData[4]):
                #self.writer.writerow(['Motor: ' + str(id_)] + ['RPM: ' + str(vel)] + ['Amps: ' + str(cur)] + ['Bus Volts: ' + str(volt)] + ['Time (s): ' + str(time)])


    def neoMove(self):
        print('running')
        y = self.build.getY() * -1 # invert the y-axis
        rotate = self.build.getRotate() * 0.85
        #if [y, rotate] == self.lastInputs: # I hope this doesn't stop the entire drive lol
            #return

        speeds = self.velocityCalculator.getSpeedT(
                                        y=float(y),
                                        rotate=float(rotate)
                                            )

        for speed, motor in zip(speeds, self.useActives):
            motor.set(speed)

        #self.recordDataToCSV()

        #self.lastInputs = [y, rotate]

    def falconMove(self):
        y = self.build.getY() * -1
        rotate = self.build.getRotate()

        if [y, rotate] == self.lastInputs: # I hope this doesn't stop the entire drive lol
            return

        speeds = self.velocityCalculator.getSpeedT(
                                        y=float(y),
                                        rotate=float(rotate)
                                            )

        for speed, motor in zip(speeds, self.useActives):
            motor.set(TalonFXControlMode.PercentOutput, speed)

        self.lastInputs = [y, rotate]

    def falconGetPosition(self):
        positions = []
        for motor in self.useActives:
            positions.append(motor.getSelectedSensorPosition())

        return positions

    def neoGetPosition(self):
        positions = []
        for motor in self.useActives:
            positions.append(motor.getEncoder().getPosition())

        return positions # Returns position in rotations TODO: Need to find unit that the talon and max share to ease calculations

    def falconSetPositions(self, positions):
        for motor, position in zip(self.useActives, positions):
            motor.set(TalonFXControlMode.MotionMagic, position) # motion magic works because of config above.

    def neoSetPositions(self, positions):
        for motor, position, in zip(self.useActives, positions):
            motor.getPIDController().setReference(position, ControlType.kPosition, 0, 0)

    def resetPosition(self):
        for motor in self.useActives:
            motor.setQuadraturePosition(0)

    def getAveragePosition(self, targets):
        error = 0
        for motor, target in zip(self.useActives, targets):
            error += abs(target - motor.getSelectedSensorPosition())

        return error

    def inchesToTicks(self, distance): #distance -> inches!
        # First does the wheel rotations necessary by dividing the distance by wheel the circumference. Takes this and multiplies by required ticks for one rotation (250)
        return (distance / (math.pi * 6)) * 250

    def falconResetPID(self): # Finalize both PID sets and set it up for nt values, separate for each bot
        for motor in self.useActives:
            motor.configClosedloopRamp(0, 0)
            for profile in range(2):
                motor.config_kP(profile, 1, 0)
                motor.config_kI(profile, 0.001, 0)
                motor.config_kD(profile, 31, 0)
                motor.config_kF(profile, 0.7, 0)
                motor.config_IntegralZone(profile, 30, 0)

    def neoResetPID(self):
        for motor in self.useActives:
            motor.setClosedLoopRampRate(0.15)
            controller = motor.getPIDController()

            for profile in range(2):
                controller.setP(1, profile)
                controller.setI(0.001, profile)
                controller.setD(31, profile)
                controller.setFF(0.7, profile)
                controller.setIZone(30, profile)
                controller.setOutputRange(-1, 1, profile)

    def execute(self):
        # Functions as a default for a low level (kinda)
        self.move()

