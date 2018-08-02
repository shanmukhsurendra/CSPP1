'''
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
@author:shanmukhsurendra
here we print no vowels in given string
'''
def main():
    '''
    @author:shanmukhsurendra
    here we print no vowels in given string
    '''
    s_in = input()
    c_v = 0
    for char in s_in:
        if char in "aeiou":
            c_v += 1
    print(c_v)

if __name__ == "__main__":
    main()
