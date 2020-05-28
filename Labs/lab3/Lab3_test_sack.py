"""
Test module Sack.

"""
import unittest
from sack import Sack

class EmptyTestCase(unittest.TestCase):
    """
    Test behavior of an empty Sack.
    """

    def setUp(self):
        """
        Set up an empty queue
        @rtype: None
        """
        self.sack = Sack()

    def TearDown(self):
        """
        Clean up.
        @rtype: None
        """
        self.sack = None

    def testIsEmpty(self):
        """
        Test is_empty() on empty Queue.
        """
        self.assertTrue(self.sack.is_empty(),
                        "Return non-empty on empty Sack")

class SingletonTestCase(unittest.TestCase):
    """
    Check whether adding a single item makes it appear at the front.
    """
    def setUp(self) -> None:
        """
        Set up a Queue with a single element
        """
        self.sack = Sack()
        self.sack.add('1')

    def TearDown(self):
        """
        Clean up

        """
        self.sack = None

    def testIsEmpty(self):
        """
        Test is_empty() on non-empty Sack.
        """
        self.assertFalse(self.sack.is_empty(),
                         "Return empty on non-empty Sack")

    def testRemove(self):
        """
        Test remove() on non-empty case and is_empty() on empty case
        """
        removed = self.sack.remove()
        self.assertEqual(removed, '1',
                         "Item removed is not the same as stored")
        self.assertTrue(self.sack.is_empty(),
                        "Return non-empty on empty Sack")

class TypicalTestCase(unittest.TestCase):
    """
    A comprehensive tester of typical behavior of Queue.
    """
    def setUp(self) -> None:
        """
        Set up an empty sack.
        """
        self.sack = Sack()

    def TearDown(self):
        """
        Clean up.
        @rtype: None
        """
        self.sack = None

    def testALL(self):
        """
        Check adding and removing several items.
        """
        l = []
        for item in range(20):
            self.sack.add(item)
            self.assertFalse(self.sack.is_empty(),
                             "Return empty on non-empty sack after adding" + str(item))
            l.append(item)

        while not self.sack.is_empty():
            removed = self.sack.remove()
            self.assertTrue(removed in l,
                            "Removed item is not input for " + str(removed))
            l.remove(removed)

        assert self.sack.is_empty(), "return non-empty on empty list"

        self.assertEqual(l, [], "something left un-removed")


if __name__ == "__main__":
    unittest.main(exit=False)
