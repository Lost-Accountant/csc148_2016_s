from csc148_queue import Queue

class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.

    === Attributes ===
    :param data: data for this binary tree node
    :type data: object
    :param left: left child of this binary tree node
    :type left: BinaryTree|None
    :param right: right child of this binary tree node
    :type right: BinaryTree|None
    """

    def __init__(self, data, left=None, right=None):
        """
        Create BinaryTree self with data and children left and right.

        :param data: data of this node
        :type data: object
        :param left: left child
        :type left: BinaryTree|None
        :param right: right child
        :type right: BinaryTree|None
        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other):
        """
        Return whether BinaryTree self is equivalent to other.

        :param other: object to check equivalence to self
        :type other: Any
        :rtype: bool

        >>> BinaryTree(7).__eq__("seven")
        False
        >>> b1 = BinaryTree(7, BinaryTree(5))
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5), None))
        True
        """
        return (type(self) == type(other) and
                self.data == other.data and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self):
        """
        Represent BinaryTree (self) as a string that can be evaluated to
        produce an equivalent BinaryTree.

        @rtype: str

        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
        """
        return "BinaryTree({}, {}, {})".format(repr(self.data),
                                               repr(self.left),
                                               repr(self.right))

    def __str__(self, indent=""):
        """
        Return a user-friendly string representing BinaryTree (self)
        inorder.  Indent by indent.

        >>> b = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = (self.right.__str__(
            indent + "    ") if self.right else "")
        left_tree = self.left.__str__(indent + "    ") if self.left else ""
        return (right_tree + "{}{}\n".format(indent, str(self.data)) +
                left_tree)

    def __contains__(self, value):
        """
        Return whether tree rooted at node contains value.

        :param value: value to search for
        :type value: object
        :rtype: bool

        >>> BinaryTree(5, BinaryTree(7), BinaryTree(9)).__contains__(7)
        True
        """
        return (self.data == value or
                (self.left and value in self.left) or
                (self.right and value in self.right))


def parenthesize(b):
    """
    Return a parenthesized expression equivalent to the arithmetic
    expression tree rooted at b.

    Assume:  -- b is a binary tree
             -- interior nodes contain data in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float data

    :param b: arithmetic expression tree
    :type b: BinaryTree
    :rtype: str

    >>> b1 = BinaryTree(3.0)
    >>> print(parenthesize(b1))
    3.0
    >>> b2 = BinaryTree(4.0)
    >>> b3 = BinaryTree(7.0)
    >>> b4 = BinaryTree("*", b1, b2)
    >>> b5 = BinaryTree("+", b4, b3)
    >>> print(parenthesize(b5))
    ((3.0 * 4.0) + 7.0)
    """
    if b.left is None and b.right is None:
        return str(b.data)
    else:
        return "({} {} {})".format(parenthesize(b.left),
                                   b.data,
                                   parenthesize(b.right))


def list_longest_path(node):
    """
    List the data in a longest path of node.

    :param node: tree to list longest path of
    :type node: BinaryTree|None
    :rtype: list[object]

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BinaryTree(5))
    [5]
    >>> b1 = BinaryTree(7)
    >>> b2 = BinaryTree(3, BinaryTree(2), None)
    >>> b3 = BinaryTree(5, b2, b1)
    >>> list_longest_path(b3)
    [5, 3, 2]
    """
    if node is None:
        return []
    else:
        path_left = list_longest_path(node.left)
        path_right = list_longest_path(node.right)
        if len(path_right) > len(path_left):
            return [node.data] + path_right
        else:
            return [node.data] + path_left


def insert(node, data):
    """
    Insert data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    :param node: root of a binary search tree.
    :type node: BinaryTree
    :param data: data to insert into BST, if necessary.
    :type data: object

    >>> b = BinaryTree(5)
    >>> b1 = insert(b, 3)
    >>> print(b1)
    5
        3
    <BLANKLINE>
    """
    return_node = node
    if not node:
        return_node = BinaryTree(data)
    elif data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    else:  # nothing to do
        pass
    return return_node


def max_value1(t):
    """
    Return the max value in BinaryTree t

    :param t: a not None binary tree
    :type t: BinaryTree
    :return: the maximum value in the tree
    :rtype: object

    >>> t1 = BinaryTree(8)
    >>> max_value1(t1)
    8
    >>> t2 = BinaryTree(8,BinaryTree(7,BinaryTree(12),BinaryTree(5)),BinaryTree(11))
    >>> max_value1(t2)
    12
    """
    # base case: no left or right child
    if t.left is None and t.right is None:
        return t.data

    # general case: recursively look up both ways
    else:
        return max([t.data, max_value1(t.left), max_value1(t.right)])

def max_value2(t):
    """
    Return the max value in BinaryTree t

    :param t: a not None binary tree
    :type t: BinaryTree
    :return: the maximum value in the tree
    :rtype: object

    >>> t1 = BinaryTree(8)
    >>> max_value2(t1)
    8
    >>> t2 = BinaryTree(8,BinaryTree(7,BinaryTree(12),BinaryTree(5)),BinaryTree(11))
    >>> max_value2(t2)
    12
    """
    # using Queue for level order traversal - Breadth First Search
    queue = Queue()
    record = t.data
    queue.add(t)
    while queue.is_empty() is False:
        extract = queue.remove()
        record = max(record, extract.data)
        if extract.left is not None:
            queue.add(extract.left)
        if extract.right is not None:
            queue.add(extract.right)
    return record


if __name__ == "__main__":
    import doctest
    doctest.testmod()
