'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def row_c(sudoku, lis_t):
    cou_nt = 0
    for i_i in sudoku:
        a_a = sorted(i_i)
        if lis_t == a_a:
            cou_nt += 1
        else:
            return False
    return cou_nt == len(sudoku)
def column_c(sudoku, lis_t):
    cou_nt = 0
    lis1_t = []
    for i_i in range(len(sudoku)):
        lis2_t = []
        for a_a in range(len(sudoku)):
            lis2_t.append(sudoku[a_a][i_i])
        lis1_t.append(lis2_t)
    for i_i in lis1_t:
        a_a = sorted(i_i)
        if lis_t == a_a:
            cou_nt += 1
        else:
            return False
    return cou_nt == len(sudoku)
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    lis_t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if row_c(sudoku, lis_t) and column_c(sudoku, lis_t):
        return True
    return False

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = list(map(int, input().split(' ')))
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()