class Container:
    """
    a data structure to store and retrieve objects.

    This is an abstract class that is not meant to be instantiated itself,
    but rather subclasses are to be instantiated.
    """
    def __init__(self):
        """
        Create a new and empty Container self.
        """
        self._content = None
        raise NotImplemented ("This is an abstract class, define or"
                              " use its subclass")

    def add(self, obj):
        """
        Add object obj to Container self.

        :param obj: object to place onto Container self
        :type obj: Any
        :rtype: None
        """
        raise NotImplemented ("This is an abstract class, define or"
                              " use its subclass")

    def remove(self):
        """
        Remove and return an element from Container self.

        Assume that Container self is not empty.
        :return an object from Container slef
        :rtype: object
        """
        raise NotImplemented ("This is an abstract class, define or"
                              " use its subclass")

    def is_empty(self):
        """
        Return whether Container self is empty.

        :rtype: bool
        """
        return len(self._content) == 0

    def __eq__(self, other):
        """
        Return whether Container self is equivalent to the other.

        :param other: a Container
        :type other: Container
        :rtype: bool
        """
        return type(self)== type(other) and self._content == other._content

    def __str__(self):
        """
        Return a human-friendly string representation of Container.

        :rtype: str
        """
        return str(self._content)


class Stack(Container):
    """
    Last-in, first-out (LIFO) stack.
    """
    def __init__(self):
        """
        Create a new, empty Stack self.

        Overrides Container.__init__

        """
        self._content = []

    def add(self, obj):
        """
        Add object obj to top of Stack self.

        Overrides Container.add

        :param obj: object to place on Stack
        :type obj: Any
        :rtype: None
        """
        self._content.append(obj)

    def remove(self):
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty.

        Overrides Container.add

        :rtype: object
        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._content.pop()

if __name__ == "__main__":
    import doctest
    doctest.testmod()



