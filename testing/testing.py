import numpy as np
import unittest

from .binom_utils import generate_binomial_random_numbers
from .sorting import counting_sort

class TestBinomialRandomNumberGeneration(unittest.TestCase):

    def test_binomial_random_numbers(self):
        n = 10
        p = 0.5
        binomial_random_numbers = generate_binomial_random_numbers(n, p)

        # Check the size of the array
        self.assertEqual(len(binomial_random_numbers), n)

        # Check if the probability is between 0 and 1
        self.assertGreaterEqual(p, 0)
        self.assertLessEqual(p, 1)

        # Check if the number of trials is non-negative
        self.assertGreaterEqual(n, 0)

class TestSorting(unittest.TestCase):

    def test_sorting(self):
        # Generate random boolean array
        array = np.random.randint(0, 2, 10000)

        # Sort the array using counting sort
        sorted_array = counting_sort(array)

        # Check if the array is sorted
        for i in range(1, len(array)):
            if sorted_array[i - 1] > sorted_array[i]:
                raise ValueError("Array is not sorted")

if __name__ == "__main__":
    unittest.main()
