# https://www.johndcook.com/blog/2022/03/09/normal-order-statistics/
# https://en.wikipedia.org/wiki/Order_statistic
import numpy as np

def sort_normal(arr):
    
    sorted_arr = np.empty_like(arr)
    
    # Issue with searchsorted, outputs right index out of bounds
    #target_indices = np.searchsorted(sort_rnd_uniform, sort_rnd_uniform)  # Use binary search for efficient lookup
    #target_indices[target_indices >= sort_rnd_uniform.size] = sort_rnd_uniform.size - 1
    target_indices = (arr * arr.size).astype(int, copy=False)

    #sorted_arr = [arr[i] for i in target_indices]  # Replace for loop with list comprehension
    sorted_arr = np.take(arr, target_indices)  # Use np.take to directly assign values
    #sorted_arr = map(lambda i: arr[i], target_indices)  # Replace for loop with map()
    return sorted_arr  

def insert_normal(new_trial, arr):
    # TODO: insert float numbers
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
