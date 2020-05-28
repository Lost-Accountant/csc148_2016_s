from shape import Shape
from point import Point

class Square(Shape):
    """
    A square shape
    """

    def __init__(self, corners):
        """
        Create Square self with vertices corners.

        Assume all sides are equal and corners are square.

        Extended from Shape.

        :@param corners: corners that define this Square
        :@type corners: list[Point]

        >>> s = Square([Point(0,0), Point(1,0), Point(1,1), Point(0,1)])
        """
        # borrow function from Shape
        Shape.__init__(self, corners)

# setter
# set a parameter, not return it
    def _set_area(self):
        """
        Set Square self's area.

        Overrides Shape._set_area

        @rtype: float

        >>> s = Square([Point(0,0), Point(10,0), Point(10,10), Point(0,10)])
        >>> s.area
        100.0
        """
        # in case only 1 point, so use 0 and -1.
        # worst situation refers to the same point
        self._area =  (self.corners[-1].distance(self.corners[0]))**2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    s = Square([Point(0,0)])
