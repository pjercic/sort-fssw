import numpy as np
import scipy.stats as stats

def generate_binomial_random_numbers(n = 10000, p = 0.5):

    # Generate random trial samples - Bernoulli trials
    # n number_of_samples
    # p chance_of_event

    validate_binomial(n, p)
    
    binomial_random_numbers = stats.bernoulli.rvs(p = p, size = n)

    return binomial_random_numbers

def sample_binomial(arr, confidence_of_chance = 0.5):

    validate_sampling(confidence_of_chance)

    binomial_sample = np.random.choice(arr, int(arr.size * confidence_of_chance), replace=False)

    return binomial_sample

def estimate_binomial(arr, confidence_of_chance = 0.5):
    
    events_count = sum(sample_binomial(arr, confidence_of_chance))

    estimated_chance_of_event = events_count / (arr.size * confidence_of_chance)

    return estimated_chance_of_event

def validate_binomial(n, p):

    if p < 0 or p > 1:
        raise ValueError("Probability p must be between 0 and 1")

    if n < 0:
        raise ValueError("Number of trials n must be non-negative")

def validate_sampling(confidence_of_chance):

    if confidence_of_chance < 0 or confidence_of_chance > 1:
        raise ValueError("Probability confidence_of_chance must be between 0 and 1")
