import random

class Container:
    """
    A container for storing items of various sorts

    === Attributes ===
    :@type obj: Any
    """
    def __init__(self):
        """
        Initiation. To be implemented in subclass.
        """
        self._content = None
        raise NotImplementedError("Subclass needed")

    def __str__(self):
        """
        Produce a user-friendly string representation of Container self
        @rtype: str
        """
        return str(self._content)

    def __eq__(self, other):
        """
        Determine if a Container self is equivalent to Container other.

        @param other: Container
        @rtype: bool
        """
        return (type(self) == type(other) and
                self._content == other._content)

    def add(self, obj):
        """
        Add an obj object to the Container self. Methods to be implemented in subclass

        @type obj: Any
        @rtype: None
        """
        raise NotImplementedError("Subclass needed")

    def remove(self):
        """
        Remove an obj object from the Container self. Methods to be implemented in subclass.

        @rtype: object
        """
        raise NotImplementedError("Subclass needed")

    def is_empty(self):
        """
        Return whether a Container self is empty

        @rtype: bool
        """
        return len(self._content) == 0

class Stack(Container):
    """
    Last-in, first-out (LIFO) stack.
    """
    def __init__(self):
        """
        Create new, empty Stack self.

        Overrides Container.__init__

        """
        self._content = []

    def add(self, obj):
        """
        Add obj to the top of Stack self.

        Overrides Container.add

        :@param obj: object to place on Stack
        :@type obj: Any
        :@rtype: None
        """
        self._content.append(obj)

    def remove(self):
        """
        Remove and return the top element of Stack self.
        Assume Stack self is not empty.

        Overrides Container.remove

        @rtype: object
        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._content.pop()

class Sack(Container):
    """
     A Sack with elements in no particular order.
    """

    def __init__(self):
        """
        Create a new, empty Sack self.

        Overrides Container.__init

        :@type self: Sack
        :@rtype: None
        """
        self._content = {}
        self._key = 0

    def add(self, obj):
        """
        Add object obj to some random location of Sack self.

        :@param obj: object to place on Sack
        :@type obj: Any
        :@rtype: None
        """
        self._content[obj] = obj

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
        return self._content.pop(random.choice(list(self._content.keys())))


# can use universal __eq__ since dict has no order


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    s = Sack()
    s.add(7)
    print(s.is_empty())
