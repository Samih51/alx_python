def print_matrix_integer(matrix=[[]]):
    outside_len=len(matrix)
    i=0
    j=0
    while(i<outside_len):
        inside_len=len(matrix[i])
        while (j<inside_len):
            print(matrix[i][j],end =" ")
            j+=1
        print()
        j=0
        i+=1

print_matrix_integer([[1,2,3],[4,5],[7]])