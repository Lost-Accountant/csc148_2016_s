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

def bst_insert(node, data):
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

def bst_delete(node, data):
    """
    Delete data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    @param node: a Binary Search Tree
    @type node: BinaryTree
    @param data: an object to be deleted
    @type data: object
    @rtype: bool

    >>> b = BinaryTree(5)
    >>> b1 = bst_insert(b, 3)
    >>> b2 = bst_insert(b1, 8)
    >>> bst_delete(b2, 3)
    True
    >>> print(b2)
        8
    5
    <BLANKLINE>
    """
    # locate node to be deleted and its parent
    parent, current = None, node
    # search node to be deleted
    while current is not None and current.data != data:
        # search left
        if data < current.data:
            parent = current
            current = current.left
        elif data > current.data:
            parent = current
            current = current.right
        else: # found equal value
            pass
    # end of loop, either found it or reach none
    if current is None:
        return False

    # Situation 1: No left child
    if current.left is None:
        # connect parent to current's right subtree
        # situation a): parent is None, current is root node
        if parent is None:
            current = current.right
        else: # situation b): has not-none parent
            # which side is current on for parent's subtree
            # help locate location of current's right subtree for parent
            if data < parent.data:
                # left side
                parent.left = current.right
            else:
                # right side
                parent.right = current.right
    # Situation 2: Has left child
    else:
        # additional locator for right most and its parent
        right_most, parent_right_most = current.left, current
        # locating process
        while right_most.right is not None: # not reach empty right yet
            parent_right_most = right_most
            right_most = right_most.right
        # replacing process
        # 1) copy value of right most to current
        current.data = right_most.data
        # 2) eliminate right most
        # situation a): parent of right most is current (right most left side)
        if parent_right_most.right != right_most:
            parent_right_most.left = right_most.left
        # situation b): parent of right most is not current (right most right side)
        else:
            parent_right_most.right = right_most.left
    return True # successfully delete a node

def BST_delete_alt(node, data):
    """
    Delete data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    @param node: a Binary Search Tree
    @type node: BinaryTree
    @param data: an object to be deleted
    @type data: object
    @rtype: bool

    >>> b = BinaryTree(5)
    >>> b1 = bst_insert(b, 3)
    >>> b2 = bst_insert(b1, 8)
    >>> bst_delete(b2, 3)
    True
    >>> print(b2)
        8
    5
    <BLANKLINE>
    """
    # locate the node to be deleted and its parent node
    parent, current = None, node
    # find node that matches value
    while current is not None and data != current.data:
        # which way to search
        if data < current.data:
            parent = current
            current = current.left
        elif data > current.data:
            parent = current
            current = current.right
        else:
            pass
    # might reach empty node
    if current is None:
        return False

    # Situation 1: no right child
    if current.right is None:
        # parent is none
        if parent is None:
            current = current.left
        # parent not none
        else:
            # which side is left subtree attached to parent node
            if data < parent.data:
                parent.left = current.left
            else:
                parent.right = current.right
    # Situation 2: has right child
    else:
        # 1) Locate left most and its parent
        left_most, parent_left_most = current.right, current
        while left_most.left is not None:
            parent_left_most = left_most
            left_most = left_most.left
        # 2) copy left most value to current
        current.data = left_most.data
        # 3) link parent to right child of left most
        # Special case: if parent of left most is current,
        # left most is at right side, but normally left side
        if parent_left_most.left != left_most:
            parent_left_most.right = left_most.right
        else:
            parent_left_most.left = left_most.right
        return True


def bst_del_rec(tree, data):
    """
    Delete data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    @param tree: a Binary Search Tree
    @type tree: BinaryTree
    @param data: an object to be deleted
    @type data: object
    @rtype: bool

    >>> b = BinaryTree(5)
    >>> b1 = bst_insert(b, 3)
    >>> b2 = bst_insert(b1, 8)
    >>> bst_delete(b2, 3)
    True
    >>> print(b2)
        8
    5
    <BLANKLINE>
    """
    # base case 1: reach empty node
    if tree is None:
        return None

    # general case 1: find target node at left or right
    elif data < tree.data:
        tree.left = bst_del_rec(tree.left, data)
    elif data > tree.data:
        tree.right = bst_del_rec(tree.right, data)

    # base case 2: find target node
    else:
        # situation 1: no left child
        if tree.left is None:
            return tree.right
        # situation 2: has left child
        else:
            # locate (right most from left child)
            largest = findmax(tree.left)
            # replace
            tree.data = largest.data
            # connect (get rid of right most from left child)
            tree.left = bst_del_rec(tree.left, largest.data)
            return tree

def findmax(tree):
    """
    Return the right most node in a tree
    @param tree: a Binary Search Tree
    @type tree: BinaryTree
    """
    return tree if tree.right is None else findmax(tree.right)
