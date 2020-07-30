from csc148_queue import Queue

class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
    """

    def __init__(self, data, left = None, right = None):
        """
        Create BinaryTree self with data and children left and right.

        @param BinaryTree self: this binary tree.
        @param object data: data of this node
        @param BinaryTree|None left: left child
        @param BinaryTree|None right: right child
        @rtype: None
        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other):
        """
        Return whether BinaryTree self is equivalent to other.

        :param BinaryTree self: this binary tree
        :param Any other: object to check equivalence to self
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

        :param BinaryTree self: this binary tree
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

def bst_contains(node, value):
    """
    Return whether tree rooted at node contains vlaue.

    Assume node is the root of a Binary Search Tree.

    @param node:  node of a Binary Search Tree
    @type node: BinaryTree|None
    @param value: value to search for
    @type value: object
    @rtype: bool

    >>> bst_contains(None, 5)
    False
    >>> bst_contains(BinaryTree(7, BinaryTree(5), BinaryTree(9)), 5)
    True
    """
    # base case, reach empty node
    if node is None:
        return False
    # general case, search value, left or right.
    else:
        if value == node.data:
            return True
        elif value < node.data:
            return bst_contains(node.left, value)
        else:
            return bst_contains(node.right, value)

def insert(node, data):
    """
    Insert data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    @param node: root of a binary search tree.
    @type node: BinaryTree
    @param data: data to insert into BST, if necessary.
    @type data: object
    >>> b = BinaryTree(5)
    >>> b1 = insert(b, 3)
    >>> print(b1)
    5
        3
    <BLANKLINE>
    """
    return_node = node
    if node.data == data:
        return node
    elif data < node.data:
        if node.left is None:
            return_node.left = BinaryTree(data)
        else:
            # keep exploring
            insert(node.left, data)
    elif data > node.data:
        if node.right is None:
            return_node.right = BinaryTree(data)
        else:
            insert(node.right, data)
    return return_node
