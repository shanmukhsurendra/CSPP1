'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
@author : shanmukhsurendra
'''
def main():
    '''
    # Write a python program to find the square root of the given number
    # using approximation method
    '''
    s_a = int(input())
    epsilon = 0.01
    g_a = s_a/2.0
    while abs(g_a*g_a - s_a) >= epsilon:
        g_a = g_a - (((g_a**2) - s_a)/(2*g_a))
    print(str(g_a))

if __name__ == "__main__":
    main()
