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
    n_n = int(input())
    res_n = 1
    res_m = 0
    neg_n = 1
    if int(n_n) < 0:
       n_n = -int(input())
       for j in str(n_n):
           neg_n = int(j)*neg_n
    else:
        for i in n_n:
            neg_n = int(i)*res_n
    if int(n_n) < 0:
        neg_n = - neg_n
        print(neg_n)
    else:
        print(res_n)

if __name__ == "__main__":
    main()
