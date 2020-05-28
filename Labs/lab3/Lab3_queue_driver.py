from csc148_queue import Queue

def list_queue(given_list, queue):
    """
    Break down any list to individual elements in a queue

    @param list given_list: a list
    @param Queue queue: a Queue
    @rtype: None
    >>> queue = Queue()
    >>> list_queue([1,3,5], queue)
    1
    3
    5
    >>> list_queue([1, [3, 5], 7], queue)
    1
    7
    3
    5
    >>> list_queue([1, [3, [5, 7], 9], 11], queue)
    1
    11
    3
    9
    5
    7
    """
    # add each element into a queue
    for item in given_list:
        queue.add(item)

    # repeat until queue is empty
    while len(queue._content) != 0:
        removed = queue.remove()
        if isinstance(removed, list):
            list_queue(removed, queue)
        else:
            print(removed)

if __name__ == "__main__":
    # create new queue
    queue = Queue()

    # ask for an integer
    response = int(input("please type in an integer:"))

    # repeat until sees 148, but not stored
    while response != 148:
        queue.add(response)
        response = int(input("please type in an integer:"))

    # print the sum of all numbers
    print(sum(queue._content))

    import doctest
    doctest.testmod()
