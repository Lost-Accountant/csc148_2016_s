class LinkedListNode:
    """
    Node to be used in linked list

    === Public Attributes ===
    :type next_: LinkedListNode
        successor to this LinkedListNode
    :type value: object
        data this LinkedListNode represents
    """
    def __init__(self, value, next_=None):
        """
        Create LinkedListNode self with data value and successor next_.

        :param value: data of this linked list node
        :type value: object
        :param next_: successor to this LinkedListNode.
        :type next_: LinkedListNode|None
        """
        self.value, self.next_ = value, next_

    def __str__(self):
        """
        Return a user-friendly representation of this LinkedListNode.

        :rtype: str

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        # start with a string s to represent current node.
        s = "{} ->".format(self.value)
        # create a reference to "walk" along the list
        current_node = self.next_
        # for each subsequent node in the list, build s
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s

    def __eq__(self, other):
        """
        Return whether LinkedListNode self is equivalent to other.

        :param other: object to compare to self.
        :type other: LinkedListNode|object
        :rtype: bool

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        # check the entire chain
        current_self = self
        current_other = other

        while type(current_self) == type(current_other) and \
            current_self and current_other and \
            current_self.value == current_other.value:
            # type right, both not None, and value right
            current_self = current_self.next_
            current_other = current_other.next_

        # if breaks, one None, both None, value not match, type not match
        # second situation means True
        # type mismatch only happens at first since next is node
        # if type mismatch, one won't be None
        return current_self is None and current_other is None

