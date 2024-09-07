'''
Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, 
standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
The input of the function should be a list containing 9 digits. 
The function should convert the list into a 3 x 3 Numpy array, 

and then return a dictionary containing the mean, variance, standard deviation, max, min, 
and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:

{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
'''



import numpy as np

def calculate(list): 
    if len(list) > 9:
        raise ValueError("Count of values entered exceeds 9")

    matrix = np.array(list).reshape(3, 3)
    print(f'{matrix}') 
    row_mean, col_mean, flat_mean = [np.mean(matrix, axis = 0).tolist(), np.mean(matrix, axis = 1).tolist(), np.mean(matrix.flatten())]
    row_var, col_var, flat_var = [np.var(matrix, axis = 0).tolist(), np.var(matrix, axis = 1).tolist(), np.var(matrix.flatten())]
    row_std, col_std, flat_std = [np.std(matrix, axis = 0).tolist(), np.std(matrix, axis = 1).tolist(), np.std(matrix.flatten())]
    row_max, col_max, flat_max = [np.max(matrix, axis = 0).tolist(), np.max(matrix, axis = 1).tolist(), np.max(matrix.flatten())]
    row_min, col_min, flat_min = [np.min(matrix, axis = 0).tolist(), np.min(matrix, axis = 1).tolist(), np.min(matrix.flatten())]
    row_sum, col_sum, flat_sum = [np.sum(matrix, axis = 0).tolist(), np.sum(matrix, axis = 1).tolist(), np.sum(matrix.flatten())]
    
    dict = {
        'mean': [row_mean, col_mean, flat_mean],
        'variance': [row_var, col_var, flat_var],
        'standard deviation': [row_std, col_std, flat_std],
        'max': [row_max, col_max, flat_max],
        'min': [row_min, col_min, flat_min],
        'sum': [row_sum, col_sum, flat_sum]
    }
    return dict;
    
    

print(calculate([1,3,4,3,4,3,4,4,5]))
