# === Selection sort === #


def find_min(list_, i):
    """
    Return the index of the smallest item in list_[i:].

    :param list_: list to search
    :type list_: list
    :param i: index to search from
    :type i: int
    :rtype: int

    >>> find_min([1, 2, 3], 1)
    1
    """
    smallest = i
#    for j in range(i + 1, len(list_)):
    list_len = len(list_)
    for j in range(i + 1, list_len):
        if list_[j] < list_[smallest]:
            smallest = j
    return smallest


# find_min using built-in min, tuple comparisons, and enumerate
# should be faster...
# def find_min(list_, i):
    # """Return index of smallest item in list_[i:]."""
    # return min([(k, j) for j, k in enumerate(list_[i:])])[1] + i


def selection_sort(list_):
    """
    Sort the items in list_ in non-decreasing order.

    :param list_: list to sort
    :type list_:list
    :rtype: None
    """
    i = 0
    list_len = len(list_)
    #while i != list_len - 1:
    for i in range(list_len):
        # Find the smallest remaining item and move it to index i.
        smallest = find_min(list_, i)
        list_[smallest], list_[i] = list_[i], list_[smallest]
        i += 1


# === Insertion sort 1 === #
def insert(list_, i):
    """
    Move list_[i] to where it belongs in list_[:i]

    :param list_: list to modify
    :type: list_:list
    :param i: index of element to place
    :type i:int
    :rtype: None
    """
    v = list_[i]
    while i > 0 and list_[i - 1] > v:
        list_[i] = list_[i - 1]
        i -= 1
    list_[i] = v


def insertion_sort_1(list_):
    """
    Sort the items in list_ in non-decreasing order.

    :param list_: list to sort
    :type list_: list
    :rtype: None
    """
    i = 1
    # Insert each item i where it belongs in list_[0:i + 1]
    while i != len(list_):
        insert(list_, i)
        i += 1


# === Insertion sort 2 === #
def find_insertion_point(list_, i):
    """
    Return the index where list_[i] belongs in list_[:i + 1].

    :param list_: list to find insertion point in
    :type list_: list
    :param int i: index of element to insert
    :type i: int
    :rtype: int

    >>> find_insertion_point([1, 3, 2], 2 )
    1
    """
    v = list_[i]
    while i > 0 and list_[i - 1] > v:
        i -= 1
    return i


def insertion_sort_2(list_):
    """
    Sort the items in list_ in non-decreasing order.

    :param list_: list to sort
    :type list_: list
    :rtype: None
    """
    i = 1
    # Insert each item i where it belongs in list_[0:i + 1]
    while i != len(list_):
        the_spot = find_insertion_point(list_, i)
        v = list_[i]
        del list_[i]
        list_.insert(the_spot, v)
        i += 1


# === Bubblesort 1 == #
def bubblesort_1(list_):
    """
    Sort the items in list_ in non-decreasing order.

    :param list_: list to sort
    :type list_: list
    :rtype: None
    """
    j = len(list_) - 1
    while j != 0:
        # Swap every item that is out of order.
        for i in range(j):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
        j -= 1


# === Bubblesort 2 === #
def bubblesort_2(list_):
    """
    Sort the items in list_ in non-decreasing order.

    :param list_: list to sort
    :type list_: list
    :rtype: None
    """
    j = len(list_) - 1
    swapped = True
    # Stop when no elements are swapped.
    while swapped and j != 0:
        swapped = False
        # Swap every item that is out of order.
        for i in range(j):
            if list_[i] > list_[i + 1]:
                swapped = True
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
        j -= 1


