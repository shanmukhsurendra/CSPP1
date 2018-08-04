'''
# Write a python program to find the square root of the given number
# using approximation method
@author:shanmukhsurendra
# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''

def main():
    '''
    # Write a python program to find the square root of the given number
    # using approximation method
    '''
    n_n = int(input())
    epsilon = 0.01
    low = 0
    high = n_n
    mid = n_n/2
    while abs(mid**2-n_n) >= epsilon:
        if mid**2 < n_n:
            low = mid
        else:
            high = mid
        mid = (low + high)/2
        print(mid)
if __name__ == "__main__":
    main()