class LinkedList:
    """
    Collection of LinkedListNodes

    === Public Attributes ==
    :type front: LinkedListNode
        first node of this LinkedList
    :type back: LinkedListNode
        last node of this LinkedList
    :type size: int
        number of nodes in this LinkedList,  a non-negative integer
    """
    def __init__(self):
        """
        Create an empty linked list.
        """
        self.front, self.back, self.size = None, None, 0

    def __str__(self):
        """
        Return a human-friendly string representation of
        LinkedList self.

        :rtype: str

        >>> lnk = LinkedList()
        >>> print(lnk)
        I'm so empty... experiencing existential angst!!!
        """
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "I'm so empty... experiencing existential angst!!!"
        else:
            # use front.__str__() if this list isn't empty
            return str(self.front)

    def __eq__(self, other):
         """
         Return whether LinkedList self is equivalent to
         other.

         :param other: object to compare to self
         :type other: LinkedList|object
         :rtype: bool

         >>> LinkedList().__eq__(None)
         False
         >>> lnk = LinkedList()
         >>> lnk.prepend(5)
         >>> lnk2 = LinkedList()
         >>> lnk2.prepend(5)
         >>> lnk.__eq__(lnk2)
         True
         """
         return type(self) == type(other) and \
                (self.front, self.back, self.size) == \
                (other.front, other.back, other.size)


    def delete_after(self, value):
        """
        Remove the 1 node following the first occurrence of value and attach the rest back to the linked list, if possible, otherwise leave self unchanged.

        :param value: value just before the deletion
        :type value: object
        :rtype: None
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(10)
        >>> lnk.prepend(15)
        >>> lnk.delete_after(15)
        >>> print(lnk)
        15 -> 5 ->|
        >>> lnk.delete_after(25)
        >>> print(lnk)
        15 -> 5 ->|

        """
        current_node = self.front
        while current_node and current_node.value != value:
            current_node = current_node.next_
            # 2 ways of ending
            # one is running out to None
            # the other is finding the right value
        if current_node and current_node.next_:
            # next is back
            if current_node.next_.next_ is None:
                current_node.next_ = None
                self.back = current_node

            # current and next are not back
            else:
                current_node.next_ = current_node.next_.next_

            self.size -= 1


    def append(self, value):
        """
        Insert a new LinkedListNode with value after self.back.

        :param value: value of new LinkedListNode
        :type value: object
        :rtype: None

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        # create the new node
        new_node = LinkedListNode(value)
        # if the list is empty, the new node is front and back
        if self.size == 0:
            assert self.back is None and self.front is None, "ooops"
            self.front = self.back = new_node
        # if the list isn't empty, front stays the same
        else:
            # change *old* self.back.next_ first!!!!
            self.back.next_ = new_node
            self.back = new_node
        # remember to increase the size
        self.size += 1

    def prepend(self, value):
        """
        Insert value before LinkedList self.front.

        :param value: value for new LinkedList.front
        :type value: object
        :rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        """
        # Create new node with next_ referring to front
        new_node = LinkedListNode(value, self.front)
        # change front
        self.front = new_node
        # if the list was empty, change back
        if self.size == 0:
            self.back = new_node
        # update size
        self.size += 1

    def delete_front(self):
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        :rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        """
        assert self.front is not None, "unexpected None!"
        # if back == front, set it to None
        if self.front == self.back:
            self.back = None
        # set front to its successor
        self.front = self.front.next_
        # decrease size
        self.size -= 1

    def __setitem__(self, index, value):
        """
        Set the value of list at position index to value. Raise IndexError
        if index >= self.size

        :param int: position of list to change
        :type index: int
        :param value: new value for linked list
        :type value: object
        :rtype: None
        """
        # correction on negative index
        if index < 0:
            index = index + self.size

        # if corrected index still negative or bigger than size
        if index > self.size or index < 0:
            raise IndexError("index exceeds linked list's size")
        else:
            current_node = self.front
            # jumps index times from 0 (front)
            for ind in range(index):
                current_node = current_node.next_
            # after looping, exactly on point
            current_node.value = value

    def __add__(self, other):
        """
        Return a new list by concatenating self to other.  Leave
        both self and other unchanged.

        :param other: Linked list to concatenate to self
        :type other: LinkedList
        :rtype: LinkedList

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> print(lnk1 + lnk2)
        5 -> 7 ->|
        >>> print(len(lnk1 + lnk2))
        2
        >>> lnk3 = LinkedList()
        >>> print(lnk3 + lnk1)
        5 ->|
        """
        # cannot make copy of None
        if len(self) == 0:
            return other.copy()
        elif len(other) == 0:
            return self.copy()
        else:
            # make copy of 2 linked lists to be safe
            lnk1 = self.copy()
            lnk2 = other.copy()
            # connect back
            lnk1.back.next_ = lnk2.front
            # set new back
            lnk1.back = lnk2.back
            # set new size
            lnk1.size += lnk2.size

            return lnk1

    def insert_before(self, value1, value2):
        """
        Insert value1 into LinkedList self before the first occurrence
        of value2, if it exists.  Otherwise leave self unchanged.

        :param value1: value to insert, if possible
        :type value1: object
        :param value2: value to insert value1 ahead of
        :type value2: object
        :rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(10)
        >>> lnk.insert_before(1, 5)
        >>> print(lnk)
        10 -> 1 -> 5 ->|
        """
        current_node = self.front
        # if value 2 at front
        if current_node.value == value2:
            self.prepend(value1)
        elif current_node is not None:
            # to avoid empty linked list
            # construct a node
            value1_node = LinkedListNode(value1)
            # value 2 somewhere in the list
            while current_node.next_:
                if current_node.next_.value == value2:
                    value1_node.next_ = current_node.next_
                    current_node.next_ = value1_node
                    # update size
                    self.size += 1
                    return
                else:
                    current_node = current_node.next_

    def copy(self):
        """
        Return a copy of LinkedList self.  The copy should have
        different nodes, but equivalent values, from self.

        :rtype: LinkedList

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(7)
        >>> print(lnk.copy())
        7 -> 5 ->|
        """
        # just need to make copy of the value
        # don't have to make copy of node
        node_copy = self.front
        new_lnk = LinkedList()
        while node_copy:
            new_lnk.append(node_copy.value)
            node_copy = node_copy.next_
        # when next one is None, node_copy now None, run thru whole list
        # if a copy of whole node is made,
        return new_lnk

    def __len__(self):
        """
        Return the number of nodes in LinkedList self.

        :rtype: int
        """
        return self.size

    def __getitem__(self, index):
        """
        Return the value at LinkedList self's position index.

        :param index: position to retrieve value from
        :type index: int
        :rtype: object

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(0)
        >>> lnk.__getitem__(1)
        0
        >>> lnk[-1]
        0
        """
        # deal with a negative index by adding self.size
        while index < 0:
            index += self.size
        if index >= self.size or self.size == 0:
            raise IndexError("index too big!!!")
        # an empty list, or an index that is too large is an error
        else:
            current_node = self.front
            # walk index steps along from 0 to retrieve element
            for step in range(index):
                current_node = current_node.next_
                assert current_node is not None, "unexpected None!!!!!"
            # return the value at position index
            return current_node.value

    def __contains__(self, value):
        """
        Return whether LinkedList self contains value.

        :param value: value to search for in self
        :type value: object
        :rtype: bool

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> lnk.append(2)
        >>> 2 in lnk
        True
        >>> lnk.__contains__(3)
        False
        """
        current_node = self.front
        # "walk" the linked list
        while current_node is not None:
            # if any node has a value == value, return True
            if current_node.value == value:
                return True
            current_node = current_node.next_
        # if you get to the end without finding value,
        # return False
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
