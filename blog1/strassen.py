def addMatrices(a,b):        
    x = [row[:] for row in a]
    for i in range(len(b)):
        for j in range(len(b[i])):
            x[i][j] += b[i][j]
    return x

def tokenize(matA,matB):
    # for matrix 1    
    if len(matA[0])&1:
        r = [0.0]
        for i in range(len(matA)):
            matA[i] = matA[i]+r
    if len(matA)&1:
        r = [0.0 for i in range(len(matA[0]))]
        matA.append(r)
        
    # now we must make the number of rows and columns equal
    ln = len(matA)-len(matA[0])
    if ln>0:
        r = [0.0 for i in range(ln)]
        for i in range(len(matA)):
            matA[i] = matA[i]+r
    if ln<0:
        r = [0.0 for i in range(len(matA[0]))]
        for i in range(-1*ln):
            matA.append(r)
            
    # for matrix 2
    # first we need to make the number of columns of matrix-1 equal to number of rows of matrix-2
    ln = len(matA[0])-len(matB)
    if ln:
        r = [0 for i in range(len(matB[0]))]
        for i in range(ln):
            matB.append(r)
    rem = len(matB[0])%len(matB)

    if(rem):
        r = [0.0 for i in range(len(matB)-rem)]
        for i in range(len(matB)):
            matB[i] = matB[i]+r
    # end of function

def strassen(mat1,mat2):

    # base condition
    if (len(mat1) == 2 and len(mat1[0]) == 2 
    and len(mat2) == 2 and len(mat2[0]) == 2):        
        a11 = mat1[0][0]*mat2[0][0]+mat1[0][1]*mat2[1][0]
        a12 = mat1[0][0]*mat2[0][1]+mat1[0][1]*mat2[1][1]
        a21 = mat1[1][0]*mat2[0][0]+mat1[1][1]*mat2[1][0]
        a22 = mat1[1][0]*mat2[0][1]+mat1[1][1]*mat2[1][1]
        return [[a11,a12],[a21,a22]]
    
    tokenize(mat1,mat2)            
    
    # number of equal parts of the matrices
    n = len(mat1)
    n = (n>>1) + (n&1)
            
    # dividing matrix-1
    mat11 = [[0.0 for i in range(n)] for j in range(n)]
    mat12 = [[0.0 for i in range(n)] for j in range(n)]
    mat13 = [[0.0 for i in range(n)] for j in range(n)]
    mat14 = [[0.0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            mat11[i][j] = mat1[i][j]
            mat12[i][j] = mat1[i][j+n]
            mat13[i][j] = mat1[i+n][j]
            mat14[i][j] = mat1[i+n][j+n]
                        
    # dividing matrix-2
    mat21 = [[0.0 for i in range(n)] for j in range(n)]
    mat22 = [[0.0 for i in range(n)] for j in range(n)]
    mat23 = [[0.0 for i in range(n)] for j in range(n)]
    mat24 = [[0.0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            mat21[i][j] = mat2[i][j]
            mat22[i][j] = mat2[i][j+n]
            mat23[i][j] = mat2[i+n][j]
            mat24[i][j] = mat2[i+n][j+n]
    
    m11 = addMatrices(strassen(mat11,mat21),strassen(mat12,mat23))
    m12 = addMatrices(strassen(mat11,mat22),strassen(mat12,mat24))
    m21 = addMatrices(strassen(mat13,mat21),strassen(mat14,mat23))
    m22 = addMatrices(strassen(mat13,mat22),strassen(mat14,mat24))
    
    # adding the matrices to make the result
    res = []
    for i in range(n):
        tempArr = m11[i][:]+m12[i][:]
        res.append(tempArr[:])
    for i in range(n):
        tempArr = m21[i][:]+m22[i][:]
        res.append(tempArr[:])

    return res

def rem0(res):
    resX = len(res[0])
    resY = len(res)
    # first for the columns
    listResX = []
    for i in range(resX):
        if res[0][i] == 0.0:
            isTrue = False
            for j in range(resY):
                isTrue = (res[j][i] == 0.0)
                if not isTrue:
                    break
            if isTrue:
                listResX.append(i)
    # similarly for the rows
    listResY = []
    for i in range(resY):
        if res[i][0] == 0.0:
            isTrue = False
            for j in range(resX):
                isTrue = (res[i][j] == 0.0)
                if not isTrue:
                    break
            if isTrue:
                listResY.append(i)
    # now we remove the elements
    for index in sorted(listResY, reverse=True):
        del res[index]
    resY = len(res)
    for index in sorted(listResX, reverse=True):
        for j in range(resY):
            del res[j][index]
    return res

def matMul(matX,matY):
    
    # if the matrices cannot be multiplied, we throw an exception
    if len(matX[0]) != len(matY):
        raise ArithmeticError("Matrices cannot be multiplied")
        
    matA = [row[:] for row in matX]
    matB = [row[:] for row in matY]
    
    tokenize(matA,matB)
        
    # now we must divide matrix-2 into equal parts where each matrix is a square matrix
    # for those matrices which is not a square matrix, we adjust them by adding columns of 0s
    # we multiply each matrices by matrix-1 and add the result
    
    sizeY = len(matB)
    sizeX = len(matB[0]) # this variable is going to be used a lot
            
    parts = sizeX/sizeY
    parts = int(parts)  # just to be safe
    
    res = []
    for p in range(0,parts):
        mat = [] # this is where we store the temporary matrix
        
        for i in range(sizeY):
            temp = []
            for j in range(sizeY):
                temp.append(matB[i][j+p*sizeY])
            mat.append(temp[:])
        
        if p == 0:
            res = strassen(matA,mat)
        else:  # join the matrices
            tmp = strassen(matA,mat)
            for i in range(sizeY):
                res[i] = res[i]+tmp[i]
                
    return rem0(res)