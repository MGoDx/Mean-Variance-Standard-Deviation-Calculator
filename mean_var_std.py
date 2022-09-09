import numpy as np

def calculate(list):

    # Check if list has 9 elements
    if len(list) != 9 :
        raise ValueError("List must contain nine numbers.") 

    # Transform the list into numpy matrix
    ls = np.array([ 
        [list[0],list[1],list[2]],
        [list[3],list[4],list[5]],
        [list[6],list[7],list[8]]
    ])

    # Do the calculations and return the result as dict
    calculations = {
        'mean': [np.mean(a = ls, axis =0).tolist(), np.mean(a = ls, axis = 1).tolist(), np.mean(a = ls)],
        'variance': [np.var(a = ls, axis =0).tolist(), np.var(a = ls, axis = 1).tolist(), np.var(a = ls)],
        'standard deviation': [np.std(a = ls, axis =0).tolist(), np.std(a = ls.tolist(), axis = 1).tolist(), np.std(a = ls)],
        'max': [np.amax(a = ls, axis =0).tolist(), np.amax(a = ls, axis = 1).tolist(), np.amax(a = ls)],
        'min': [np.amin(a = ls, axis =0).tolist(), np.amin(a = ls, axis = 1).tolist(), np.amin(a = ls)],
        'sum': [np.sum(a = ls, axis =0).tolist(), np.sum(a = ls, axis = 1).tolist(), np.sum(a = ls)]
        }


    return calculations