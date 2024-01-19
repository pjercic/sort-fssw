import numpy as np

def sort_bernoulli(arr):
    
    # Count sort
    count = sort_rnd_bernoulli.size // 2
    arr[:count] = 0
    arr[count:] = 1
    
    return arr

def sort_binomial(arr):
    
    # Count sort
    count = np.count_nonzero(arr == 0)
    arr[:count] = 0
    arr[count:] = 1
    
    return arr

def insert_binomial (new_trial, trials_list):

    if new_trial == 0:
        
        # + operator
        #trials_list = [new_trial] + trials_list
    
        # extend
        #trials_list.extend([new_trial])
        
        #numpy
        trials_list = np.insert(trials_list, 0, new_trial)
    else:
        #trials_list.append(new_trial)
        
        #numpy
        trials_list = np.append(trials_list, new_trial)
    
    return trials_list
