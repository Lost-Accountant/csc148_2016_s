from container import Container

class Sack(Container):
    """
    Last-in, first-out (LIFO) Sack.
    """
    def __init__(self):
        """
        Create a new, empty Sack self.

        Overrides Container.__init__

        """
        self._content, self._key = {}, (1,1)

    def add(self, obj):
        """
        Add object obj to top of Sack self.

        Overrides Container.add

        :param obj: object to place on Sack
        :type obj: Any
        :rtype: None
        """
        # increment key in a way that a dictionary stores
        # in no particular order...
        self._key = (self._key[0], self._key[1] + 1)
        self._content[self._key] = obj

    def remove(self):
        """
        Remove and return top element of Sack self.

        Assume Sack self is not empty.

        Overrides Container.add

        :rtype: object
        >>> s = Sack()
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._content.popitem()[1]

    def __str__(self):
        """
        Return a list-like string representation of Sack.

        Overrides Container.add

        :rtype: str
        >>> s = Sack()
        >>> s.add(7)
        >>> print(s)
        [7]
        """
        return str(list(self._content.values()))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("sack")
