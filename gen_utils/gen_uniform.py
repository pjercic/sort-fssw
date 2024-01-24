import numpy as np
import scipy.stats as stats

def generate_uniform_random_numbers(n = 10000):

    # Generate random trial samples - Bernoulli trials
    # n number_of_samples

    validate_uniform(n)
    
    #np.random.uniform(size = n)
    uniform_random_numbers = stats.uniform.rvs(size = n)

    return uniform_random_numbers

def sample_uniform(arr, confidence_of_chance = 0.5):

    validate_sampling(confidence_of_chance)

    uniform_sample = np.random.choice(arr, int(arr.size * confidence_of_chance), replace=False)

    return uniform_sample

def estimate_uniform(arr, confidence_of_chance = 0.5):
    
    uniform_sample = sample_uniform(arr, confidence_of_chance)

    desc_stats = stats.describe(uniform_sample)

    # mean, var, skew, kurt
    return desc_stats[2], desc_stats[3], desc_stats[4], desc_stats[5]

def validate_uniform(n):

    if n < 0:
        raise ValueError("Number of trials n must be non-negative")

def validate_sampling(confidence_of_chance):

    if confidence_of_chance < 0 or confidence_of_chance > 1:
        raise ValueError("Probability confidence_of_chance must be between 0 and 1")
