'''
docstring
'''
def mult_matrix(ma_m, ma_mm):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    # l_new = []
    # if len(ma_m[0]) == len(ma_mm):
    #     for i in range(len(ma_m)):
    #         for j in range(len(ma_mm)):
    #             a += ma_m[i][j]*ma_mm[j][i]
    #         l_new.append(a)
    if len(ma_m) != len(ma_mm[0]):
        print("Error: Matrix shapes invalid for mult")
        return
     
    grid = [[0 for i in enumerate(ma_m)] for j in enumerate(ma_mm[0])]
    for i in range(len(ma_m)):
        for j in range(len(ma_mm[0])):
            for k in range(len(ma_mm)):
                grid[i][j]  += int(ma_m[i][k]) * int(ma_mm[k][j])

      return grid
def add_matrix(ma_m, ma_mm):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    l_new = []
    # try:
    if len(ma_m[0]) == len(ma_mm[0]):
        for i in range(len(ma_m)):
            a_new = []
            for j in range(len(ma_mm[0])):
                a_new.append(int(ma_m[i][j])+int(ma_mm[i][j]))
            l_new.append(a_new)
        return l_new
    else:
        print("Error: Matrix shapes invalid for addition")
        return None
# except:
    #     return print("Error: Invalid input for the matrix")
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
    rows, columns = int(lis_t_len[0]), int(lis_t_len[1])
    for i in range(int(lis_t_len[0])):
        li_matrix = input().split()
        if columns == len(li_matrix):
            lis_t.append([int(i) for i in li_matrix])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return lis_t

def main():
    read_m = read_matrix()
    if read_m is None:
        exit()
    read2_m = read_matrix()
    if read2_m is None:
        exit()
    # print(read_m)
    # print(read2_m)
    print(add_matrix(read_m, read2_m))
    print(mult_matrix(read_m, read2_m))
    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
