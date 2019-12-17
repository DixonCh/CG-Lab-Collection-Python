import numpy as np
import matplotlib.pyplot as plt

class Point:
    """ Point Class """

    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord

    @classmethod
    def input_point(point):
        """ Takes X-Coord and Y-Coord from user to form a point """
        return point(
            int(input('  X-Coord: ')),
            int(input('  Y-Coord: ')),
        )

    def __str__(self):
        """ Displays point's coordinates """
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class LineSegment:
    """ Line Segment Class """

    def __init__(self, point1, point2):
        self.start = point1
        self.terminal = point2

    def __str__(self):
        """ Displays end-points of line segment """
        return "[" + str(self.start) + ", " + str(self.terminal) + "]"


def check_plc(start_point, terminal_point, qpoint):
    """ Checks PLC for given given query point and line segment """
    line_segment = LineSegment(start_point, terminal_point)
    x = [start_point.x, terminal_point.x]
    y = [start_point.y, terminal_point.y]
    "obtain the coefficients of line y= AX + B using np.polyfit function"
    coefficients = np.polyfit(x, y, 1)
    check_y = coefficients[0] * qpoint.x + coefficients[1]
    if qpoint.x == start_point.x and qpoint.y == start_point.y:
        print(" Query Point " + str(qpoint) + " is Start Point of line segment" + str(line_segment))
    elif qpoint.x == terminal_point.x and qpoint.y == terminal_point.y:
        print(" Query Point " + str(qpoint) + " is Terminal Point of line segment" + str(line_segment))
    elif (check_y == qpoint.y):
        if ((qpoint.y > start_point.y) and (qpoint.y < terminal_point.y)) or (
                (qpoint.y < start_point.x) and (qpoint.y > terminal_point.x)):
            print("\n Query Point " + str(qpoint) + "colinear with line segment" + str(line_segment))
        else:
            print(" Query Point " + str(qpoint) + " is Beyond Line Segment" + str(line_segment))
    elif check_y < qpoint.y:
        print(" Query Point " + str(qpoint) + " is Between Line Segment" + str(line_segment))
    else:
        print(" Query Point " + str(qpoint) + " is Behind Line Segment" + str(line_segment))


def main():
    """ Main Function """

    print("CG LAB 1 (Point Line Classification)")

    print("Enter end-points of Line Segment")
    print(" Start Point")
    start_point = Point.input_point()
    print("\n Terminal Point")
    terminal_point = Point.input_point()

    print("\n Enter Query Point")
    query_point = Point.input_point()

    check_plc(start_point, terminal_point, query_point)

    print("\n DONE.\n")


if __name__ == '__main__':
    main()
