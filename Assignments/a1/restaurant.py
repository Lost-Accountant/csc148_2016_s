from customer import Customer

class Restaurant(object):
    """A Restaurant.

    This class represents a restaurant in the simulation. This is the base
    class for different restaurant approaches. The main purpose of this
    class to define common interfaces for different approaches. If there
    are common tasks for all approaches that did not depend on a specific
    management style, they should be implemented here. Otherwise, they should
    be implemented in the subclasses.

    This class is abstract; subclasses must implement add_customer and
    process_turn functions.

    You may, if you wish, change the API of this class to add
    extra public methods or attributes. Make sure that anything
    you add makes sense for ALL approaches, and not just a particular
    approach.

    """

    # === Private Attributes ===
    # :type _waiting_list: List[Customer]
    #   The list of customer currently waiting
    # :type _accumulated_profit: float
    #   The accumulated profit earned from serving customers
    # :type _number_served: int
    #   The accumulated number of customers served
    # :type _order_in_progress: Customer
    #   The customer whose order is being processed.
    # TODO: Complete this part

    def __init__(self):
        """Initialize a restaurant.
        """
        self._accumulated_profit = 0.0
        self._number_served = 0
        self._order_in_progress = None
        self._waiting_list = []
        #TODO: Complete this part


    def add_customer(self, new_customer):
        """
        Add a new entering customer to the restaurant.

        :type new_customer: Customer
            The new customer that is entering the restaurant
        :rtype: None
        """
        self._waiting_list.append(new_customer)

    def process_turn(self, current_turn):
        """Process the current_turn.

        This function will process the current turn. If the restaurant is not
        serving any customer now, and there are waiting customers, it should
        select one of them to serve.

        You can assume that all customers who entered the restaurant before or
        during this turn were already passed to the restaurant by simulator via
        calling the AddCustomer function.

        :type self: Restaurant
        :type current_turn: int
        :param current_turn: The number indicating current turn
        :rtype: None
        """
        # currently no customer, do nothing
        if self._order_in_progress is not None:
            # not reached patience
            if self._order_in_progress._patience > \
                    current_turn - self._order_in_progress._entry_time:
                if self._order_in_progress._prepare_time == \
                        current_turn - self._order_in_progress._entry_time:
                    self._accumulated_profit += self._order_in_progress._profit
                    self._number_served += 1
                    self._order_in_progress = None
            else:
                self._order_in_progress = None

    def write_report(self, report_file):
        """
        Write the final report of this restaurant approach in the report_file.

        :type self: Restaurant
        :type report_file: File
            This is an open file that this restaurant will write the report into.
        :rtype: None
        """

        report_file.write("Total profit: ${} \nCustomer served: {}\n".format(self._accumulated_profit, self._number_served))
        #TODO: Complete this part


class PatApproach(Restaurant):
    """A Restaurant with Pat management style.

    This class represents a restaurant that uses the Pat management style,
    in which customers are served based on their arrival time. This class is
    a subclass of Restaurant and implements two functions: write_report and
    add_customer.

    """
    # FIFO, Queue structure

    def add_customer(self, new_customer):
        """
        Add a new customer to the restaurant waiting list and preparation list, if no order is being processed, with the first one being served first.

        Extends from Restaurant.add_customer

        :@type new_customer: Customer
        :@param new_customer: The new customer that is entering the restaurant.
        :@rtype: None

        """
        super().add_customer(new_customer)
        # if no order being processed, add new customer based on first arrival
        if self._order_in_progress is None:
            self._order_in_progress = self._waiting_list.pop(0)


    def write_report(self, report_file):
        """
        Write the final report of Pat restaurant approach in the report_file.

        Extends from Restaurant.write_report

        :type self: PatApproach
        :type report_file: file
        :param report_file: This is an open file that PatApproach writes the report into.
        :rtype: None
        """

        report_file.write("Results for the serving approach using Pat's suggestion:\n")
        super().write_report(report_file)


