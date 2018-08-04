'''
# Write a python program to find the square root of the given number
# using approximation method
@author: shanmukhsurendra
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

    n_i = int(input())
    epsilon = 0.01
    step = 0.1
    guess = 0.0
    while abs(guess**2-n_i) >= epsilon:
        if guess <= n_i:
            guess += step
        else:
            break
    if abs(guess**2 - n_i) >= epsilon:
        print("failed")
    else:
        print(str(guess))

if __name__ == "__main__":
    main()
