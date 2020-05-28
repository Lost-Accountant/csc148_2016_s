from point import Point
from turtle import Turtle

class Shape:
    """
    A Shape shape that can draw itself, move, and report area and permimeter.

    === Attributes ===
    :@type corners: list[Point]
        corners that define this Shape
    :@type area; float
        area of this shape
    :@type perimeter: float
        perimeter of this shape
    """

    def __init__(self, corners):
        """
        Create a new Shape self with defined by its corners, with perimeter and area.
        :@param corners: corners that define shape self
        :@type corners: list [Points]
        :@rtype: None
        """

        # copy of the list
        self.corners = corners[:]
        self._turtle = Turtle()
        self._set_perimeter()
        self._set_area()

# setter
    def _set_perimeter(self):
        # """
        # Set Shape self's perimeter to the sum of the distances
        # between corners.
        #
        # :rtype: None
        # """
        distance = 0
        for i in range(len(self.corners) - 1):
            distance += self.corners[i].distance(self.corners[i+1])
        self._perimeter = distance

    def _set_area(self):
        # too complex for abstract shape
        self._area = -1.0
        raise NotImplementedError("Set area in subclass")

# getter
    def _get_perimeter(self):
        return self._perimeter

    def _get_area(self):
        return self._area


# property
    perimeter = property(_get_perimeter, _set_perimeter)
    area = property(_get_area)


    def __eq__(self, other):
        """
        Determine if a Shape self is equivalent to Shape other

        :@type self: a Shape
        :@param other: a 2D Shape
        :@type other: Shape
        :@return: whether coordinates of Shape self is the same as of the other Shape
        :@rtype: bool
        """
        # always check type first
        return (type(self) == type(other) and
                self.corners == other.corners and
                self.perimeter == other.perimeter)

    def __str__(self):
        """
        Produce a user-friendly string representation of Shape self.

        :@return: string representation of Shape self
        :@rtype: str
        >>> print(Shape([Point(0, 0), Point(1, 0), Point(0, 1)]))
        Shape([(0, 0), (1, 0), (0, 1)])
        """
        point_list = ', '.join([str(p) for p in self.corners])

        return type(self).__name__ + '([{}])'.format(point_list)

    def move_by(self, offset_point):
        """
        Move Shape self to a new position by adding Point offset_point  to each corner

        :@param offset_point: the point relative to the Shape self will be moved
        :@type offset_point: Point
        :@rtype: None
        """
        # move every point by offset_point, using _add_

        for i in range(len(self.corners)):
            self.corners[i] = self.corners[i].add(offset_point)

        return

    def draw(self):
        """
        Draw Shape self.

        :rtype: None
        """
        self._turtle.penup()

        # to solve that loop not going from nth to 1st
        self._turtle.goto(self.corners[-1].x, self.corners[-1].y)
        self._turtle.pendown()
        for i in range(len(self.corners)):
            self._turtle.goto(self.corners[i].x, self.corners[i].y)

        # don't leave extra more mark
        self._turtle.penup()
        # good practice to reset
        self._turtle.goto(0,0)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = Shape([Point(0,0)])
