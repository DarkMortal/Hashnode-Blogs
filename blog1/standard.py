def matrix_mult(A, B):
    #get the number of rows and columns of the 
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    #check if the matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError("Cannot multiply matrices:  incompatible dimensions.")
    #create the result matrix 
    c = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
             for k in range(cols_A):
                   c[i][j] += A[i][k] * B[k][j]
    return c

import time as T
def show_time(func):
    def inner(*args, **kwargs):
        start_time = T.time()
        res = func(*args, **kwargs)
        print(f'Time taken : {(T.time()-start_time)*(10**6)} {chr(181)}s')
        return res
    return inner

def disp(mat):
    for i in mat:
        for j in i:
            print(int(j),end=" ")
        print()