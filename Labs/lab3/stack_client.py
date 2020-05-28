from stack import Stack


def list_stack(list_, st):
    """
    Add elements of list_ to Stack st, and then print all
    the non-list elements in an interesting order.

    st is assumed to be empty.

    @param list list_: a Python list, possibly noted
    @param Stack st: an empty Stack
    @rtype: None
    """
    for i in list_:
        st.add(i)
    print(st)
    while not st.is_empty():
        el = st.remove()
        if isinstance(el, list):
            for j in el:
                st.add(j)
        else:
            print(el)

if __name__ == "__main__":
    stack_ = Stack()
    s = input("Type a string: ")
    while not s == "end":
        stack_.add(s)
        s = input("Type a string: ")
    while not stack_.is_empty():
        print(stack_.remove())

    list_stack([1, [3, [5, 7], 9], 11], Stack())
