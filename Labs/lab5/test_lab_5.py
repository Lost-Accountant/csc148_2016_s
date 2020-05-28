import unittest
#from dot_product import *
from comprehension import  *
from random import randint

class TestDotProduct(unittest.TestCase):
    def test_size_1(self):
        u = [3.0]
        v = [2.0]
        z = 6.0
        assert dot_prod(u,v) == z

    def test_multiple_size(self):
        u = [1.0, 2.0, 3.0]
        v = [3.0,2.0,1.0]
        z = 10.0
        assert dot_prod(u,v) == z

class TestMatrixVector(unittest.TestCase):
    def test_matrix_size_1(self):
        m = [[1.0, 2.0]]
        v = [5.0,6.0]
        assert matrix_vector_prod(m,v) == [17.0]

    def test_matrix_larger_size(self):
        m = [[1.0, 2.0], [3.0, 4.0]]
        v = [5.0,6.0]
        assert matrix_vector_prod(m,v) == [17.0,39.0]

class TestPythagoreanTriples(unittest.TestCase):
    def test_random_case(self):
        l = pythagorean_triples(randint(0,100))
        for (i,j,k) in l:
            assert (i**2 + j**2) == k**2

if __name__ == "__main__":
    unittest.main()

