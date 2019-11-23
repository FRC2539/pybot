import os.path
import pickle
import os

import robot

import pathfinder as pf

import wpilib

def run():
    pickleFile = os.path.join(os.path.dirname(__file__), 'trajectory.pickle')

    if not wpilib.RobotBase.isSimulation():
        with open(os.path.join(os.path.dirname(__file__), 'trajectory.pickle'), 'rb') as fp:
            trajectory = pickle.load(fp)

    else:
        if os.path.isfile(os.path.join(os.path.dirname(__file__), 'trajectory.pickle')):
            print('FILE FOUND...DELETING')
            os.remove(os.path.join(os.path.dirname(__file__), 'trajectory.pickle'))

        pdfPoints = [pf.Waypoint(0, 0, 0), pf.Waypoint(1, 7, 0)]

        info, trajectory = pf.generate(pdfPoints, pf.FIT_HERMITE_CUBIC, pf.SAMPLES_HIGH,
                                        dt=0.05,
                                        max_velocity=10.0,
                                        max_acceleration=.0001,
                                        max_jerk=20.0
                                        )

        with open(pickleFile, 'wb') as fp:
            pickle.dump(trajectory, fp)
