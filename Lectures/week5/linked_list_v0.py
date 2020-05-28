# As an exercise on linked lists, complete the following classes
# read the forum for more exercises on linkedlists

class LinkedListNode:
    """
    a node to help defining linked list data structure
    (this is a helper class)

    ====Public Attributes ====
    :type value: object
         the object to be stored in the node
    :type next_: LinkedListNode | None
         a reference to the next LinkedListNode
    """

    def __init__(self, value, next_=None):
        """
        Create a new LinkedListNode self

        :param value:  the object to be stored in the node
        :type value: object
        :param next_: a reference to the next LinkedListNode
        :type next_:
        """
        self.value, self.next_ = value, next_

    def __str__(self):
        """
        Return a user-friendly representation of LinkedListNode self
        :rtype: str
        >>> node1 = LinkedListNode(10)
        >>> print(node1)
        10 ->|
        >>> node2 = LinkedListNode(12, node1)
        >>> print(node2)
        12 ->10 ->|
        """
        current = self
        s = ""
        while current is not None:
            s += "{} ->".format(current.value)
            current = current.next_
        s += "|"
        return s

    def __eq__(self, other):
        """
        Return whether or not LinkedList self is equivalent to the other

        :param other: a LinkedListNode
        :type other: LinkedListNode |Any
        :rtype: bool
        >>> node1 = LinkedListNode(10)
        >>> node2 = LinkedListNode(12)
        >>> node3 = LinkedListNode(10, node2)
        >>> node4 = LinkedListNode(10, LinkedListNode(12))
        >>> node1 == node2
        False
        >>> node1 == node3
        False
        >>> node3 == node4
        True
        """
        current_self = self
        current_other = other
        while type(current_self) is type(current_other) and \
                current_self and current_other and \
                        current_self.value == current_other.value:
            current_self = current_self.next_
            current_other = current_other.next_
        if not current_self and not current_other:
            return True
        else:
            return False

    def set_value(self, new_value):
        """
        Set the value of self to new_value

        :param new_value: a new value for the node self
        :type new_value: object
        :rtype: None
        >>> node1 = LinkedListNode(10)
        >>> print(node1)
        10 ->|
        >>> node1.set_value(20)
        >>> print(node1)
        20 ->|
        """
        self.value = new_value


class LinkedList:
    """
    a chain of LinkedListNodes

    === Public Attributes ==
    :type front: LinkedListNode
         first node of this LinkedList
    :type back: LinkedListNode back
         last node of this LinkedList
    :type size: int
         number of nodes in this LinkedList a non-negative integer
    """

    def __init__(self):
        """
        Create an empty linked list.
        """
        self.front, self.back, self.size = None, None, 0

    def __str__(self):
        """
        Return a human-friendly string representation of LinkedList self.

        >>> my_list = LinkedList()
        >>> my_list.prepend(5)
        >>> print(my_list)
        5 ->|
        """
        return str(self.front)

    def __eq__(self, other):
        """
        Return whether LinkedList self is equivalent to other.

        :param other: object to compare to self
        :type other: LinkedList | object
        :rtype: bool

        >>> LinkedList().__eq__(None)
        False
        >>> my_list = LinkedList()
        >>> my_list.prepend(5)
        >>> another_list = LinkedList()
        >>> another_list.prepend(5)
        >>> my_list.__eq__(another_list)
        True
        """
        return (type(self) is type(other) and
                (self.size, self.front, self.back) ==
                (other.size, other.front, other.back))

    def append(self, value):
        """
        Insert a new LinkedListNode with value after self.back.

        :param value: value of new LinkedListNode
        :type value: object
        :rtype: None

        >>> my_list = LinkedList()
        >>> my_list.append(5)
        >>> my_list.size
        1
        >>> print(my_list.front)
        5 ->|
        >>> my_list.append(6)
        >>> my_list.size
        2
        >>> print(my_list.front)
        5 ->6 ->|
        """
        new_node = LinkedListNode(value)
        if self.front is None:
            # append to an empty LinkedList
            self.front = self.back = new_node
        else:
            # self.back better not be None
            assert self.back, 'Unexpected None node'
            self.back.next_ = new_node
            self.back = new_node
        self.size += 1

    def prepend(self, value):
        """
        Insert value before LinkedList self.front.

        :param value: value for new LinkedList.front
        :type value: object
        :rtype: None

        >>> my_list = LinkedList()
        >>> my_list.prepend(0)
        >>> my_list.prepend(1)
        >>> my_list.prepend(2)
        >>> str(my_list.front)
        '2 ->1 ->0 ->|'
        >>> my_list.size
        3
        """
        new_node = LinkedListNode(value)
        # if linked list is empty
        if self.front is None:
            self.front = self.back = new_node

        # if linked list is not empty
        else:
            # set ref for the new node to be the current front
            new_node.next_ = self.front
            # set the new node to be the new front
            self.front = new_node
        # increase the size
        self.size += 1


    def delete_front(self):
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        :rtype: None

        >>> my_list = LinkedList()
        >>> my_list.prepend(0)
        >>> my_list.prepend(1)
        >>> my_list.prepend(2)
        >>> my_list.delete_front()
        >>> str(my_list.front)
        '1 ->0 ->|'
        >>> my_list.size
        2
        >>> my_list.delete_front()
        >>> my_list.delete_front()
        >>> str(my_list.front)
        'None'
        """
        # assume linked list not empty
        self.front = self.front.next_
        self.size -= 1

    def __getitem__(self, index):
        """
        Return the value at LinkedList self's position index.

        :param index: position to retrieve value from
        :type index: int
        :rtype: object

        >>> my_list = LinkedList()
        >>> my_list.prepend(1)
        >>> my_list.prepend(0)
        >>> my_list.__getitem__(1)
        1
        >>> my_list[-1]
        0
        >>> my_list[0]
        0
        """
        id = 0
        current_self = self.front
        if index <= 0:
            return current_self.value

        while current_self.next_:
            current_self = current_self.next_
            id += 1
            if id == index:
                return current_self.value
            # finish the whole thing without returning
            # just not return anything?

    def __setitem__(self, index, new_value):
        """
        Set the value at LinkedList self's position index to a new value.

        :param index: position to set the new value to
        :type index: int
        :param new_value: position to set the new value to
        :type new_value: object

        :rtype: object

        >>> my_list = LinkedList()
        >>> my_list.prepend(5)
        >>> my_list.prepend(10)
        >>> my_list.__setitem__(self, 0, 15)
        >>> my_list[0]
        15
        >>> my_list.__setitem__(self, 1, 20)
        >>> my_list[1]
        20
        """
        if index < self.size:
            counter = 0
            while counter != index:
                pass

    def __contains__(self, value):
        """
        Return whether LinkedList self contains value.

        :param value: value to search for in self
        :type value: object
        :rtype: bool

        >>> my_list = LinkedList()
        >>> my_list.prepend(0)
        >>> my_list.prepend(1)
        >>> my_list.prepend(2)
        >>> my_list.__contains__(1)
        True
        >>> 1 in my_list
        True
        >>> my_list.__contains__(3)
        False
        """

        current_self = self.front
        if current_self.value == value:
            return True

        while current_self.next_:
            current_self = current_self.next_
            if current_self.value == value:
                return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
