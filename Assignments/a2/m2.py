import unittest


class A2Mark_1(unittest.TestCase):

    def setUp(self):
        from network import Network
        self.network = Network()

    def test_boss(self):
        """ check sponsor and mentor for super boss """
        self.network.load_log("topology_test_1.txt")
        member_name = "Alexander"
        target_name = "None"
        assert (str(self.network.sponsor(member_name)) == target_name), "super boss's sponsor should be none"
        assert (str(self.network.mentor(member_name)) == target_name), "super boss's mentor should be none"

    def test_asset(self):
        """ check assert """
        self.network.load_log("topology_test_1.txt")
        member_name = "Alexander"
        target_num = 20
        assert (self.network.assets(member_name) == target_num), "asset read incorrect: %r vs desired: %r" \
                                                                   % (self.network.assets(member_name), target_num)

    def test_seize1(self):
        """ check best seize, case 1"""
        self.network.load_log("topology_test_1.txt")
        maximum_arrest = 1
        target_num = 20
        seize1 = self.network.best_arrest_assets(maximum_arrest)
        assert (seize1 == target_num), "amount of seized money incorrect: %r vs desired: %r" % (seize1, target_num)

    def test_order1(self):
        """ check best order, case 1"""
        self.network.load_log("topology_test_1.txt")
        maximum_arrest = 1
        target_order = ["Alexander"]
        order1 = self.network.best_arrest_order(maximum_arrest)
        assert (set(order1) == set(target_order)), "order of arrest incorrect: %r vs desired: %r" % (order1, target_order)

class A2Mark_2(unittest.TestCase):

    def setUp(self):
        from network import Network
        self.network = Network()

    def test_boss(self):
        """ check sponsor and mentor for super boss """
        self.network.load_log("topology_test_2.txt")
        member_name = "Alexander"
        target_name = "None"
        assert (str(self.network.sponsor(member_name)) == target_name), "super boss's sponsor should be none"
        assert (str(self.network.mentor(member_name)) == target_name), "super boss's mentor should be none"

    def test_sponsor1(self):
        """ check sponsor """
        self.network.load_log("topology_test_2.txt")
        member_name = "Emma"
        target_name = "Alexander"
        assert (self.network.sponsor(member_name) == target_name), "sponsor read incorrect: %r vs desired: %r"\
                                                                    % (self.network.sponsor(member_name), target_name)

    def test_mentor1(self):
        """ check mentor same as sponsor """
        self.network.load_log("topology_test_2.txt")
        member_name = "Emma"
        target_name = "Alexander"
        assert (self.network.mentor(member_name) == target_name), "mentor(same as sponsor) read incorrect: %r vs desired: %r" \
                                                                  % (self.network.mentor(member_name), target_name)

    def test_sponsor2(self):
        """ check sponsor """
        self.network.load_log("topology_test_2.txt")
        member_name = "James"
        target_name = "Alexander"
        assert (self.network.sponsor(member_name) == target_name), "sponsor read incorrect: %r vs desired: %r" \
                                                                   % (self.network.sponsor(member_name), target_name)
    def test_mentor2(self):
        """ check mentor diff from sponsor """
        self.network.load_log("topology_test_2.txt")
        member_name = "James"
        target_name = "Emma"
        assert (self.network.mentor(member_name) == target_name), "mentor(diff from sponsor) read incorrect: %r vs desired: %r" \
                                                                  % (self.network.mentor(member_name), target_name)

    def test_asset(self):
        """ check assert """
        self.network.load_log("topology_test_2.txt")
        member_name = "James"
        target_num = 50
        assert (self.network.assets(member_name) == target_num), "asset read incorrect: %r vs desired: %r" \
                                                                   % (self.network.assets(member_name), target_num)

    def test_children1(self):
        """ check children for member with multiple children """
        self.network.load_log("topology_test_2.txt")
        member_name = "Alexander"
        target_names = ['Emma', 'James']
        children1 = self.network.children(member_name)
        assert (children1 == target_names), "children case 1 read incorrect: %r vs desired: %r" % (children1, target_names)

    def test_seize1(self):
        """ check best seize, case 1"""
        self.network.load_log("topology_test_2.txt")
        maximum_arrest = 1
        target_num = 50
        seize1 = self.network.best_arrest_assets(maximum_arrest)
        assert (seize1 == target_num), "amount of seized money incorrect: %r vs desired: %r" % (seize1, target_num)

    def test_order1(self):
        """ check best order, case 1"""
        self.network.load_log("topology_test_2.txt")
        maximum_arrest = 1
        target_order = ["James"]
        order1 = self.network.best_arrest_order(maximum_arrest)
        assert (order1 == target_order), "order of arrest incorrect: %r vs desired: %r" % (order1, target_order)

    def test_seize2(self):
        """ check best seize, case 2"""
        self.network.load_log("topology_test_2.txt")
        maximum_arrest = 2
        target_num = 82

        seize1 = self.network.best_arrest_assets(maximum_arrest)
        assert (seize1 == target_num), "amount of seized money incorrect: %r vs desired: %r" % (seize1, target_num)

    def test_order2(self):
        """ check best order, case 2"""
        self.network.load_log("topology_test_2.txt")
        maximum_arrest = 2
        target_order = ['James', 'Emma']
        order1 = self.network.best_arrest_order(maximum_arrest)
        assert (set(order1) == set(target_order)), "order of arrest incorrect: %r vs desired: %r" % (order1, target_order)


