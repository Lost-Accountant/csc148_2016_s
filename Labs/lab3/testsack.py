import unittest
from sack import Sack


class TestSackEmpty(unittest.TestCase):
    """Test behaviour of is_empty() method"""

    def setUp(self):
        """
        Set up an empty sack before running each test case
        :return:
        :rtype: None
        """
        self.sack = Sack()

    def tearDown(self):
        """
        Clear up after running each test case
        :return:
        :rtype: None
        """
        self.sack = None

    def test_isEmpty(self):
        """
        verify if is_empty() returns True on an empty sack
        :return:
        :rtype: bool
        """
        assert self.sack.is_empty(), 'is_empty() returned False on an ' \
                                      'empty sack'

    def test_not_is_Empty(self):
        """
        verify if is_empty() returns true on a non-empty sack
        :return:
        :rtype: bool
        """
        self.sack.add("1")
        assert not self.sack.is_empty(), 'is_empty() returned True on a ' \
                                          'non-empty sack'

class TestSackComprehensiveness(unittest.TestCase):
    """ Test behaviour of a sack"""
    def setUp(self):
        """
        Set up an empty sack before running each test case
        :return:
        :rtype: None
        """
        self.sack = Sack()

    def tearDown(self):
        """
        Clear up after running each test case
        :return:
        :rtype: None
        """
        self.sack = None

    def test_add_remove(self):
        """Test if add() and remove() work properly for one element"""
        self.sack.add("12")
        removed= self.sack.remove()
        self.assertEqual(removed , "12", "Oops, remove() removed "
                         + removed + " where '12' was expected")

    def test_more_add_remove(self):
        """Test if add() and remove() work properly for more elements"""

        for item in range(20):
            self.sack.add(item)
            assert not self.sack.is_empty(), "Oops, is_empty() returned " \
                                              "True where it should not"


        removed =[False] * 20
        counter = 19
        while not self.sack.is_empty():
            removed[self.sack.remove()] = True
            counter -=1

        assert self.sack.is_empty(), "Oops, sack is not " \
                                      "empty where is should be"

        assert counter == -1, "Oops, number of removed items is not 20"
        assert removed == [True] * 20, "Oops, some items have not removed " \
                                       "from the sack"

if __name__ == "__main__":
    unittest.main(exit=False)

# suite = unittest.TestLoader().loadTestsFromTestCase(TestsackComprehensiveness)
# unittest.TextTestRunner(verbosity=2).run(suite)
#
# suite = unittest.TestLoader().loadTestsFromTestCase(TestsackEmptyness)
# unittest.TextTestRunner(verbosity=2).run(suite)

