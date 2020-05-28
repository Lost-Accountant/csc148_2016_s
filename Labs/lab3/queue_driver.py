from csc148_queue import Queue


def list_queue(list_, q):
    """
    Add elements of list_ to q, and then print all
    the non-list elements in an interesting order.

    q is assumed to be empty.

    @param list list_: a Python list, possibly noted
    @param Queue q: an empty queue
    @rtype: None
    """
    for i in list_:
        q.add(i)
    while not q.is_empty():
        el = q.remove()
        if isinstance(el, list):
            for j in el:
                q.add(j)
        else:
            print(el)


if __name__ == "__main__":
    queue_ = Queue()
    s = input("Type an integer: ")
    while not s == "148":
        queue_.add(s)
        s = input("Type an integer: ")
    sum = 0
    while not queue_.is_empty():
        sum += int(queue_.remove())
    print("total: {}".format(sum))

    list_queue([1, [3, [5, 7], 9], 11], Queue())
