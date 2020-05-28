import unittest
from week4_container_in_class_example import Stack


class TestStackEmptyness(unittest.TestCase):
    """Test behaviour of is_empty() method"""

    def setUp(self):
        """
        Set up an empty Stack before running each test case
        :return:
        :rtype: None
        """
        self.stack = Stack()

    def tearDown(self):
        """
        Clear up after running each test case
        :return:
        :rtype: None
        """
        self.stack = None

    def test_isEmpty(self):
        """
        verify if is_empty() returns true on an empty stack
        :return:
        :rtype: bool
        """
        assert self.stack.is_empty(), 'Oops, is_empty() returned False on an ' \
                                      'empty stack'

    def test_not_is_Empty(self):
        """
        verify if is_empty() returns true on a non-empty stack
        :return:
        :rtype: bool
        """
        self.stack.add("1")
        assert not self.stack.is_empty(), 'Oops, is_empty() returned True on a ' \
                                          'non-empty stack'

class TestStackComprehensiveness(unittest.TestCase):
    """ Test behaviour of a Stack"""
    def setUp(self):
        """
        Set up an empty Stack before running each test case
        :return:
        :rtype: None
        """
        self.stack = Stack()

    def tearDown(self):
        """
        Clear up after running each test case
        :return:
        :rtype: None
        """
        self.stack = None

    def test_add_remove(self):
        """Test if add() and remove() work properly for one element"""
        self.stack.add("12")
        self.assertEqual(self.stack.remove(), "12", "Oops, add() and "
                                                    "remove() did not "
                                                    "work properly")

    def test_more_add_remove(self):
        """Test if add() and remove() work properly for more elements"""

        for item in range(20):
            self.stack.add(item)
            assert not self.stack.is_empty(), "Oops, is_empty() returned " \
                                              "True where it should not"

        expect = 19
        while not self.stack.is_empty():
            removed_item = self.stack.remove()
            self.assertEqual(removed_item, expect, "Oops, remove() did not "
                                                   "remove the expected value")
            expect -=1

        assert self.stack.is_empty(), "Oops, stack is not " \
                                      "empty where is should be"

        assert expect == -1, "Oops, something is wrong"

if __name__ == "__main__":
    unittest.main(exit=False)

# suite = unittest.TestLoader().loadTestsFromTestCase(TestStackComprehensiveness)
# unittest.TextTestRunner(verbosity=2).run(suite)
#
# suite = unittest.TestLoader().loadTestsFromTestCase(TestStackEmptyness)
# unittest.TextTestRunner(verbosity=2).run(suite)
