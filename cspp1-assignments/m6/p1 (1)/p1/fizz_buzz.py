'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    n = int(input())
    i_i = 0
    while i_i <= n:
        if(i_i % 3 == 0 and i_i % 5 == 0):
            print("Fizz")
            break
        elif i_i % 3 == 0:
          print("Fizz")
        elif i_i % 5 == 0:
           print("Buzz")
        print(i_i)
        i_i += 1

if __name__ == "__main__":
    main()
