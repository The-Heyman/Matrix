import numpy as np
from math import floor, ceil, sqrt
class Matrix:

    def __init__(self, matrix_string, m = 0, n = 0):
        self.matrix_string = matrix_string
        self.dex()
        #intialize m (row) and n (column) as dimensions of matrix m x n, 
        self.m = m
        self.n = n
    
    #define function to caltulate the dimentions of matrix
    def dex(self):

        #convert matrix_string into a list by stripping of whitespaces and 
        # newlines, then store length of string in string_length variable
        string_length = len(self.matrix_string.split())

        #calculate dimensions of matrix using ceil, sqrt and floor methods
        self.n = ceil(sqrt(string_length))
        self.m = floor(sqrt(string_length))
        if self.m * self.n < string_length:
            self.m = self.n

        return self.m, self.n
            
    #method to return indexed row from matrix
    def row(self, index):
        #list index
        index -= 1

        #call dex method to return m and n to this method scope
        self.dex()
        row_list = self.matrix_string.split()

        #create a nexted list of rows
        row_list = list(map(list, zip(*[map(int, row_list)] * self.m)))

        return row_list[index]
        
    #method to return indexed column from matrix
    def column(self, index):
        #list index
        index -= 1
        string_list = self.matrix_string.split()

        #convert list into m x n matrix using numpy
        matrix = np.array(string_list).reshape(self.dex())

        #convert matrix into a flat matrix along the column
        # and convert back to list
        column_list = list(matrix.flatten(order = "F"))

        #create nested list of columns
        column_list = list(map(list, zip( *[map(int, column_list)] * self.m)))

        return column_list[index]


#example 3 x 4 matrix string
matrix_string = "1 2 3 4\n5 6 7 8\n9 8 7 6"

T = Matrix(matrix_string)
R = T.row(1)
C = T.column(4)
print("matrix rows: {}" .format(T.m)) 
print("matrix columns: {}" .format(T.n)) 
print("Return row 1 of matrix: {}" .format(R))
print("Return column 4 of matrix: {}" .format(C))

