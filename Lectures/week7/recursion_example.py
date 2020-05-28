def Msort(l):
    """
    Merge sort.

    @param l: a list to be sorted
    @type l: list
    @rtype: list
    @return: a sorted list of l

    >>> print(Msort([3,2,1]))
    [1, 2, 3]
    >>> print(Msort([2,4,6,1,5,2,5,6,7,4,2,5,6,9,6,31,2,8,9,3,0]))
    [0, 1, 2, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 9, 9, 31]
    """
    # when still lists of elements, GENERAL CASE
    if len(l) > 1:
        # break down from midpoint
        midpoint = len(l)//2
        s1 = l[:midpoint]
        s2 = l[midpoint:]

        # continue to breakdown
        Msort(s1)
        Msort(s2)
        # once reach base case, would just return itself

        # create 3 index to track
        i = j = k = 0
        while i < len(s1) and j < len(s2):
            # pick the small one out first
            if s1[i] < s2[j]:
                l[k] = s1[i]
                i += 1
            else:
                l[k] = s2[j]
                j += 1
            # no matter what, temp index always moves up
            k += 1

        # one of the list exhausted
        # the other might not be
        while i < len(s1):
            l[k] = s1[i]
            i += 1
            k += 1
        while j < len(s2):
            l[k] = s2[j]
            j += 1
            k += 1
    return l

def Qsort(l):
    """

    @param l:
    @rtype: list
    >>> print(Qsort([3,2,1]))
    [1, 2, 3]
    >>> print(Qsort([2,4,6,1,5,2,5,6,7,4,2,5,6,9,6,31,2,8,9,3,0]))
    [0, 1, 2, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 9, 9, 31]
    """
    QsortHelper(l, 0, len(l) - 1)
    return l

def QsortHelper(l, low, high):
    if low < high:
        p = partition(l, low, high)
        QsortHelper(l, low, p-1)
        QsortHelper(l, p+1, high)
    return l

def partition(l, low, high):
    # high as the pivot
    follower = leader = low
    # follower is last seen small element
    while leader < high:
        if l[leader] <= l[high]:
            # swap
            l[follower], l[leader] = l[leader], l[follower]
            follower += 1
        leader += 1
        # swap pivot and last small element
    l[follower], l[high] = l[high], l[follower]
    return follower

# 2 ways of fib(n)
# https://www.geeksforgeeks.org/memoization-1d-2d-and-3d/

def Hanoi(n, s, d, aux):
    if n == 1:
        print("move disk ",n,"from source ", s, "to destination ", d)
    else:
        Hanoi(n-1, s, aux, d)
        print("move disk ",n,"from source ", s, "to destination ", d)
        Hanoi(n-1, aux, d, s)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    n = 3
    Hanoi(n, 'a','b','c')
