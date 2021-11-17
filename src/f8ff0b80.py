# ARC f8ff0b80.json

# count number of objects in grid by counting frequency of non-zero elements
# build a 3 element 1-d column numpy array as ouput grid
# largest object (most elements in input grid) is first element, second is middle, and smallest is third element 

import as numpy as np 

# test input matrix # ! data will be provided from PATH 
x =[[0,0,0,2,2],
    [0,0,0,2,2],
    [0,0,0,0,0],
    [0,0,0,0,4,],
    [3,0,0,0,4]]

# get unique elements and count of each one (returns two arrays, elements and counts)	
np.unique(x, return_counts=True,)

# transpose row arrays into columns 
frequencies = np.asarray((np.unique(x, return_counts=True))).T
#print(frequencies)	

# sort columns into descending order
sort = frequencies[frequencies[:, 1].argsort()]
#print(sort)

# remove count column array
remove_col = sort[:,0]
#print(remove_col)

remove_black = np.trim_zeros(remove_col)
#print(remove_black)

# flip the array into asccending order with the colour of the largest object on top, smallest on the bottom
flip_em = np.flip(remove_black, axis=None)
#print(flip_em)

output_grid = np.c_[flip_em]
