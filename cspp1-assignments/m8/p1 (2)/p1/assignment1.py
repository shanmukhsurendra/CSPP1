'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.
@author:shnamukhsurendra
# This function takes in one number and returns one number.
'''

def factorial(n_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n_n == 0 or n_n == 1:
        return 1  
    else:
        return n_n*factorial(n_n-1)
    


def main():
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''

    a = input()
    print(factorial(int(a)))    

if __name__== "__main__":
    main()
