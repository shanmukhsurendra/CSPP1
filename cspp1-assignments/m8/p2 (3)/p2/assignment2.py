'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one
number and returns the sum of digits of given number.
@author:shanmukhsurendra
# This function takes in one number and returns one number.
'''

def sumofdigits(n_n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n_n == 0:
        return n_n
    return n_n % 10 +sumofdigits(n_n//10)
def main():
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    a_n = int(input())
    print(sumofdigits(int(a_n)))

if __name__ == "__main__":
    main()
