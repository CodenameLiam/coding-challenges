def flippingMatrix(matrix):
    matrixLength = len(matrix)
    matrixEnd = matrixLength - 1
    maxSum = 0

    for i in range(matrixLength//2):
        for j in range(matrixLength//2):
            maxSum += max(matrix[i][j], matrix[i][matrixEnd-j], matrix[matrixEnd-i][j], matrix[matrixEnd-i][matrixEnd-j])
    return maxSum

matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

print(flippingMatrix(matrix))