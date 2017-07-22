"""
Programming task
================
******** NOTES BY BENJAMIN TANZ ********:
- Code was tested with Python 2.7.10 and 3.4.3 and all unit tests passed
- Considering various implementations, I opted for one that is functional in style
- Please also see comments in text for explanations
Implement the method iter_sample below to make the Unit test pass. iter_sample
is supposed to peek at the first n elements of an iterator, and determine the
minimum and maximum values (using their comparison operators) found in that
sample. To make it more interesting, the method is supposed to return an
iterator which will return the same exact elements that the original one would
have yielded, i.e. the first n elements can't be missing.
You may make use of Python's standard library. Python 3 is allowed, even though
it's not supported by codepad apparently.
Create your solution as a private fork, and send us the URL.
"""

from itertools import count, tee, islice
import unittest


def iter_sample(it, n):
    """
    Peek at the first n elements of an iterator, and determine the min and max
    values. Preserve all elements in the iterator!
    @param it: Iterator, potentially infinite
    @param n: Number of elements to peek off the iterator
    @return: Tuple of minimum, maximum (in sample), and an iterator that yields
    all elements that would have been yielded by the original iterator.
    """

    # create two independent iterators from the input iterator
    it_new, it = tee(it, 2)

    # retrieve first n items of iterator as a list
    arr = list(islice(it_new, n))

    # return min / max of sample and the original iterator
    return (min(arr), max(arr), it)


class StreamSampleTestCase(unittest.TestCase):

    def test_smoke(self):

        # sample only the first 10 elements of a range of length 100

        it = iter(range(100))
        min_val, max_val, new_it = iter_sample(it, 10)


        self.assertEqual(0, min_val)
        self.assertEqual(9, max_val)
        # all elements are still there:
        self.assertEqual(list(range(100)), list(new_it))

    def test_sample_all(self):

        # sample more elements than there are - no error raised
        # now we now the global maximum!

        it = iter(range(100))
        min_val, max_val, new_it = iter_sample(it, 1000)

        self.assertEqual(0, min_val)
        self.assertEqual(99, max_val)
        self.assertEqual(list(range(100)), list(new_it))

    def test_infinite_stream(self):

        # and guess what - it also works with infinite iterators

        it = count(0)
        min_val, max_val, _ = iter_sample(it, 10)

        self.assertEqual(0, min_val)
        self.assertEqual(9, max_val)

if __name__ == "__main__":
    unittest.main()