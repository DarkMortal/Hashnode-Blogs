import sys
from matrices import *
from strassen import matMul
from standard import matrix_mult, show_time as decorator, disp

@decorator
def strassen(mat1,mat2):
    return matMul(mat1,mat2)

@decorator
def normal(mat1,mat2):
    return matrix_mult(mat1,mat2)

if __name__=="__main__":
    isStandard = sys.argv[1] == '1'
    disp((normal(mat3,mat4) if isStandard else strassen(mat3,mat4)))
    print()
    disp((normal(mat5,mat6) if isStandard else strassen(mat5,mat6)))
    print()
    disp((normal(mat7,mat8) if isStandard else strassen(mat7,mat8)))
    print()
    disp((normal(mat7,mat9) if isStandard else strassen(mat7,mat9)))