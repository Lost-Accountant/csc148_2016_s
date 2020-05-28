from random import randint

class Sack:
    """
    A Sack with elements in no particular order.
    """

    def __init__(self):
        """
        Create a new, empty Sack self.
        :@type self: Sack
        :@rtype: None
        """
        self._content = []

    def add(self, obj):
        """
        Add object obj to some random location of Sack self.

        :@param obj: object to place on Sack
        :@type obj: Any
        :@rtype: None
        """
        i = randint(0,len(self._content))
        self.sack = self._content[:i] + [obj] + self._content[i:]

    def remove(self):
        """
        Remove and return some random element of Sack self.
        Assume Sack self is not empty.

        :@param Sack self: this Sack
        :@rtype: object

        >>> s = Sack()
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._content.pop()

    def is_empty(self):
        """
        Return whether Sack self is empty

        :@rtype: bool
        """
        return len(self.sack) == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = Sack()
    s.add(5)
    s.add(6)
    s.add(7)
    print(s.sack)
