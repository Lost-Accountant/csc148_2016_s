def list_even(obj):
    """
    Return a list of all even integers in obj or sublists of obj, if obj is a list.
    Otherwise, if obj is an even integer return a list containing obj, and if obj
    is an odd integer, return an empty list.

    :param obj: possibly nested list of ints, or int
    :type obj: int|list
    :rtype: list[int]

    >>> list_even(3)
    []
    >>> list_even(16)
    [16]
    >>> L = list_even([1, 2, 3, 4, 5])
    >>> all([x in L for x in [2, 4]])
    True
    >>> all([x in [2, 4] for x in L])
    True
    >>> L = list_even([1, 2, [3, 4], 5])
    >>> all([x in L for x in [2, 4]])
    True
    >>> all([x in [2, 4] for x in L])
    True
    >>> L = list_even([1, [2, [3, 4]], 5])
    >>> all([x in L for x in [2, 4]])
    True
    >>> all([x in [2, 4] for x in L])
    True
    """
    # base case
    if not isinstance(obj, list):
        # return even number only
        if obj % 2 == 0:
            return [obj]
        else:
            return []
    # general case
    else:
        return gather_list([list_even(x) for x in obj])


def count_even(obj):
    """
    Return the number of even numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 1
    if it is an even number and 0 if it is an odd number.

    :param obj: object to count even numbers from
    :type obj: int|list
    :rtype: int

    >>> count_even(3)
    0
    >>> count_even(16)
    1
    >>> count_even([1, 2, [3, 4], 5])
    2
    """
    # base case
    # when not list
    if not isinstance(obj, list):
        # return 1 if even and 0 for odds
        return (obj + 1) % 2
    # general case
    else:
        return sum([count_even(x) for x in obj])


def count_all(obj):
    """
    Return the number of elements in obj or sublists of obj if obj is a list.
    Otherwise, if obj is a non-list return 1.

    :param obj: object to count
    :type obj: object|list
    :rtype: int

    >>> count_all(17)
    1
    >>> count_all([17, 17, 5])
    3
    >>> count_all([17, [17, 5], 3])
    4
    """
    # base case, when encounter non list
    if not isinstance(obj, list):
        return 1
    else:
        return sum([count_all(x) for x in obj])


def count_above(obj, n):
    """
    Return tally of numbers in obj, and sublists of obj, that are over n, if
    obj is a list.  Otherwise, if obj is a number over n, return 1.  Otherwise
    return 0.

    >>> count_above(17, 19)
    0
    >>> count_above(19, 17)
    1
    >>> count_above([17, 18, 19, 20], 18)
    2
    >>> count_above([17, 18, [19, 20]], 18)
    2
    """
    # base case, when not list
    if not isinstance(obj, list):
        if obj > n:
            return 1
        else:
            return 0
    # general case
    else:
        return sum([count_above(x, n) for x in obj])

def gather_list(lst):
    output = []
    for element in lst:
        for item in element:
            output.append(item)
    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()
