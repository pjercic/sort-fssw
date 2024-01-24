import numpy as np
import scipy.stats as stats

def generate_normal_random_numbers(n = 10000, p = 0.5):

    # Generate random trial samples - Bernoulli trials
    # n number_of_samples

    validate_normal(n, p)
    
    #np.random.normal(p, size = n)
    normal_random_numbers = stats.norm.rvs(size = n)

    return normal_random_numbers

def sample_normal(arr, confidence_of_chance = 0.5):

    validate_sampling(confidence_of_chance)

    normal_sample = np.random.choice(arr, int(arr.size * confidence_of_chance), replace=False)

    return normal_sample

def estimate_normal(arr, confidence_of_chance = 0.5):
    
    uniform_sample = sample_normal(arr, confidence_of_chance)

    desc_stats = stats.describe(uniform_sample)

    # mean, var, skew, kurt
    return desc_stats[2], desc_stats[3], desc_stats[4], desc_stats[5]

def validate_normal(n, p):

    if p < 0 or p > 1:
        raise ValueError("Probability p must be between 0 and 1")

    if n < 0:
        raise ValueError("Number of trials n must be non-negative")

def validate_sampling(confidence_of_chance):

    if confidence_of_chance < 0 or confidence_of_chance > 1:
        raise ValueError("Probability confidence_of_chance must be between 0 and 1")
