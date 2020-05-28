# recursion exercises with nested lists


# we provide this helper function
def gather_lists(list_):
    """
    Return the concatenation of the sublists of list_.

    @param list[list] list_: list of sublists
    @rtype: list

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
    # this is equivalent to
    # sum(list_, [])


def list_all(obj):
    """
    Return a list of all non-list elements in obj or obj's sublists, if obj
    is a list.  Otherwise, return a list containing obj.

    :param obj: object to list
    :type obj: list|object
    :rtype: list

    >>> obj = 17
    >>> list_all(obj)
    [17]
    >>> obj = [1, 2, 3, 4]
    >>> list_all(obj)
    [1, 2, 3, 4]
    >>> obj = [[1, 2, [3, 4], 5], 6]
    >>> all([x in list_all(obj) for x in [1, 2, 3, 4, 5, 6]])
    True
    >>> all ([x in [1, 2, 3, 4, 5, 6] for x in list_all(obj)])
    True
    """
    if not isinstance(obj, list):
        return [obj]
    else:
        return gather_lists([list_all(x) for x in obj])


def max_length(obj):
    """
    Return the maximum length of obj or any of its sublists,
    if obj is a list.  Otherwise return 0.

    :param obj: object to return length of
    :type obj: object|list
    :rtype: int

    >>> max_length(17)
    0
    >>> max_length([1, 2, 3, 17])
    4
    >>> max_length([[1, 2, 3, 3], 4, [4, 5]])
    4
    """
    if not isinstance(obj, list):
        return 0
    else:
        return max([max_length(x) for x in obj] + [len(obj)])


def list_over(obj, n):
    """
    Return a list of strings of length greater than n in obj,
    or sublists of obj, if obj is a list.  Otherwise, if obj
    is a string return a list containing obj if obj has
    length greater than n, otherwise an empty list.

    :param obj: possibly nested list of strings, or string
    :type obj str|list
    :param n: non-negative integer
    :type n: int
    :rtype: list[str]

    >>> list_over("five", 3)
    ['five']
    >>> list_over("five", 4)
    []
    >>> L = list_over(["one", "two", "three", "four"], 3)
    >>> all([x in L for x in ["three", "four"]])
    True
    >>> all([x in ["three", "four"] for x in L])
    True
    """
    if not isinstance(obj, list) and len(obj) > n:
        return [obj]
    elif not isinstance(obj, list):
        return []
    else:
        return gather_lists([list_over(x, n) for x in obj])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
