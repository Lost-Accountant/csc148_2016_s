from _collections import deque

class Network(object):
    """A pyramid network.

    This class represents a pyramid network. The network topology can be loaded
    from a file, and it can find the best arrest scenario to maximize the seized
    asset.

    You may, if you wish, change the API of this class to add extra public
    methods or attributes. Make sure that you do not change the public methods
    that were defined in the handout. Otherwise, you may fail test results for
    those methods.

    """

    # === Attributes ===
    def __init__(self, name=None, asset=None, child=None):
        """
        Create a Network self with content value of its name, asset,
        rank as children itself, and 0 or more children

        @param name: the name of the person in the Network
        @type name: str
        @param asset: the asset value held by the person
        @type asset: int
        @param child: the children of itself, possibly an empty list
        @type child: list[Network]
        """
        self.name = name
        self.asset = asset
        self.child = child.copy() if child else []

    def __repr__(self):
        """
        Return representation of Network (self) as string that can be evaludated
        into an equivalent Network

        @rtype: str

        >>> n1 = Network("John", 100)
        >>> n1
        Network('John', $100)
        >>> n2 = Network("Smith", 150, [n1])
        >>> n2
        Network('Smith', $150, [Network('John', $100)])
        """
        return ('Network({}, ${}, {})'.format(repr(self.name),
                                                repr(self.asset),
                                                repr(self.child))
                if self.child
                else 'Network({}, ${})'.format(repr(self.name),
                                                repr(self.asset)))

    def __contains__(self, name):
        """
        Return whether Network self contains name.

        @param name: a certain name to search for
        @type name: str
        @rtype: bool

        >>> n1 = Network("John", 100)
        >>> n1.__contains__('John')
        True
        >>> n2 = Network("Smith", 150, [n1])
        >>> n2.__contains__('John')
        True
        >>> n2.__contains__('Charles')
        False
        """
        if len(self.child) == 0:
            return self.name == name
        else:
            return self.name == name or any([name in each for each in self.child])
    # TODO: Complete this part

    def bfs_contains(self, name):
        """
        Return whether Network self contains name with Breadth-first search,
        using Queue (FIFO)

        @param name: a certain name to search for
        @type name: str
        @rtype: bool

        >>> n1 = Network("John", 100)
        >>> n1.bfs_contains('John')
        True
        >>> n2 = Network("Smith", 150, [n1])
        >>> n2.bfs_contains('John')
        True
        >>> n2.bfs_contains('Charles')
        False
        """
        queue = deque()
        if self.name == name:
            return True
        queue.append(self)
        while len(queue) != 0:
            extract = queue.popleft()
            if extract.name == name:
                return True
            for child in extract.child:
                if child.name == name:
                    return True
                queue.append(child)
        # go through everything and still not found
        return False

    def dfs_contains(self, name):
        """
        Return whether Network self contains name with Depth-first search,
        using Stack (LIFO) which is just a list

        @param name: a certain name to search for
        @type name: str
        @rtype: bool

        >>> n1 = Network("John", 100)
        >>> n1.dfs_contains('John')
        True
        >>> n2 = Network("Smith", 150, [n1])
        >>> n2.dfs_contains('John')
        True
        >>> n2.dfs_contains('Charles')
        False
        >>> n3 = Network('Arthur', 20)
        >>> n4 = Network('Bob', 200, [n2, n3])
        >>> n4.dfs_contains('John')
        True
        >>> n4.dfs_contains('Charles')
        False
        """
        if self.name == name:
            return True
        for child in self.child:
            return child.dfs_contains(name)
        # goes through everything
        return False
        # feels very similar to the tree search function taught.

    def dfs_contains_iter(self, name):
        """
        Return whether Network self contains name with Depth-first search,
        using Stack (LIFO) which is just a list, with iterative methods.

        @param name: a certain name to search for
        @type name: str
        @rtype: bool

        >>> n1 = Network("John", 100)
        >>> n1.dfs_contains_iter('John')
        True
        >>> n2 = Network("Smith", 150, [n1])
        >>> n2.dfs_contains_iter('John')
        True
        >>> n2.dfs_contains_iter('Charles')
        False
        >>> n3 = Network('Arthur', 20)
        >>> n4 = Network('Bob', 200, [n2, n3])
        >>> n4.dfs_contains_iter('John')
        True
        >>> n4.dfs_contains_iter('Charles')
        False
        """
        stack = []
        stack.append(self)
        while len(stack) != 0:
            extract = stack.pop()
            if extract.name == name:
                return True
            for child in extract.child:
                stack.append(child)
        # goes through everything
        return False

    def load_log(self, log_file_name):
        """
        Load the network topology from the log log_file_name.

        @param self: Network self
        @type self: Network
        @param log_file_name: the name of the file for network topology
        @type log_file_name: str

        >>> network = Network()
        >>> network.load_log("topology0.txt")
        >>> network
        Network('Liam', $20, [Network('Emma', $32, [Network('Mason', $14)])])
        """
        open_file = open(log_file_name, 'r')
        for line in open_file:
            info = line.rstrip('\n').split('#')
            if len(info) == 2: # boss slot, no parent
                self.name = info[0]
                self.asset = int(info[1])
            else:
                # has parent
                # parent already in
                if self.__contains__(info[1]):
                    current = self
                    # search for parent
                    while current.name != info[1]:
                        # move down if that branch contains name
                        for each in current.child.copy():
                            if each.__contains__(info[1]):
                                current = each
                                # create child from parent
                    current.child.append(Network(name=info[0],
                                                 asset=int(info[2])))

        open_file.close()

    def sponsor(self, member_name):
        """
        Return the sponsor name of member with name member_name,
        and None when member_name is boss.

        Basically returning the parents

        @param self: Network self
        @type self: Network
        @param member_name: the name of the member known
        @type member_name: str
        @rtype: str or None

        >>> n1 = Network("John", 100)
        >>> print(n1.sponsor('John'))
        None
        >>> n2 = Network("Smith", 150, [n1])
        >>> print(n2.sponsor('John'))
        Smith
        """
        parent, current = None, self
        if self.name == member_name and parent is None:
            return None
        else:
            while current.name != member_name:
                for child in current.child.copy():
                    if child.__contains__(member_name):
                        parent = current
                        current = child
            return parent.name

    def mentor(self, member_name):
        """
        Return the mentor name of member with name member_name.

        TODO: Complete this part
        """

        #TODO: Complete this part


    def assets(self, member_name):
        """Return the assets of member with name member_name.

        TODO: Complete this part
        """

        #TODO: Complete this part


    def children(self, member_name):
        """Return the name of all children of member with name member_name.

        TODO: Complete this part
        """

        #TODO: Complete this part


    def best_arrest_assets(self, maximum_arrest):
        """Search for the amount of seized assets in the best arrest scenario
        that maximizes the seized assets. Consider all members as target zero.

        TODO: Complete this part
        """

        #TODO: Complete this part

    def best_arrest_order(self, maximum_arrest):
        """Search for list of member names in the best arrest scenario that
        maximizes the seized assets. Consider all members as target zero,
        and the order in the list represents the order that members are
        arrested.

        TODO: Complete this part
        """

        #TODO: Complete this part


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # A sample example of how to use a network object
    #network = Network()
    #network.load_log("topology1.txt")
    #member_name = "Sophia"
    #print(member_name + "'s sponsor is " + network.sponsor(member_name))
    #print(member_name + "'s mentor is " + network.mentor(member_name))
    #print(member_name + "'s asset is " + str(network.assets(member_name)))
    #print(member_name + "'s childrens are " + str(network.children(member_name)))
    #maximum_arrest = 4
    #print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
    #      + " arrests will seize " + str(network.best_arrest_assets(maximum_arrest)))
    #print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
    #      + " arrests is: " + str(network.best_arrest_order(maximum_arrest)))
