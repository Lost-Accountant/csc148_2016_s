from container import Container


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
    s = Stack()
    s.add(5)
    print("hi")