# === Mergesort 1 === #
def _merge_1(left, right):
    """
    Merge sorted lists left and right into a new list and return that new
    list.

    :param left: left elements of desired list
    :type left: list
    :param list right: right elements of desired list
    :type right: list
    :rtype: list

    >>> _merge_1([1, 3, 5], [2, 4,6])
    [1, 2, 3, 4, 5, 6]
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def _mergesort_1(list_):
    """
    Return a new list that is a sorted version of list list_.

    :param list_: list to sort from
    :type list_: list
    :rtype: list

    >>> _mergesort_1([5, 1, 3])
    [1, 3, 5]
    """
    if len(list_) < 2:
        return list_[:]
    else:
        middle = len(list_) // 2
        left = _mergesort_1(list_[:middle])
        right = _mergesort_1(list_[middle:])
    return _merge_1(left, right)


def mergesort_1(list_):
    """
    Sort list list_ in non-decreasing order.

    :param list_: list to sort
    :type list_: list
    :rtype: None
    """
    list_[:] = _mergesort_1(list_)


# === Mergesort 2 === #
def _merge_2(list_, i, mid, j):
    """
    Merge the two sorted halves list_[i:mid + 1] and
    list_[mid + 1:j + 1] and return them in a new list.
    Notice that list_[mid] belongs in the left half and list_[j]
    belongs in the right half -- the indices are inclusive.

    :param list list_: list to sort
    :type list_: list
    :param int i: starting index for first half of list to sort
    :type i: int
    :param int mid: index for middle of list to sort
    :type mid: int
    :param j: index for end of list to sort
    :type j: int

    >>> _merge_2([1, 3, 5, 2, 4, 6], 0, 2, 5)
    [1, 2, 3, 4, 5, 6]
    """
    result = []
    left = i
    right = mid + 1
    # Done when left > mid or when right > j; i.e.,
    # when we've finished one of the halves.
    while left <= mid and right <= j:
        if list_[left] < list_[right]:
            result.append(list_[left])
            left += 1
        else:
            result.append(list_[right])
            right += 1
    # Items left: list_[left:mid + 1]
    #             list_[right:j + 1]
    return result + list_[left:mid + 1] + list_[right:j + 1]


def _mergesort_2(list_, i, j):
    """
    Sort the items in list_[i] through list_[j] in
    non-decreasing order.

    :param list_: list to sort
    :type list_: list
    :param int i: index to begin sorting from
    :type int: int
    :param int j: index to continue sorting until
    :type j: int
    :rtype: None
    """
    if i < j:
        mid = (i + j) // 2
        _mergesort_2(list_, i, mid)
        _mergesort_2(list_, mid + 1, j)
        list_[i:j + 1] = _merge_2(list_, i, mid, j)


def mergesort_2(list_):
    """
    Sort list list_ in non-decreasing order.

    :param list_: list to sort
    :type list_: list
    :rtype: None
    """
    _mergesort_2(list_, 0, len(list_) - 1)


# === Quicksort 1 === #
def _partition_1(list_):
    """
    Rearrange list_ so that items < list_[0] are at the beginning
    and items >= list_[0] are at the end, and return the new index
    for list_[0].

    :param list_: list to partition
    :type list_: list
    :rtype: int

    >>> _partition_1([2, 1, 3])
    1
    """
    v = list_[0]
    i = 1
    j = len(list_) - 1
    while i <= j:
        if list_[i] < v:
            i += 1
        else:
            list_[i], list_[j] = list_[j], list_[i]
            j -= 1
    list_[0], list_[j] = list_[j], list_[0]
    return j


def _quicksort_1(list_):
    """
    Sort list_ by partitioning it around the first item,
    then recursing.

    :param list_: list to sort
    :type list_: list
    :rtype: list

    >>> _quicksort_1([3, 1, 2, 5])
    [1, 2, 3, 5]
    """
    if len(list_) <= 1:
        return list_
    else:
        pivot = _partition_1(list_)
        left = list_[:pivot]
        right = list_[pivot + 1:]
        return _quicksort_1(left) + [list_[pivot]] + _quicksort_1(right)


def quicksort_1(list_):
    """
    Sort list list_ in non-decreasing order.

    :param list_: list to sort
    :type list_: list
    :rtype: None
    """
    list_[:] = _quicksort_1(list_)


# === Quicksort 2 === #
def _partition_2(list_, i, j):
    """Rearrange list_[i:j] so that items < list_[i] are at
    the beginning and items >= list_[i] are at the end,
    and return the new index for list_[i].

    :param list_: list to partition
    :type list_: list
    :param i: beginning of partition slice
    :type i: int
    :param j: end of partition slice
    :type j: int
    :rtype: int

    >>> _partition_2([1, 5, 2, 4, 3], 1, 4)
    3
    """
    v = list_[i]
    k = i + 1
    j -= 1
    while k <= j:
        if list_[k] < v:
            k += 1
        else:
            list_[k], list_[j] = list_[j], list_[k]
            j -= 1
    list_[i], list_[j] = list_[j], list_[i]
    return j


def _quicksort_2(list_, i, j):
    """
    Sort list_[i:j] by partitioning it around the first item,
    then recursing.

    :param list_: list to sort
    :type list_: list
    :param int i: index to begin sorted slice
    :type i: int
    :param int j: index to end sorted slice
    :type j: int
    :rtype: None
    """
    if i < j:
        pivot = _partition_2(list_, i, j)
        _quicksort_2(list_, i, pivot)
        _quicksort_2(list_, pivot + 1, j)


def quicksort_2(list_):
    """
    Sort list list_ in non-decreasing order.

    :param list_: list to sort
    :type list_: list
    :rtype: None
    """
    _quicksort_2(list_, 0, len(list_))
