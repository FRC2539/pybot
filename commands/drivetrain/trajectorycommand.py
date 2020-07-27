from wpilib.geometry import Pose2d, Rotation2d, Translation2d
from wpilib.trajectory import TrajectoryGenerator, TrajectoryConfig

def TrajectoryCommand(startXY: list, interiorWayPointsXY: list, endXY: list):

        startXYR = startXY
        interiorWayPoints = interiorWayPointsXY
        endXYR = endXY

        for x in interiorWayPoints:
            if type(x) is not list:
                raise Exception('Format the interior points like so:  [[x1,y1], [x2,y2]]')

        objects = []

        for list_ in interiorWayPoints:
            objects.append(Translation2d(list_[0], list_[1]))

        config = TrajectoryConfig(12, 12)
        config.setReversed(True)

        return TrajectoryGenerator.generateTrajectory(
            Pose2d(startXYR[0], startXYR[1], Rotation2d.fromDegrees(180)),
            objects,
            Pose2d(endXYR[0], endXYR[1], Rotation2d.fromDegrees(-160)),
            config
            )
