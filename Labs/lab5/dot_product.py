# don't use list comprehension or zip

def dot_prod(u,v):
    """
    Return the dot product of u and v

    @param u: vector of floats
    @type u: list[float]
    @param v: vector of floats
    @type v: list[float]
    @rtype: float

    >>> dot_prod([1.0, 2.0], [3.0,4.0])
    11.0
    """
    each_product = []
    for i in range(len(u)):
        each_product.append(u[i] * v[i])
    return sum(each_product)

def matrix_vector_prod(m,u):
    """
    Return the matrix-vector product of m x u.

    @param m: matrix
    @type m: list[list[float]]
    @param u: vector
    @type u: list[float]
    @return: vector
    @rtype: list[float]

    >>> matrix_vector_prod([[1.0, 2.0], [3.0, 4.0]], [5.0, 6.0])
    [17.0, 39.0]
    """
    each_product = []
    for v in m:
        each_product.append(dot_prod(v, u))
    return each_product

def pythagorean_triples(n):
    """
    Return list of pythagorean triples as non-descending tuples of ints from 1 to n.

    Assume n is positive.

    @param n: upper bound of pythagorean triples
    @type n: int
    @rtype: list[tuple]
    >>> pythagorean_triples(5)
    [(3, 4, 5)]
    >>> pythagorean_triples(13)
    [(3, 4, 5), (5, 12, 13), (6, 8, 10)]
    """
    triples = []
    for i in range(1,n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if i**2 + j**2 == k**2 and i <= j <= k:
                    triples.append((i,j,k))
    return triples

if __name__ == '__main__':
    import doctest
    doctest.testmod()

