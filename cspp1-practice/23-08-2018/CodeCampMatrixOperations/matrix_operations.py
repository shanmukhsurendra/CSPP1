def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    # l_new = []
    # if len(m1[0]) == len(m2):
    #     for i in range(len(m1)):
    #         for j in range(len(m2)):
    #             a += m1[i][j]*m2[j][i]
    #         l_new.append(a)
    grid = [[0]*len(m1)]*len(m2[0])
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                grid[i][j] += m1[i][k] * m2[k][j]
            print(grid)

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    l_new = []
    # try:
    if len(m1) == len(m2):
        for i in range(len(m1)):
            a_new = []
            for j in range(len(m2)):
                a_new.append(int(m1[i][j])+int(m2[i][j]))
            l_new.append(a_new)
    else:
        print("Error: Matrix shapes invalid for addition")
        print("None")
# except:
    #     return print("Error: Invalid input for the matrix")
    return (l_new)
def read_matrix():
    '''
    read the matrix dimensions from input
    create a list of lists and read the numbers into it
    in case there are not enough numbers given in the input
    print an error message and return None
    error message should be "Error: Invalid input for the matrix"
    '''
    lis_t = []
    lis_t_len = input().split(",")
    for i in range(int(lis_t_len[0])):
        lis_t.append(input().split(" "))
    return lis_t
def main():
    read_m = read_matrix()
    read2_m = read_matrix()
    # print(read_m)
    # print(read2_m)
    print(add_matrix(read_m, read2_m))
    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
