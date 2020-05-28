
class Customer:
    """A Customer.

    This class represents a customer in the simulation. Each customer will
    enter the simulation at _entry_time, will wait at most _patience turns.
    The restaurant need _prepare_time turns to prepare this customer order,
    and will receive _profit if can serve this customer on time.

    Your main task is to implement the remaining methods.
    """

    # === Private Attributes ===
    # :type _entry_time: int
    #   The turn time when a customer walks in
    # :type _id: str
    #   A unique id that is used to easily identify that customer
    # :type _profit: float
    #   The profit the restaurant will earn if served
    # :type _prepare_time: int
    #   The number of turns needed to prepare the order
    # :type _patience: int
    #   The maximum number of turns that this customer will wait for their order



    def __init__(self, definition):
        """
        Initialize a customer profile

        :type definition: str
        :param definition: a string with all information separated by tab
        """
        info = definition.split()
        # entry time is int
        self._entry_time = int(info[0])
        # id is str
        self._id = info[1]
        # profit is float
        self._profit = float(info[2])
        # rest are int
        (self._prepare_time, self._patience) = \
            (int(info[3]), int(info[4]))

    def __eq__(self, other):
        """
        Determine whether two customer profile are equal.

        :param other: another customer profile
        :type other: Customer
        :rtype: bool
        >>> a = Customer("3\t38623\t11\t8\t3")
        >>> b = Customer("3\t38623\t11\t8\t3")
        >>> a.__eq__(b)
        True
        >>> c = Customer("3\t38623\t12\t8\t5")
        >>> a == c
        False
        """
        return type(self) == type(other) and \
               (self._entry_time, self._id, self._profit, self._prepare_time, self._patience) == \
               (other._entry_time, other._id, other._profit, other._prepare_time, other._patience)

    def id(self):
        """
        Return the id of this Customer self

        :rtype: str

        >>> a = Customer("3\t38623\t11\t8\t3")
        >>> print(a.id())
        38623
        """
        return self._id

    def entry_turn(self):
        """
        Return the turn when the Customer self walks into the restaurant.

        :rtype: int

        >>> a = Customer("3\t38623\t11\t8\t3")
        >>> print(a.entry_turn())
        3
        """
        return self._entry_time

    def patience(self):
        """
        Return the maximum number of turns the Customer self will wait for their order.

        :rtype: int

        >>> a = Customer("3\t38623\t11\t8\t3")
        >>> print(a.patience())
        3
        """
        return self._patience
    # TODO: Complete this part

if __name__ == "__main__":
    import doctest
    doctest.testmod()
