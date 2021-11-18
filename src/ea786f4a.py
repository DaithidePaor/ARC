# Uses Depth-First-Search to identify the number of discrete objects (shapes) within the grid
# keeps track of each space in rows/columns scanned 
# returns the number of discrete objects which is used as a parameter to shape the size of the 
# output grid (numpy array) the output design is filled diagonally, the matrix is flipped and 
# filled diagonally from the opposite side also
# ARC task number: ea786f4a.json 

import numpy as np

class Matrix:
    def __init__(self, row, col, m):
        self.Row = row
        self.Col = col
        self.matrix = m
    
    # fx checks if a square can be included in the DFS, 
    # checks rows/cols values 1 and above
    # and has not been scanned 
    def isSafe(self, i, j, scan):
        return (i >=0 and i < self.Row and
               j >=0 and j <self.Col and not 
               scan[i][j] and self.matrix[i][j])
    
    # checks the neighbouring 8 squares 
    def DFS(self, i, j, scan):
        # get row / col nums of adjacent squares 
        rowNumr = [-1,-1, -1, 0, 0, 1, 1, 1];
        colNumr = [-1, 0, 1, -1, 1, -1, 0, -1];
        scan[i][j] = True # square has been scanned 
        # recursively check neighbours
        for k in range(8):
            if self.isSafe(i + rowNumr[k], j + colNumr[k], scan):
                self.DFS(i +rowNumr[k], j + colNumr[k], scan)
    
    # returns count of descrete object shapes in grid
    # passes the count as a parameter to an output grid (numpy array)
    # fills the output grid(new_array) with output shape 
    def discreteObj(self):
        # intialise a boolean array for scanned sqaures, initialise to False
        scan =[[False for j in range(self.Col)] for i in range(self.Row)]
        count = 0 
        # traverse across the matrix 
        for i in range(self.Row):
            for j in range(self.Col):
                # if a square greater than zero not yet scanned it is a new discrete object 
                if scan[i][j] == False and self.matrix[i][j] > 0:
                    self.DFS(i, j, scan)
                    # increment the count of discrete objects (and new_array size)
                    count += 1
                    # count is used as parameter to shape the size of output array
                    # !!! will need conditional statements here to deal with different colour grids / codes !!!
                    new_array = np.ones((count, count), dtype=int)
                    # fill design on the diagonals 
                    np.fill_diagonal(new_array,0)
                    np.fill_diagonal(np.fliplr(new_array), [0])
        
        return count, new_array
    
    
    

#test matrix # matrix will be input training matrix of n-dimensions from ARC dataset from PATH 
matrix = [[1,1,0,0,0],
        [0,1,0,0,0,],
        [1,0,0,1,1],
        [0,0,0,0,0],
        [1,0,1,0,1]]

row = len(matrix)
col = len(matrix[0])

# initalise Matrix 
m = Matrix(row, col, matrix)


# for testing purposes 
#print("Number of Discrete Objects is: ")
#print(m.discreteObj())
