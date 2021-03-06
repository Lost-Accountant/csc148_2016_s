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

        :rtype: str

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
    # when no 2 children
    # base case
    if not b.left or not b.right:
        return b.data
    # when has children
    else:
        #  recursion
        # general case
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
    l = []
    # base case 1: no nodes:
    if not node:
        return l
    # base case 2: no further nodes
    if node.left is None and node.right is None:
        return l + [node.data]

    # general case: recursion
    else:
        if len(list_longest_path(node.left)) < len(list_longest_path(node.right)):
            return l + [node.data] + list_longest_path(node.right)
        else:
            return l + [node.data] + list_longest_path(node.left)


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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
