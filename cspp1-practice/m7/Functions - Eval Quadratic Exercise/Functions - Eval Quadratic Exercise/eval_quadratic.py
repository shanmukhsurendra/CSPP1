'''
# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.
'''
def evalQuadratic(a_n, b_n, c_n, x_n):
    '''
    evakl quadratic
    '''
    return (a_n * (x_n ** 2)) + (b_n * x_n) + (c_n)
    

def main():
    '''
    evakl quadratic
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for x in range(len(data)):
        temp = str(data[x]).split('.')
        if(temp[1] == '0'):
            data[x] = int(float(str(data[x])))
        else:
            data[x] = data[x]
    print(evalQuadratic(data[0],data[1],data[2],data[3]))

if __name__== "__main__":
    main()

