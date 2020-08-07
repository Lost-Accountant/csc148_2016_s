from csc148_stack import Stack

class LinkedListNode:
    """
    Node to be used in linked list

    === Public Attributes ===
    :param LinkedListNode next_: successor to this LinkedListNode
    :param object value: data this LinkedListNode represents
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
        s = "{} ->".format(self.value)
        cur_node = self
        while cur_node is not None:
            if cur_node.next_ is None:
                s += "|"
            else:
                s += " {} ->".format(cur_node.next_.value)
            cur_node = cur_node.next_
        return s

    def __eq__(self, other):
        """
        Return whether LinkedListNode self is equivalent to other.

        :param LinkedListNode self: this LinkedListNode
        :param LinkedListNode|object other: object to compare to self.
        :rtype: bool

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        self_node, other_node = self, other

        while (self_node is not None and
               type(self_node) is type(other_node) and
               self_node.value == other_node.value):
            self_node, other_node = self_node.next_, other_node.next_
        return self_node is None and other_node is None


class CircularLinkedList:
    """
    Circular collection of LinkedListNodes

    === Attributes ==
    :param: back: back node of this CircularLinkedList
    :type back: LinkedListNode
    """

    def __init__(self, value):
        """
        Create CircularLinkedList self with data value.

        :param value: data of the front element of this circular linked list
        :type value: object
        """
        self.back = LinkedListNode(value)
        #back.next_ corresponds to front
        self.back.next_ = self.back

    def __str__(self):
        """
        Return a human-friendly string representation of CircularLinkedList self
        :rtype: str

        >>> lnk = CircularLinkedList(12)
        >>> str(lnk)
        '12 ->'
        """

        #back.next_ corresponds to front
        current = self.back.next_
        result = "{} ->".format(current.value)
        current = current.next_
        while current is not self.back.next_:
            result += " {} ->".format(current.value)
            current = current.next_
        return result

    def append(self, value):
        """
        Insert value before LinkedList front, i.e self.back.next_.

        :param value: value for new LinkedList.front
        :type value: object
        :rtype: None

        >>> lnk = CircularLinkedList(12)
        >>> lnk.append(99)
        >>> lnk.append(37)
        >>> print(lnk)
        12 -> 99 -> 37 ->
        """
        self.back.next_ = LinkedListNode(value, self.back.next_)
        self.back = self.back.next_

    def reverse_print1(self, current):
        """
        Print the values of a linked list in reverse order, i.e. from back of
        the list to the node current

        :param current: a node in self
        :type current: LinkedListNode
         :rtype: None

        >>> lnk = CircularLinkedList(12)
        >>> lnk.append(99)
        >>> lnk.append(37)
        >>> lnk.reverse_print1(lnk.back.next_)
        37
        99
        12
        >>> lnk.reverse_print1(lnk.back)
        37
        """
        # base case
        if current.next_ is self.back.next_:
            print(current.value)
        # general case
        else:
            # call recursively
            self.reverse_print1(current.next_)
            print(current.value)

    def reverse_print2(self, current):
        """
        Print the values of a linked list in reverse order, i.e. from back of
        the list to the node current

        :param current: a node in self
        :type current: LinkedListNode
         :rtype: None

        >>> lnk = CircularLinkedList(12)
        >>> lnk.append(99)
        >>> lnk.append(37)
        >>> lnk.reverse_print2(lnk.back.next_)
        37
        99
        12
        >>> lnk.reverse_print2(lnk.back)
        37
        """
        # without recursion
        # step 1: define a stack
        stack = Stack()

        # step 2: push current onto the stack
        stack.add(current)

        # step 3: advance through the list till the end
        while current.next_ is not self.back.next_:
            current = current.next_
            stack.add(current)

        # step 4: empty the stack
        while stack.is_empty() is False:
            print(stack.remove().value)


    def reverse_print3(self, current):
        """
        Print the values of a linked list in reverse order, i.e. from back of
        the list to the node current

        :param current: a node in self
        :type current: LinkedListNode
         :rtype: None

        >>> lnk = CircularLinkedList(12)
        >>> lnk.append(99)
        >>> lnk.append(37)
        >>> lnk.reverse_print3(lnk.back.next_)
        37
        99
        12
        >>> lnk.reverse_print3(lnk.back)
        37
        """
        # setp 1: list
        l = [current.value]

        # step 2: add value to list
        while current.next_ is not self.back.next_:
            current = current.next_
            l.append(current.value)

        # step 3: reverse list
        l.reverse()

        # step 4: print
        for element in l:
            print(element)

if __name__ == "__main__":
     import doctest
     doctest.testmod()
