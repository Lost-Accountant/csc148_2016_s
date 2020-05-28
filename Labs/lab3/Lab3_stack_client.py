from stack import Stack

def list_stack(given_list, stack):
    """
    Break down any list to individual elements in a stack

    @param list given_list: a list
    @param Stack stack: a Stack
    @rtype: None

    >>> stack = Stack()
    >>> list_stack([1,3,5], stack)
    5
    3
    1
    >>> list_stack([1, [3, 5], 7], stack)
    7
    5
    3
    1
    >>> list_stack([1, [3, [5, 7], 9], 11], stack)
    11
    9
    7
    5
    3
    1
    """
    # add each element of the list to the stack
    for item in given_list:
        stack.add(item)

    # continue the following while stack not empty
    while len(stack._content) > 0:
        # remove the top element from the stack
        removed = stack.remove()
        if isinstance(removed, list):
            list_stack(removed, stack)
        else:
            print(removed)


if __name__ == "__main__":
    stack = Stack()

    response = input("Type a string:")
    stack.add(response)

    while response != 'end':
        response = input("Type a string:")
        stack.add(response)

    while len(stack._content) != 0:
        print(stack.remove())

    import doctest
    doctest.testmod()
