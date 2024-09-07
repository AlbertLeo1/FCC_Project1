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
    
