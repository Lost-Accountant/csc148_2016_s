from csc148_queue import Queue

class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """
    def __init__(self, value = None, children = None):
        """
        Create Tree self with content value and 0 or more children

        @param value: value contained in this tree
        @type value: object
        @param children: possibly empty list of children
        @type children: list[Tree]
        """
        self.value = value
        # copy if not none
        if children:
            self.children = children.copy()
        else:
            self.children = []

    def __repr__(self):
        """
        Return representation of Tree (self) as string that can be evaluated into an equivalent Tree.

        @return: str

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        root = "Tree({}".format(self.value)
        if len(self.children) == 0:
            child = ")"
        else:
            child = ", {})".format(self.children.__repr__())

        return root + child

    def __eq__(self, other):
        """
        Return whether this Tree is equivalent to other.

        @param other: object to compare to self
        @type other: object}Tree
        @rtype: bool

        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) == type(other) and \
                self.value == other.value and \
                self.children == other.children)

def leaf_count(t):
    """
    Return the number of leaves in Tree t.

    @param t: tree to count the leave of
    @type t: Tree
    @rtype: int
    >>> t = Tree(7)
    >>> leaf_count(t)
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> leaf_count(t)
    6
    """
    if len(t.children) == 0:
        # t is a leaf
        return 1
    else:
        # t is an internal node
        # general case
        return sum([leaf_count(x) for x in t.children])

def height(t):
    """
    Return 1 + length of longest path of t.

    @param t: tree to find height of
    @type t: Tree
    @rtype: int
    >>> t = Tree(13)
    >>> height(t)
    1
    >>> t = descendants_from_list(Tree(13), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> height(t)
    3
    """
    # base case: it is a leaf
    if len(t.children) == 0:
        return 1
    else:
        return 1 + max([height(x) for x in t.children])

def arity(t):
    """
    Return the maximum branching factor (arity) of Tree t.

    @param t: tree to find the arity of
    @type t: Tree
    @rtype: int
    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    4
    """
    # base case
    if len(t.children) == 0:
        return 0
    else:
        return max([len(t.children)] + [arity(x) for x in t.children])

def count(t):
    """
    Return the number of nodes in Tree t.

    @param t: tree to find number of nodes in
    @type t: Tree
    @rtype: int

    >>> t = Tree(17)
    >>> count(t)
    1
    >>> t4 = descendants_from_list(Tree(17), [0, 2, 4, 6, 8, 10, 11], 4)
    >>> count(t4)
    8
    """
    # base case
    if len(t.children) == 0:
        return 1
    else:
        return 1 + sum([count(x) for x in t.children])

def descendants_from_list(t, list_, arity):
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    :param t: tree to populate from list_
    :type t: Tree
    :param list_: list of values to populate from
    :type list_: list
    :param arity: maximum branching factor
    :type arity: int
    :rtype: Tree

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, arity):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t

def list_all(t):
    """
    Return list of values in t.

    @param t: tree to list values of
    @type t: Tree
    @rtype: list[object]

    >>> t = Tree(0)
    >>> list_all(t)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_all(t)
    >>> list_.sort()
    >>> list_
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    if len(t.children) == 0:
        return [t.value]
    # ultimately always returns a list
    else:
        return gather_lists(list_all(x) for x in t.children) + [t.value]

def gather_lists(list_):
    """
    Return the concatenation of the sublists of list_.

    :param list_: list of sublists
    :type list_: list[list]
    :rtype: list

    >>> list_ = [[1, 2], [3, 4]]
    >>> gather_lists(list_)
    [1, 2, 3, 4]
    """
    # this is a case where list comprehension gets a bit unreadable
    new_list = []
    for sub in list_:
        for element in sub:
            new_list.append(element)
    return new_list

if __name__ == "__main__":
    import doctest
    doctest.testmod()