class A2Mark_3(unittest.TestCase):

    def setUp(self):
        from network import Network
        self.network = Network()

    # def test_boss(self):
    #     """ check sponsor and mentor for super boss """
    #     self.network.load_log("topology_test_3.txt")
    #     member_name = "Alexander"
    #     target_name = "None"
    #     assert (self.network.sponsor(member_name) == target_name), "super boss's sponsor should be none"
    #     assert (self.network.mentor(member_name) == target_name), "super boss's mentor should be none"

    def test_sponsor1(self):
        """ check sponsor """
        self.network.load_log("topology_test_3.txt")
        member_name = "Sophia"
        target_name = "Emma"
        assert (self.network.sponsor(member_name) == target_name), "sponsor read incorrect: %r vs desired: %r"\
                                                                    % (self.network.sponsor(member_name), target_name)

    def test_mentor1(self):
        """ check mentor same as sponsor """
        self.network.load_log("topology_test_3.txt")
        member_name = "Sophia"
        target_name = "Emma"
        assert (self.network.mentor(member_name) == target_name), "mentor(same as sponsor) read incorrect: %r vs desired: %r" \
                                                                  % (self.network.mentor(member_name), target_name)

    # def test_asset(self):
    #     """ check assert """
    #     self.network.load_log("topology_test_3.txt")
    #     member_name = "Sophia"
    #     target_num = 14
    #     assert (self.network.assets(member_name) == target_num), "asset read incorrect: %r vs desired: %r" \
    #                                                                % (self.network.assets(member_name), target_num)

    def test_children1(self):
        """ check children for member with one child """
        self.network.load_log("topology_test_3.txt")
        member_name = "Emma"
        target_names = ['Sophia']
        children1 = self.network.children(member_name)
        assert (children1 == target_names), "children case 1 read incorrect: %r vs desired: %r" % (children1, target_names)

    def test_seize1(self):
        """ check best seize, case 1"""
        self.network.load_log("topology_test_3.txt")
        maximum_arrest = 1
        target_num = 32
        seize1 = self.network.best_arrest_assets(maximum_arrest)
        assert (seize1 == target_num), "amount of seized money incorrect: %r vs desired: %r" % (seize1, target_num)

    def test_order1(self):
        """ check best order, case 1"""
        self.network.load_log("topology_test_3.txt")
        maximum_arrest = 1
        target_order = ["Emma"]
        order1 = self.network.best_arrest_order(maximum_arrest)
        assert (set(order1) == set(target_order)), "order of arrest incorrect: %r vs desired: %r" % (order1, target_order)

    def test_seize2(self):
        """ check best seize, case 2"""
        self.network.load_log("topology_test_3.txt")
        maximum_arrest = 2
        target_num = 52

        seize1 = self.network.best_arrest_assets(maximum_arrest)
        assert (seize1 == target_num), "amount of seized money incorrect: %r vs desired: %r" % (seize1, target_num)

    def test_order2(self):
        """ check best order, case 2"""
        self.network.load_log("topology_test_3.txt")
        maximum_arrest = 2
        target_order = ['Alexander', 'Emma']
        order2 = self.network.best_arrest_order(maximum_arrest)
        assert (set(order2) == set(target_order)), "order of arrest incorrect: %r vs desired: %r" % (order2, target_order)


