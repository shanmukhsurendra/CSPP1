'''
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm
@author:shanmukh
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
'''

def main():
    '''
    # Write a python program to find if the given number is a perfect cube or not
    # using guess and check algorithm
    '''


    cube_n = int(input())
    epsilon = 0.01
    inc = 1
    guess = 0
    while guess <= cube_n:
        if abs(guess**3 -cube_n) < epsilon:
            break
        else:
            guess += inc
    if abs(guess**3 - cube_n) >= epsilon:
        print(str(cube_n) + "is not perfect cube")
    else:
        print(str(cube_n) + "is a perfect cube")
if __name__ == "__main__":
    main()
