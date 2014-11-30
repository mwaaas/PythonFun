__author__ = 'mwas'


def tree_n_plus_one_problem(n, sequence=[]):
    """
    Start with an integer n. If n is even, divide by 2.
    If n is odd, multiply by 3 and add 1.
    Repeat this process with the new value of n,
    terminating when n = 1.
    For example, the following sequence of numbers will be generated for n = 22:
        22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
    It is conjectured (but not yet proven) that this algorithm will terminate at
     n = 1 for every integer n.
     Still, the conjecture holds for all integers up to at least 1, 000, 000.


     The challenge has been derived from the following link
            http://www.programming-challenges.com/pg.php?page=downloadproblem&probid=110101&format=html


    :param n: int  ( should be greater than 0 and less that 1,000,000
    :param sequence: list of numbers produced by the sequence
    :return: list
    :raises exception is n is not int or its less than 0 and greater than 1,000,000

    """

    if n < 0 or n > 1000000:
        raise TypeError
    if n == 1:
        return n

    # even numbers are divided into two
    if n % 2 == 0:
        n /= 2

    else:
        n = (3 * n) + 1

    sequence.append(n)

    sequence.append(tree_n_plus_one_problem(n, sequence))
    return sequence

print "start excuting"
