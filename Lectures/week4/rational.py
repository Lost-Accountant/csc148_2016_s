class Rational:
    """
    A rational number

    Public Attributes:
    ==================
    None
    """

    def __init__(self, num, denom=1):
        """
        Create new Rational self with numerator num and
        denominator denom --- denom must not be 0.

        :param num: the numinoator of Rational self
        :type num: int
        :param num: the numinoator of Rational self
        :type denom: int
        """
        self.num, self.denom = num, denom

    def __eq__(self, other):
        """
        Return whether Rational self is equivalent to other.

        :param other: a Rational number
        :type other: Rational | Any
        :return: whether the two numbers are equal or not
        :rtype: bool

        >>> r1 = Rational(3, 5)
        >>> r2 = Rational(6, 10)
        >>> r3 = Rational(4, 7)
        >>> r1 == r2
        True
        >>> r1.__eq__(r3)
        False
        """
        return (type(self) == type(other) and
                self.num * other.denom == self.denom * other.num)

    def __str__(self):
        """
        Return a user-friendly string representation of
        Rational self.

        :return: a string representation of Ratoinal self
        :rtype: str

        >>> print(Rational(3, 5))
        3 / 5
        """
        return "{} / {}".format(self.num, self.denom)

    def __repr__(self):
        """
        Return a string representation of Rational self that
        evaluates to an equivalent Rational.

        :return: a string representation of how Ratoinal self is constructed
        :rtype: str

        >>> r1 = Rational(3, 4)
        >>> r1
        Rational(3, 4)
        """
        return "Rational({}, {})".format(self.num, self.denom)

    def __lt__(self, other):
        """
        Return whether Rational self is less than other.

        :param other: a Rational number
        :type other: Rational | Any
        :return: whether or not Rational self is lesser than other
        :rtype: bool

        >>> Rational(3, 5).__lt__(Rational(4, 7))
        False
        >>> Rational(3, 5).__lt__(Rational(5, 7))
        True
        """
        return self.num * other.denom < self.denom * other.num

    def __mul__(self, other):
        """
        Return the product of Rational self and Rational other.

        :param other: a Rational number
        :type other: Rational
        :return: the multiplication of self and other
        :rtype: Rational

        >>> print(Rational(3, 5).__mul__(Rational(4, 7)))
        12 / 35
        """
        return Rational(self.num * other.num, self.denom * other.denom)

    def __add__(self, other):
        """
        Return the sum of Rational self and Rational other.

        :param other: a Rational number
        :type other: Rational
        :rtype: Rational

        >>> print(Rational(3, 5).__add__(Rational(4, 7)))
        41 / 35
        """
        return Rational(self.num * other.denom +
                        other.num * self.denom,
                        self.denom * other.denom)

    def _get_num(self):
        # """
        # Return numerator num.
        #
        # :rtype: int
        #
        # >>> Rational(3, 4)._get_num()
        # 3
        # """
        return self._num

    def _set_num(self, num):
        # """
        # Set numerator of Rational self to num.
        #
        # :type num: int
        # :rtype: None
        # """
        self._num = int(num)

    def _get_denom(self):
        # """
        # Return denominator of Rational self.
        #
        # :rtype: int
        #
        # >>> Rational(3, 4)._get_denom()
        # 4
        # """
        return self._denom

    def _set_denom(self, denom):
        # """
        # Set denominator of Rational self to denom.
        #
        # :type denom: int
        # :rtype: None
        # """
        if denom == 0:
            raise Exception("Zero denominator!")
        else:
            self._denom = int(denom)

    num = property(_get_num, _set_num)
    denom = property(_get_denom, _set_denom)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    r1 = Rational(3, 5)
    r2 = Rational(4, 7)
    r1 < r2
    r1.__add__(r2)
    r1.__mul__(r2)
    r1 == r2
