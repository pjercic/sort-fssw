import numpy as np
import scipy.stats as stats

def generate_chi2_random_numbers(n = 10000, degrees_of_freedom = 2):

    # Generate random trial samples - Bernoulli trials
    # n number_of_samples

    validate_chi2(n, degrees_of_freedom)
    
    #np.random.chisquare(degrees_of_freedom, size = 1000)
    chi2_random_numbers = stats.chi2.rvs(degrees_of_freedom, size=n)

    return chi2_random_numbers

def sample_chi2(arr, confidence_of_chance = 0.5):

    validate_sampling(confidence_of_chance)

    chi2_sample = np.random.choice(arr, int(arr.size * confidence_of_chance), replace=False)

    return chi2_sample

def estimate_chi2(arr, confidence_of_chance = 0.5):
    
    chi2_sample = sample_chi2(arr, confidence_of_chance)

    desc_stats = stats.describe(chi2_sample)

    # mean, var, skew, kurt
    return desc_stats[2], desc_stats[3], desc_stats[4], desc_stats[5]

def validate_chi2(n, degrees_of_freedom):

    if degrees_of_freedom >= 1:
        raise ValueError("degrees_of_freedom must be greater equal 1")

    if n < 0:
        raise ValueError("Number of trials n must be non-negative")

def validate_sampling(confidence_of_chance):

    if confidence_of_chance < 0 or confidence_of_chance > 1:
        raise ValueError("Probability confidence_of_chance must be between 0 and 1")
