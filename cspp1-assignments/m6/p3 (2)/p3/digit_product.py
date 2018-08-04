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
    int_input = int(input())
     n_n = int(input())
    b_n = n_n
    res_n = 1
    if n_n < 0:
        n_n = - n_n
    while n_n > 0:
        a_n = n_n % 10
        res_n = res_n * a_n
        n_n = n_n // 10
    if b_n < 0:
        print(-res_n)
    if b_n > 0:
        print(res_n)
    if b_n == 0:
        print(b_n)
if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