class A2Mark_4(unittest.TestCase):

    def setUp(self):
        from network import Network
        self.network = Network()

    # def test_boss(self):
    #     """ check sponsor and mentor for super boss """
    #     self.network.load_log("topology_test_4.txt")
    #     member_name = "Alexander"
    #     target_name = "None"
    #     assert (self.network.sponsor(member_name) == target_name), "super boss's sponsor should be none"
    #     assert (self.network.mentor(member_name) == target_name), "super boss's mentor should be none"

    def test_sponsor1(self):
        """ check sponsor """
        self.network.load_log("topology_test_4.txt")
        member_name = "Sophia"
        target_name = "Emma"
        assert (self.network.sponsor(member_name) == target_name), "sponsor read incorrect: %r vs desired: %r"\
                                                                    % (self.network.sponsor(member_name), target_name)

    def test_mentor1(self):
        """ check mentor same as sponsor """
        self.network.load_log("topology_test_4.txt")
        member_name = "Sophia"
        target_name = "Emma"
        assert (self.network.mentor(member_name) == target_name), "mentor(same as sponsor) read incorrect: %r vs desired: %r" \
                                                                  % (self.network.mentor(member_name), target_name)

    def test_sponsor2(self):
        """ check sponsor """
        self.network.load_log("topology_test_4.txt")
        member_name = "Mason"
        target_name = "Emma"
        assert (self.network.sponsor(member_name) == target_name), "sponsor read incorrect: %r vs desired: %r" \
                                                                   % (self.network.sponsor(member_name), target_name)
    def test_mentor2(self):
        """ check mentor diff from sponsor """
        self.network.load_log("topology_test_4.txt")
        member_name = "Mason"
        target_name = "Sophia"
        assert (self.network.mentor(member_name) == target_name), "mentor(diff from sponsor) read incorrect: %r vs desired: %r" \
                                                                  % (self.network.mentor(member_name), target_name)

    # def test_asset(self):
    #     """ check assert """
    #     self.network.load_log("topology_test_4.txt")
    #     member_name = "James"
    #     target_num = 50
    #     assert (self.network.assets(member_name) == target_num), "asset read incorrect: %r vs desired: %r" \
    #                                                                % (self.network.assets(member_name), target_num)

    def test_children1(self):
        """ check children for member with multiple children """
        self.network.load_log("topology_test_4.txt")
        member_name = "James"
        target_names = ['William', 'Liam', 'Olivia']
        children1 = self.network.children(member_name)
        assert (children1 == target_names), "children case 1 read incorrect: %r vs desired: %r" % (children1, target_names)

    def test_children2(self):
        """ check children for member without children """
        self.network.load_log("topology_test_4.txt")
        member_name = "Mason"
        target_names = []
        children1 = self.network.children(member_name)
        assert (children1 == target_names), "children case 2 read incorrect: %r vs desired: %r" % (children1, target_names)

    def test_seize1(self):
        """ check best seize, case 1"""
        self.network.load_log("topology_test_4.txt")
        maximum_arrest = 1
        target_num = 60
        seize1 = self.network.best_arrest_assets(maximum_arrest)
        assert (seize1 == target_num), "amount of seized money incorrect: %r vs desired: %r" % (seize1, target_num)

    def test_order1(self):
        """ check best order, case 1"""
        self.network.load_log("topology_test_4.txt")
        maximum_arrest = 1
        target_order = ["Jacob"]
        order1 = self.network.best_arrest_order(maximum_arrest)
        assert (set(order1) == set(target_order)), "order of arrest incorrect: %r vs desired: %r" % (order1, target_order)

    def test_seize2(self):
        """ check best seize, case 2"""
        self.network.load_log("topology_test_4.txt")
        maximum_arrest = 4
        target_num = 144

        seize1 = self.network.best_arrest_assets(maximum_arrest)
        assert (seize1 == target_num), "amount of seized money incorrect: %r vs desired: %r" % (seize1, target_num)

    def test_order2(self):
        """ check best order, case 2"""
        self.network.load_log("topology_test_4.txt")
        maximum_arrest = 4
        target_order = ['Emma', 'Alexander', 'James', 'William']
        order2 = self.network.best_arrest_order(maximum_arrest)
        assert (set(order2) == set(target_order)), "order of arrest incorrect: %r vs desired: %r" % (order1, target_order)

if __name__ == '__main__':
    unittest.main()
