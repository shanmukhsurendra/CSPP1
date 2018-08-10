'''
#Exercise: Integer Division Exercise
#Modify the code for integer_division so that this error does not occur.
'''
def integer_division(x_x, a_a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count_c = 0
    while x_x >= a_a:
        count_c += 1
        x_x = x_x - a_a
    return count_c

def main():
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))


if __name__ == "__main__":
    main()
