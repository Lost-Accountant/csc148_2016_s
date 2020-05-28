class Rectangle:
    """"
    A rectangle defined by its top-left corner, width, and height

    Attributes:
    ===========
    @type x: int
        The x coordinate of rectangle's top-left corner
    @type y: int
        The y coordinate of rectangle's top-left corner
    @type width: int
        The width of rectangle
    @type height: int
        The height of rectangle

    """

    def __init__(self, the_x, the_y, the_width, the_height):
        """
        Create a new Rectangle self that with top_left corner at the_x and the_y
        and with width the_width and height the_height.

        the_x, the_y, the_width, and the_height are non-negative integers.

        @param Rectangle self: this rectangle
        @param int the_x: The x coordinate of rectangle's top-left corner
        @param int the_y: The y coordinate of rectangle's top-left corner
        @param int the_width: The width of rectangle
        @param int the_height: The height of rectangle
        @rtype: None
        """
        self.x = the_x
        self.y = the_y
        self.width = the_width
        self.height = the_height

    def __eq__(self, other):
        """
        Return whether this rectangle is equivalent to other.

        @param Rectangle self: this rectangle
        @param Rectangle | Any other: another rectangle
        @rtype: bool

        >>> rec1 = Rectangle(100, 200, 400, 200)
        >>> rec2 = Rectangle(50, 100, 400, 200)
        >>> rec3 = Rectangle(100, 200, 400, 200)
        >>> rec1 == rec2
        False
        >>> rec1 == rec3
        True
        """
        if type(self) == type(other):
            if (self.x, self.y, self.width, self.height) == (other.x, other.y, other.width, other.height):
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        """
        Return a user-friendly string representation of Rectangle self.

        @param Rectangle self: this rectangle
        @rtype: str

        >>> rec1 = Rectangle(100, 200, 400, 200)
        >>> print(rec1)
        (100, 200, 400, 200)
        """
        return ('({}, {}, {}, {})'.format(self.x, self.y, self.width, self.height))

    def translate_right(self, num):
        """
        Move Rectangle self to the right by a number of pixels.

        num is a non-negative integer.

        @param Rectangle self: this rectangle
        @param int num: the number of pixel the rectangle is translated
        @rtype: None

        >>> rec1 = Rectangle(100, 200, 300, 400)
        >>> rec1.translate_right(20)
        >>> rec1.x
        120
        """
        self.x += num

    def is_in(self, other):
        """
        Return whether this rectangle falls within the other

        @param Rectangle self: this rectangle
        @param Rectangle other: another rectangle
        @rtype: bool

        >>> rec1 = Rectangle(100, 200, 400, 200)
        >>> rec2 = Rectangle(50, 100, 400, 200)
        >>> rec3 = Rectangle(50, 100, 500, 400)
        >>> rec1.is_in(rec2)
        False
        >>> rec1.is_in(rec3)
        True
        """
        if type(self) == type(other):
            return self.x + self.width <= other.x + other.width and self.y + self.height <= other.y + other.height
        else:
            return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    rec1 = Rectangle(0, 0, 100, 200)
    rec2 = Rectangle(0, 0, 100, 200)
    rec1.is_in(rec2)
    rec1 == rec2
    rec1.translate_right(30)
    rec1 == rec2
