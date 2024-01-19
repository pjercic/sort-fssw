import numpy as np
import scipy.stats as stats

def generate_binomial_random_numbers(n = 10000, p = 0.5):

    # Generate random trial samples - Bernoulli trials
    # n number_of_samples
    # p chance_of_event

    validate_binomial(n, p)
    
    #binomial_random_numbers = stats.bernoulli.rvs(p = p, size = n)
    binomial_random_numbers = np.random.binomial(n, p, 10000)

    return binomial_random_numbers

def count_succesful_events(n = 10000, p = 0.5):

    validate_binomial(n, p)

    succesful_count = stats.binom.rvs(n = n, p = p)

    return succesful_count

def sampling_binomial(arr, confidence_of_chance = 0.5):

    events_counter = 0
    for j in range(1, int(arr.size * confidence_of_chance)):
        if arr[j] == 1:
            events_counter += 1
            
    #? estimated_chance_of_event = events_counter / number_of_samples * confidence_of_chance
    estimated_chance_of_event = events_counter / (arr.size * confidence_of_chance)

    return estimated_chance_of_event

def validate_binomial(n, p):

    if p < 0 or p > 1:
        raise ValueError("Probability p must be between 0 and 1")

    if n < 0:
        raise ValueError("Number of trials n must be non-negative")
