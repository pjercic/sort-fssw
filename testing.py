import numpy as np
import unittest
import copy
import time

import scipy.stats as stats

from gen_utils import gen_binomial, gen_uniform
from sorting import binomial, uniform

class TestRandomNumberGeneration(unittest.TestCase):

    def test_binomial_random_numbers(self):
        n = 10000
        p = 0.5
        confidence_of_chance = 0.5

        binomial_random_numbers = gen_binomial.generate_binomial_random_numbers(n, p)

        # Check the size of the array
        self.assertEqual(len(binomial_random_numbers), n)

        # Sampling array
        binomial_sample = gen_binomial.sample_binomial(binomial_random_numbers, confidence_of_chance)

        # Check the size of the array
        self.assertEqual(len(binomial_sample), int(binomial_random_numbers.size * confidence_of_chance))

        # Estimation
        binomial_probability = gen_binomial.estimate_binomial(binomial_random_numbers, confidence_of_chance)

        # Check the size of the array
        self.assertLessEqual(p - 0.1, binomial_probability)
        self.assertGreaterEqual(p + 0.1, binomial_probability)

    def test_uniform_random_numbers(self):
        n = 10000
        confidence_of_chance = 0.5

        uniform_random_numbers = gen_uniform.generate_uniform_random_numbers(n)

        # Check the size of the array
        self.assertEqual(len(uniform_random_numbers), n)

        # Sampling array
        uniform_sample = gen_uniform.sample_uniform(uniform_random_numbers, confidence_of_chance)

        # Check the size of the array
        self.assertEqual(len(uniform_sample), int(uniform_random_numbers.size * confidence_of_chance))

        # Estimation
        
        mean, _, _, _ = stats.uniform.stats(moments='mvsk')
        est_mean, _, _, _ = gen_uniform.estimate_uniform(uniform_random_numbers, confidence_of_chance)

        # Check the size of the array
        self.assertLessEqual(mean - 0.1, est_mean)
        self.assertGreaterEqual(mean + 0.1, est_mean)

class TestSorting(unittest.TestCase):

    def test_binomial_sorting(self):
        
        n = 10000
        p = 0.5

        binomial_random_numbers = gen_binomial.generate_binomial_random_numbers(n, p)

        # Sort the array using counting sort
        # TODO: Validate if array is sorted
        sorted_array = binomial.sort_bernoulli(binomial_random_numbers)

        sorted_array = binomial.sort_binomial(binomial_random_numbers)

        # Generate random trial samples
        bernoulli_random_inserts = gen_binomial.generate_binomial_random_numbers(n, p)

        for new_trial in bernoulli_random_inserts:
            binomial_random_numbers =binomial.insert_binomial(new_trial, binomial_random_numbers)

        # Check the size of the array
        self.assertEqual(len(binomial_random_numbers), 2 * n)

    def test_uniform_sorting(self):
        
        n = 10000

        uniform_random_numbers = gen_uniform.generate_uniform_random_numbers(n)

        # Sort the array using counting sort
        # TODO: Validate if array is sorted
        sorted_array = uniform.sort_uniform(uniform_random_numbers)

        # Generate random trial samples
        uniform_random_inserts = gen_uniform.generate_uniform_random_numbers(n)

        for new_trial in uniform_random_inserts:
            uniform_random_numbers =uniform.insert_uniform(new_trial, uniform_random_numbers)

        # Check the size of the array
        self.assertEqual(len(uniform_random_numbers), 2 * n)

class TestSpeed(unittest.TestCase):

    def test_binomial_speed(self):
        
        n = 10000
        p = 0.5

        binomial_random_numbers = gen_binomial.generate_binomial_random_numbers(n, p)

        sort_rnd_python = copy.deepcopy(binomial_random_numbers)
        start = time.time()
        sort_rnd_python.sort()
        end = time.time()
        print('Time to python sort = ', (end-start)*1000, 'ms')

        sort_rnd_numpy = copy.deepcopy(binomial_random_numbers)
        start = time.time()
        sort_rnd_numpy = np.sort(sort_rnd_numpy)
        end = time.time()
        print('Time to numpy sort = ', (end-start)*1000, 'ms')

        sort_rnd_bernoulli = copy.deepcopy(binomial_random_numbers)
        start = time.time()
        sort_rnd_bernoulli = binomial.sort_bernoulli(sort_rnd_bernoulli)
        end = time.time()
        print('Time to bernoulli sort = ', (end-start)*1000, 'ms')

        sort_rnd_bernoulli = copy.deepcopy(binomial_random_numbers)
        start = time.time()
        sort_rnd_binomial = binomial.sort_binomial(sort_rnd_bernoulli)
        end = time.time()
        print('Time to binomail sort = ', (end-start)*1000, 'ms')

    def test_uniform_speed(self):
        
        n = 10000

        uniform_random_numbers = gen_uniform.generate_uniform_random_numbers(n)

        sort_rnd_python = copy.deepcopy(uniform_random_numbers)
        start = time.time()
        sort_rnd_python.sort()
        end = time.time()
        print('Time to python sort = ', (end-start)*1000, 'ms')

        sort_rnd_numpy = copy.deepcopy(uniform_random_numbers)
        start = time.time()
        sort_rnd_numpy = np.sort(sort_rnd_numpy)
        end = time.time()
        print('Time to numpy sort = ', (end-start)*1000, 'ms')

        sort_rnd_bernoulli = copy.deepcopy(uniform_random_numbers)
        start = time.time()
        sort_rnd_bernoulli = uniform.sort_uniform(sort_rnd_bernoulli)
        end = time.time()
        print('Time to uniform sort = ', (end-start)*1000, 'ms')

if __name__ == "__main__":
    unittest.main()
