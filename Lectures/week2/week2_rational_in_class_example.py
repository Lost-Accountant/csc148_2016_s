class Rational:
    """
    A rational number
    """
    def __init__(self, num, denom=1):
        """
        Create new RRationalself with numerator num and denominator denom --- denom cannot be 0.

        :@type self: Rational
        :@type num: int
        :@type denom: int
        :@rtype: None
        """
        self.num = num
        self.denom = denom

    # private attribute
    def _get_num(self):
        """
        Return numerator of Rational self

        :@type self: Rational
        @rtype: int

        >>> Rational(3,4)._get_num()
        3
        """

        return self._num

    def _set_num(self, num):
        """
        Set numerator of Rational self to num.


        :@type self: Rational
        :@type num: int
        :@rtype: None
        """

        self._num = int(num)

    num = property(_get_num, _set_num)

    def _get_denom(self):
        """
        Return denominator of Rational self.

        :@type self: Rational
        :@rtype: int

        >>> Rational(3,4)._get_denom()
        4
        """
        return self._denom

    def _set_denom(self, denom):
        # """
        # Set denominator of Rational self to denom.
        # :type self: Rational
        # :type denom: int
        # :rtype: None
        # """
        if denom == 0:
            raise Exception("Zero denominator!")
        else:
            self._denom = int(denom)

    denom = property(_get_denom, _set_denom)

    # public methods
    def __eq__(self, other):
        """
        Return whether Rational self is equivalent to other.

        :@type self: Rational
        :@type other: Rational | Any
        :@rtype: bool

        >>> r1 = Rational(3,5)
        >>> r2 = Rational(6,10)
        >>> r3 = Rational(4,7)
        >>> r1 == r2
        True
        >>> r1.__eq__(r3)
        False
        """
        return (type(self) == type(other)) and \
               ((self.num/self.denom) == (other.num/other.denom))

    def __str__(self):
        """
        Return a user-friendly string representation of Rational self.
        :@type self: Rational
        :@rtype: str

        >>> print(Rational(3,5))
        3 / 5
        """

        return '{} / {}'.format(self.num, self.denom)

    def __lt__(self, other):
        """
        Return whether Rational self is less than other.

        :@type self: Rational
        :@type other: Rational | Any
        :@rtype: bool

        >>> Rational(3,5).__lt__(Rational(4,7))
        False
        >>> Rational(3,5).__lt__(Rational(5,7))
        True
        """

        return (self.num/self.denom) < (other.num/other.denom)

    def __mul__(self, other):
        """
        Return the product of Rational self and Rational other.

        :@type self: Rational
        :@type other: Rational
        :@rtype: Rational

        >>> print(Rational(3, 5).__mul__(Rational(4, 7)))
        12 / 35
        """
        # not worry about common divisor for now

        return Rational(self.num * other.num, self.denom * other.denom)

    def __add__(self, other):
        """
        Return the sum of Rational sefl and Rational other.

        :@type self: Rational
        :@type other: Rational
        :@rtype: Rational

        >>> print(Rational(3,5).__add__(Rational(4, 7)))
        41 / 35
        """

        return Rational((self.num * other.denom + self.denom * other.num),
                        (self.denom * other.denom))




if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(Rational(3.0, 4.0))

    #print(Rational(3.0, 0))

    a1 = Rational(3,4)
    print(a1.denom)
    a1.denom = 123.4321
    print(a1.denom)

    a1.denom = 0
    print(a1.denom)

