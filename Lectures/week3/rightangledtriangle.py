from point import Point
from shape import Shape

class RightAngledTriangle(Shape):
    """
    A right-angled triangle Shape.

    """

    def __init__(self, corners):
        """
        Create RightAngledTriangle self with vertices corners.

        Assume corners are right-angled.

        Extended from Shape.

        :@param corners: corners that define a right angled triangle
        :@type corners: list[Point]

        >>> t =  RightAngledTriangle([Point(0,0), Point(1,0), Point(0,1)])
        """
        # borrow from shape
        Shape.__init__(self, corners)


    # setter
    # override _set_area

    def _set_area(self):
        """
        Set RightAngledTriangle self's area.

        Overrides Shape._set_area

        @rtype: float
        >>> s = RightAngledTriangle([Point(0,0), Point(10,0), Point(0,10)])
        >>> s.area
        50.0
        """

        self._area = 0.5 * self.corners[0].distance(self.corners[1]) *\
                     self.corners[0].distance(self.corners[-1])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    t = RightAngledTriangle([Point(0,0), Point(10,0), Point(0,10)])
