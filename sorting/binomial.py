import numpy as np

def sort_bernoulli(arr):
    
    # Count sort
    count = arr.size // 2
    arr[:count] = 0
    arr[count:] = 1
    
    return arr

def sort_binomial(arr):
    
    # Count sort
    count = np.count_nonzero(arr == 0)
    arr[:count] = 0
    arr[count:] = 1
    
    return arr

def insert_binomial (new_trial, arr):

    if new_trial == 0:
        
        # + operator
        #trials_list = [new_trial] + trials_list
    
        # extend
        #trials_list.extend([new_trial])
        
        #numpy
        arr = np.insert(arr, 0, new_trial)
    else:
        #trials_list.append(new_trial)
        
        #numpy
        arr = np.append(arr, new_trial)
    
    return arr
