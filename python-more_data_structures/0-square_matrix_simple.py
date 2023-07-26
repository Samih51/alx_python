def square_matrix_simple(matrix=[]):
    i=0
    length=len(matrix)
    square=[]
    while(i<length):
        result = map(lambda x : x**2, matrix[i])
        square.append(list(result))
        i+=1

    print (square)
    print (matrix)
square_matrix_simple([[1,2,3],[4,5]])
