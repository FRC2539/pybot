import os.path
import pickle
import os

import robot

import pathfinder as pf

import wpilib

def run():
    if wpilib.RobotBase.isSimulation():
        print('\n\n\n RAN SIMULATION\n\n\n')
        try:
            os.remove('/home/coder/code/pybot/subsystems/trajectory.pickle')
        except(FileNotFoundError, MemoryError, FileExistsError):
            pass

        pdfPoints = [pf.Waypoint(0, 0, 0), pf.Waypoint(1, -5, 0), pf.Waypoint(3, -7, 0)]

        info, trajectory = pf.generate(pdfPoints, pf.FIT_HERMITE_CUBIC, pf.SAMPLES_HIGH,
                                        dt=0.008,
                                        max_velocity=10.0,
                                        max_acceleration=1.0,
                                        max_jerk=10.0
                                        )

        with open('/home/coder/code/pybot/subsystems/trajectory.pickle', 'w+b') as fp:
            pickle.dump(trajectory, fp)

    else:
        if os.path.getsize('/home/lvuser/py/tests/trajectory.pickle') > 0:
            with open('/home/lvuser/py/tests/trajectory.pickle', 'rb') as fp:
                trajectory = pickle.load(fp)
        else:
            raise IndexError('File is empty')
