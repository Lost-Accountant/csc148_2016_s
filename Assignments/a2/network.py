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
    # TODO: Complete this part

    def load_log(self, log_file_name):
        """Load the network topology from the log log_file_name.

        TODO: Complete this part
        """

        #TODO: Complete this part


    def sponsor(self, member_name):
        """Return the sponsor name of member with name member_name.

        TODO: Complete this part
        """

        #TODO: Complete this part


    def mentor(self, member_name):
        """Return the mentor name of member with name member_name.

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
