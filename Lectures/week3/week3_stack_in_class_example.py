class Stack:
    """
    Last-in, first-out (LIFO) stack.
    """

    def __init__(self):
        """
        Create a new, empty Stack self.
        """
        self.stack = []

    def add(self, obj):
        """
        Add obj to the top of Stack self.

        :@param obj: object to place on Stack
        :@type obj: Any
        :@rtype: None
        """
        self.stack.append(obj)

    def remove(self):
        """
        Remove and return the top element of Stack self.
        Assume Stack self is not empty.

        @rtype: Any
        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self.stack.pop(-1)

    def is_empty(self):
        """
        Return whether Stack self is empty.

        @rtype: bool
        """
        return len(self.stack) == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    s = Stack()
    s.add(5)