class MatApproach(Restaurant):
    """
    A Restaurant with Mat management style.

    This class represents a restaurant that uses the Mat management style, in which customers are served on their arrival time, serving the last one in line.
    This class is a subclass of Restaurant and implements write_report and process_turn.

    """
    #LIFO, Stack structure

    def add_customer(self, new_customer):
        """
        Add a new customer to the restaurant waiting list and preparation list, if no order is being processed, with the last one being served first.

        Extends from Restaurant.add_customer

        :@type new_customer: Customer
        :@param new_customer: The new customer that is entering the restaurant.
        :@rtype: None

        """
        super().add_customer(new_customer)
        # if no order being processed, add new customer from the last arrival
        if self._order_in_progress is None or \
                new_customer._entry_time == self._order_in_progress._entry_time:
            # replaced by the lastest in line but arrived at same time
            # due to simulator only adding 1 customer per turn
            # but multiple people could have arrived at the same time
            self._order_in_progress = self._waiting_list.pop(-1)

    def write_report(self, report_file):
        """
        Write the final report of Pat restaurant approach in the report_file.

        Extends from Restaurant.write_report.

        :type report_file: file
        :type self: MatApproach
        :param report_file:  This is an open file that MatApproach write the report into.
        :rtype: None
        """
        report_file.write("Results for the serving approach using Mat's suggestion:\n")
        super().write_report(report_file)


class MaxApproach(Restaurant):
    """
    A Restaurant with Max management style.

    This class represents a restaurant that uses the Max management style, in which customers are served on their profit, serving the one with highest profit first.
    This class is a subclass of Restaurant and implements write_report and process_turn.

    """
    # priority queue on profit.

    def add_customer(self, new_customer):
        """
        Add a new customer to the restaurant waiting list and preparation list,
        if no oder is being processed, with the one with the highest profit being served first.

        :@type new_customer: Customer
        :@param new_customer: The new customer that is entering the restaurant.
        :@rtype: None
        """
        super().add_customer(new_customer)
        # if no order being processed
        if self._order_in_progress is None:
            # get the one with highest profit
            ind = 0
            for i in range(len(self._waiting_list)):
                if self._waiting_list[i]._profit \
                        > self._waiting_list[ind]._profit:
                    ind = i
            # after loop, ind directs to one with highest profit
            self._order_in_progress = self._waiting_list.pop(ind)

        # if added by the simulator on next turn but actually entered at same time
        # serve the one with highest profit first
        elif new_customer._entry_time == self._order_in_progress._entry_time \
            and new_customer._profit > self._order_in_progress._profit:
            self._order_in_progress = new_customer

    def write_report(self, report_file):
        """
        Write the final report of Max restaurant appraoch in the report_file.

        Extends from Restaurant.write_report

        :type self: MaxApproach
        :type report_file: file
        :param report_file: This is an open file that MaxApproach writes the report into
        :rtype: None
        """

        report_file.write("Results for the serving approach using Max's suggestion:\n")
        super().write_report(report_file)

class PacApproach(Restaurant):
    """
    A Restaurant with Pac management style.

    This class represents a restaurant that uses the Pac management style,
    in which customers are served based on their arrival time.
    This class is a subclass of Restaurant and implements two functions:
    write_report and add_customer.

    """
    # priority queue on prepare_time

    def add_customer(self, new_customer):
        """
        Add a new customer to the restaurant waiting list and preparation list,
        if no order is being processed, with the one with the shortest preparation time being served first.

        :@type new_customer: Customer
        :@param new_customer: The new customer that is entering the restaurant.
        :@rtype: None
        """
        super().add_customer(new_customer)
        # if no order is being processed
        if self._order_in_progress is None:
            # get the one with the shortest serving time
            ind = 0
            for i in range(len(self._waiting_list)):
                if self._waiting_list[i]._prepare_time \
                        < self._waiting_list[ind]._prepare_time:
                    ind = i
            # after loop, ind directs to the one with lowest serving time
            self._order_in_progress = self._waiting_list.pop(ind)
        # if added by the simulator on next turn but actually entered at same time
        # serve the one with lowest serving time first
        elif new_customer._entry_time == self._order_in_progress._entry_time \
                and new_customer._prepare_time \
                < self._order_in_progress._prepare_time:
            self._order_in_progress = new_customer

    def write_report(self, report_file):
        """
        Write the final report of Pac restaurant appraoch in the report_file.

        Extends from Restaurant.write_report

        :type self: PacApproach
        :type report_file: file
        :param report_file: This is an open file that MaxApproach writes the report into
        :rtype: None
        """

        report_file.write("Results for the serving approach using Pac's suggestion:\n")
        super().write_report(report_file)

#TODO: Complete this part
if __name__ == "__main__":
    import doctest
    doctest.testmod()

