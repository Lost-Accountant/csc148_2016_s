# module-level functions, alternatively these could be implemented as methods,
# but then they might not be appropriate for every Tree
from tree import Tree
from csc148_queue import Queue


def arity(t):
    """
    Return the maximum branching factor (arity) of Tree t.

    :param t: tree to find the arity of
    :type t: Tree
    :rtype: int

    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    4
    """
    return max([len(t.children)] + [arity(n) for n in t.children])


def list_internal(t):
    """
    Return list of values in internal nodes of t.

    :param t: tree to list internal values of
    :type t: Tree
    :rtype: list[object]

    >>> t = Tree(0)
    >>> list_internal(t)
    []
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_internal(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    """
    if len(t.children) == 0:
        return []
    else:
        return [t.value] + gather_lists([list_internal(c) for c in t.children])


def contains_test_passer(t, test):
    """
    Return whether t contains a value that test(value) returns True for.

    :param t: tree to search for values that pass test
    :type t: Tree
    :param test: predicate to check values with
    :type test: (object)->bool
    :rtype: bool

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4.5, 5, 6, 7.5, 8.5], 4)
    >>> def greater_than_nine(n): return n > 9
    >>> contains_test_passer(t, greater_than_nine)
    False
    >>> def even(n): return n % 2 == 0
    >>> contains_test_passer(t, even)
    True
    """
    return test(t.value) or any([test(c.value) for c in t.children])


# helper function that may be useful in the functions
# above
def gather_lists(list_):
    """
    Concatenate all the sublists of L and return the result.

    @param list[list[object]] list_: list of lists to concatenate
    @rtype: list[object]

    >>> gather_lists([[1, 2], [3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> gather_lists([[6, 7], [8], [9, 10, 11]])
    [6, 7, 8, 9, 10, 11]
    """
    new_list = []
    for l in list_:
        new_list += l
    return new_list


# helpful helper function
def descendants_from_list(t, list_, branching):
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to branching children per node.
    Then return t.

    @param Tree t: tree to populate from list_
    @param list list_: list of values to populate from
    @param int branching: maximum branching factor
    @rtype: Tree

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, branching):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t

def count_odd(lst):
    if isinstance(lst, int):
        return lst % 2
    else:
        for element in lst:
            return count_odd(element)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(count_odd(1))
    print(count_odd([2,6,5]))
    print(count_odd([9,[8,7]]))
