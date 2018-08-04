'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
    @author:shanmukhsurendra
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    n_n = 145
    res_n = 1
    while n_n > 0:
        a_n = n_n % 10
        res_n = res_n * a_n
        n_n = n_n / 10
    print(res_n)

if __name__ == "__main__":
    main()
