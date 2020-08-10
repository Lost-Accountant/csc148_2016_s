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
        if self.child:
            return 'Network({}, ${}, {})'.format(repr(self.name),
                                                  repr(self.asset),
                                                  repr(self.child))
        else:
            return 'Network({}, ${})'.format(repr(self.name),
                                             repr(self.asset))

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
            return self.name == name or \
                   any([each.__contains__(name) for each in self.child])

    def jump_to(self, name):
        """
        Jump to the node with given name

        @param name: name we want to jump to
        @type name: str
        @rtype: Network
        >>> n1 = Network("John", 100)
        >>> n2 = Network("Smith", 150, [n1])
        >>> current = n2.jump_to("John")
        >>> current is n1
        True
        """
        if self.__contains__(name):
            current = self
            while current.name != name:
                for child in current.child.copy():
                    if child.__contains__(name):
                        current = child
            return current

    def richest_child(self, member_name):
        """
        Return the name of the richest child under a member name, if no child,
        return None

        @param member_name: the member name of the parent
        @type member_name: str
        @rtype: str

        >>> n1 = Network()
        >>> n1.load_log("topology1.txt")
        >>> n1.richest_child("Jacob")
        'William'
        >>> n1.richest_child("Emma")
        'Mason'
        >>> print(n1.richest_child("Sophia"))
        None
        """
        child_list = self.children(member_name)
        record = 0
        holder = None
        for each in child_list:
            if self.assets(each) > record:
                record = self.assets(each)
                holder = each
        return holder

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
            if len(info) == 2:  # boss slot, no parent
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
        Return the mentor name of member with name member_name. Sponsor is the
        parent of the first child, or the previous member.

        @param member_name: the member name we are interested in
        @type member_name: str
        @param self: Network self
        @type self: Network
        @rtype: str

        >>> n1 = Network("John", 100)
        >>> n2 = Network("Smith", 150, [n1])
        >>> print(n2.mentor('John'))
        Smith
        >>> n3 = Network("Alex", 170)
        >>> n2 = Network("Smith", 150, [n1, n3])
        >>> print(n2.mentor("Alex"))
        John
        """
        # get parent if list[0], else get list[n-1]
        # locate member interested and its parent
        parent, current = None, self
        while current.name != member_name:
            # locate the target
            for child in current.child.copy():
                if child.__contains__(member_name):
                    parent = current
                    current = child
        # after locating the target
        # is the child at list[0]?

        if parent is not None:
            if parent.child[0] is current:
                return parent.name
            else:
                # previous member
                return parent.child[parent.child.index(current) - 1].name
        else:
            return None

    def assets(self, member_name):
        """
        Return the assets of member with name member_name.

        @param self: Network self
        @type self: Network
        @param member_name: the member name we are interested in
        @type member_name: str
        @rtype: int

        >>> n1 = Network("John", 100)
        >>> n3 = Network("Alex", 170)
        >>> n2 = Network("Smith", 150, [n1, n3])
        >>> n2.assets('John')
        100
        >>> n2.assets('Smith')
        150
        """
        # locate child
        current = self.jump_to(member_name)
        # after locating
        return current.asset

    def children(self, member_name):
        """
        Return the name of all children of member with name member_name.
        Assuming it is only for first/direct child, not including any children
        after first layer.

        @param self: Network self
        @type self: Network
        @param member_name: the member name we are interested in
        @type member_name: str
        @rtype: list[str]

        >>> n1 = Network("John", 100)
        >>> n3 = Network("Alex", 170)
        >>> n2 = Network("Smith", 150, [n1, n3])
        >>> n2.children("Smith")
        ['John', 'Alex']
        """
        # locate member
        current = self
        while current.name != member_name:
            for child in current.child.copy():
                if child.__contains__(member_name):
                    current = child
        # find the member, get its children names
        list_child = []
        for child in current.child:
            list_child.append(child.name)
        return list_child

    def best_arrest_assets(self, maximum_arrest):
        """
        Search for the amount of seized assets in the best arrest scenario
        that maximizes the seized assets. Consider all members as target zero.

        >>> n1 = Network()
        >>> n1.load_log("topology1.txt")
        >>> n1.best_arrest_assets(4)
        162
        >>> n1.best_arrest_assets(2)
        92
        >>> n1.best_arrest_assets(1)
        60
        >>> n1.best_arrest_assets(3)
        124
        """
        members = list_all(self)
        top = 0
        for each in members:
            path = best_path_order(self, each, maximum_arrest)
            seized = self.sum_assets(path)
            top = max(top, seized)
        return top

    def best_arrest_order(self, maximum_arrest):
        """
        Search for list of member names in the best arrest scenario that
        maximizes the seized assets. Consider all members as target zero,
        and the order in the list represents the order that members are
        arrested.

        >>> n1 = Network()
        >>> n1.load_log("topology1.txt")
        >>> best_four = n1.best_arrest_order(4)
        >>> best_four.sort()
        >>> best_four == ['Alexander', 'Jacob', 'James', 'William']
        True
        >>> best_two = n1.best_arrest_order(2)
        >>> best_two.sort()
        >>> best_two == ["Jacob", "William"]
        True
        >>> n1.best_arrest_order(1)
        ['Alexander']
        >>> best_three = n1.best_arrest_order(3)
        >>> best_three.sort()
        >>> best_three == ['Emma', 'Jacob', 'William']
        True
        """
        members = list_all(self)
        top = 0
        best_path = []

        for each in members:
            path = best_path_order(self, each, maximum_arrest)
            seized = self.sum_assets(path)
            if top < seized:
                top = seized
                best_path = path
        return best_path

    def sum_assets(self, name_list):
        """
        Return the sum of assets given a list of names in the Network.

        @param name_list: a list of memebr names
        @type name_list: list[str]
        @rtype: int

        >>> n1 = Network()
        >>> n1.load_log("topology1.txt")
        >>> n1.sum_assets(["Liam", "Alexander", "Olivia"])
        88
        """
        sum = 0
        for item in name_list:
            sum += self.assets(item)
        return sum

def list_all(network):
    """
    List all names in the network

    @param network: the network interested in
    @type network: Network
    @rtype: list[str]

    >>> n1 = Network("John", 100)
    >>> n3 = Network("Alex", 170)
    >>> n2 = Network("Smith", 150, [n1, n3])
    >>> list_all(n2)
    ['John', 'Alex', 'Smith']
    """
    if len(network.child) == 0:
        return [network.name]
    else:
        return gather_lists([list_all(x) for x in network.child]) \
               + [network.name]


def gather_lists(list_):
    """
    Return the concatenation of the sublists of list_.

    :param list_: list of sublists
    :type list_: list[list]
    :rtype: list

    >>> list_ = [[1, 2], [3, 4]]
    >>> gather_lists(list_)
    [1, 2, 3, 4]
    """
    # this is a case where list comprehension gets a bit unreadable
    new_list = []
    for sub in list_:
        for element in sub:
            new_list.append(element)
    return new_list

def best_path_order(network, member_name, steps):
    """
    Return the best path in the network from a given member_name and number of
    steps in the form of a list.

    @param self: Network self
    @type self: Network
    @param member_name: the member name we are interested in
    @type member_name: str
    @param steps: steps left to explore
    @type steps: int
    @rtype: list[str]

    >>> n1 = Network()
    >>> n1.load_log("topology1.txt")
    >>> best_path_order(n1, "Alexander", 3)
    ['Alexander', 'James', 'William']
    >>> best_path_order(n1, "Mason", 4)
    ['Mason', 'Emma', 'Liam', 'Jacob']
    """
    if member_name is None:
        return []

    path = []
    # base case
    # 1 steps left, return its name
    if steps == 1:
        path.append(member_name)
        return path

    # general case
    else:
        # current asset is zero so that future recursion doesn't come back
        current = network.jump_to(member_name)
        temp = current.asset
        current.asset = 0

        sponsor, mentor, child = network.sponsor(member_name), \
                                 network.mentor(member_name), \
                                 network.richest_child(member_name)
        # selection process
        sponsor_path = best_path_order(network, sponsor, steps - 1)
        mentor_path = best_path_order(network, mentor, steps - 1)
        child_path = best_path_order(network, child, steps - 1)

        pool = {repr(sponsor_path): network.sum_assets(sponsor_path),
                repr(mentor_path): network.sum_assets(mentor_path),
                repr(child_path): network.sum_assets(child_path)}
        ## filter out path with current member name
        for l in pool.keys():
            if member_name in l:
                pool[l] = 0
        ## select best path to return
        path = [member_name] + eval(max(pool, key=pool.get))

        # put the value back after selection process
        current.asset = temp

        return path

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # A sample example of how to use a network object
    network = Network()
    network.load_log("topology1.txt")
    member_name = "Sophia"
    print(member_name + "'s sponsor is " + network.sponsor(member_name))
    print(member_name + "'s mentor is " + network.mentor(member_name))
    print(member_name + "'s asset is " + str(network.assets(member_name)))
    print(member_name + "'s childrens are " + str(network.children(member_name)))
    maximum_arrest = 4
    print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
          + " arrests will seize " + str(network.best_arrest_assets(maximum_arrest)))
    print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
          + " arrests is: " + str(network.best_arrest_order(maximum_arrest)))
